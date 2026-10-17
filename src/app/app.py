# -*- coding: utf-8 -*-
"""
Hệ thống Khảo sát & Đo lường Tương tác Thực nghiệm Đề tài 09
"Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo"
Chạy cục bộ trên Flask, hỗ trợ đo lường thời gian, độ tự tin và can thiệp nhận thức
"""

import os
import sys
import json
import time
import csv
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")
RESPONSES_FILE = os.path.join(DATA_DIR, "live_survey_responses.csv")

# Load bộ 60 câu hỏi
with open(os.path.join(DATA_DIR, "dataset_60_messages.json"), "r", encoding="utf-8") as f:
    ALL_MESSAGES = json.load(f)

PRE_MESSAGES = [m for m in ALL_MESSAGES if m["set"] == "Pre-test"]
POST_MESSAGES = [m for m in ALL_MESSAGES if m["set"] == "Post-test"]

@app.route("/")
def index():
    return render_template("index.html", pre_count=len(PRE_MESSAGES), post_count=len(POST_MESSAGES))

@app.route("/api/messages/<phase>")
def get_messages(phase):
    if phase == "pre":
        # Trả về các thông điệp Pre-test (ẩn ground_truth để tránh gian lận phía client)
        safe_msgs = [{k: v for k, v in m.items() if k not in ["ground_truth", "technical_indicators"]} for m in PRE_MESSAGES]
        return jsonify(safe_msgs)
    elif phase == "post":
        safe_msgs = [{k: v for k, v in m.items() if k not in ["ground_truth", "technical_indicators"]} for m in POST_MESSAGES]
        return jsonify(safe_msgs)
    return jsonify([])

@app.route("/api/submit_phase", methods=["POST"])
def submit_phase():
    payload = request.json
    participant_id = payload.get("participant_id", "PART_ANON")
    user_group = payload.get("user_group", "Student")
    phase = payload.get("phase", "Pre-test")
    answers = payload.get("answers", []) # list of {message_id, prediction, confidence, time_sec}

    lookup = {m["id"]: m for m in ALL_MESSAGES}
    results = []

    file_exists = os.path.exists(RESPONSES_FILE)
    fieldnames = [
        "participant_id", "user_group", "phase", "message_id", "message_type",
        "ground_truth", "user_prediction", "is_correct", "decision_time_sec",
        "confidence_score", "timestamp"
    ]

    with open(RESPONSES_FILE, "a", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()

        for ans in answers:
            m_id = ans.get("message_id")
            original = lookup.get(m_id, {})
            ground_truth = original.get("ground_truth", "Legitimate")
            pred = ans.get("prediction")
            is_correct = 1 if pred == ground_truth else 0

            row = {
                "participant_id": participant_id,
                "user_group": user_group,
                "phase": phase,
                "message_id": m_id,
                "message_type": original.get("type", "Unknown"),
                "ground_truth": ground_truth,
                "user_prediction": pred,
                "is_correct": is_correct,
                "decision_time_sec": ans.get("time_sec", 0),
                "confidence_score": ans.get("confidence", 3),
                "timestamp": datetime.now().isoformat()
            }
            writer.writerow(row)
            results.append({
                "message_id": m_id,
                "is_correct": is_correct,
                "ground_truth": ground_truth,
                "technical_indicators": original.get("technical_indicators", [])
            })

    # Tính điểm tóm tắt
    correct_count = sum(1 for r in results if r["is_correct"])
    total_count = len(results)
    score_pct = round((correct_count / total_count * 100), 1) if total_count > 0 else 0

    return jsonify({
        "status": "success",
        "phase": phase,
        "score_pct": score_pct,
        "correct_count": correct_count,
        "total_count": total_count,
        "details": results
    })

@app.route("/static/charts/<path:filename>")
def serve_charts(filename):
    chart_dir = os.path.join(app.root_path, "static", "charts")
    return send_from_directory(chart_dir, filename)

if __name__ == "__main__":
    print("=" * 60)
    print(" ỨNG DỤNG KHẢO SÁT THỰC NGHIỆM ĐỀ TÀI 09 ĐANG KHỞI CHẠY...")
    print(" Mở trình duyệt truy cập: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host="127.0.0.1", port=5000, debug=False)

