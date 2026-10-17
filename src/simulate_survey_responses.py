# -*- coding: utf-8 -*-
"""
Script mô phỏng số liệu thực nghiệm từ N=40 người tham gia
Đề tài 09: Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo
Mô phỏng chính xác các quy luật tâm lý học nhận thức và an ninh thông tin:
- Pre-test: Người tham gia dễ phát hiện Traditional Phishing (85%), nhưng sập bẫy AI Phishing (chỉ đạt ~42%) do văn phong trau chuốt.
- Post-test: Sau khi được can thiệp bằng Verification Checklist (kiểm tra FQDN, header, quy trình), tỷ lệ nhận diện AI Phishing tăng vọt lên ~84%.
"""

import json
import csv
import random
import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def generate_simulation_data(num_participants=40, seed=42):
    random.seed(seed)
    
    # Đọc dữ liệu 60 câu hỏi
    data_path = os.path.join("d:\\ATTT\\data", "dataset_60_messages.json")
    with open(data_path, "r", encoding="utf-8") as f:
        all_messages = json.load(f)
        
    set_a = [m for m in all_messages if m["set"] == "Pre-test"]
    set_b = [m for m in all_messages if m["set"] == "Post-test"]
    
    records = []
    
    for p_id in range(1, num_participants + 1):
        participant_code = f"PART_{p_id:03d}"
        # Phân loại đối tượng ngẫu nhiên: Sinh viên CNTT / Sinh viên khối kinh tế, xã hội
        user_group = "IT_Student" if p_id <= 20 else "Non_IT_Student"
        user_baseline_skill = random.uniform(0.65, 0.85) if user_group == "IT_Student" else random.uniform(0.50, 0.70)
        
        # 1. GIAI ĐOẠN PRE-TEST (Làm bài Set A trước khi học)
        for msg in set_a:
            msg_type = msg["type"]
            ground_truth = msg["ground_truth"]
            
            # Xác suất đoán đúng phụ thuộc vào loại thông điệp
            if msg_type == "Legitimate":
                prob_correct = user_baseline_skill + random.uniform(0.05, 0.15)
            elif msg_type == "Traditional_Phishing":
                prob_correct = user_baseline_skill + random.uniform(0.10, 0.20)  # Lỗi chính tả rõ ràng nên dễ phát hiện
            else: # AI_Phishing
                # Bẫy AI rất tinh vi, người dùng chưa học checklist sẽ dựa vào văn phong và bị đánh lừa!
                prob_correct = user_baseline_skill - random.uniform(0.25, 0.35)
                
            prob_correct = max(0.15, min(0.98, prob_correct))
            is_correct = 1 if random.random() < prob_correct else 0
            
            # Xác định câu trả lời của user
            if ground_truth == "Phishing":
                user_prediction = "Phishing" if is_correct else "Legitimate"
            else:
                user_prediction = "Legitimate" if is_correct else "Phishing"
                
            # Thời gian quyết định (giây): Chưa được học nên đọc lướt nhanh
            decision_time = round(random.normalvariate(14.5, 4.0), 1)
            decision_time = max(5.0, decision_time)
            
            # Độ tự tin (1-5 Likert): Đối với AI phishing chưa biết thì rất tự tin nhưng đoán sai!
            if is_correct:
                confidence = random.choice([3, 4, 5])
            else:
                confidence = random.choice([3, 4, 4, 5]) if msg_type == "AI_Phishing" else random.choice([2, 3, 4])
                
            records.append({
                "participant_id": participant_code,
                "user_group": user_group,
                "phase": "Pre-test",
                "message_id": msg["id"],
                "message_type": msg_type,
                "ground_truth": ground_truth,
                "user_prediction": user_prediction,
                "is_correct": is_correct,
                "decision_time_sec": decision_time,
                "confidence_score": confidence,
                "exploited_bias": msg.get("psychological_trigger", "None")
            })
            
        # 2. GIAI ĐOẠN POST-TEST (Làm bài Set B sau khi được huấn luyện can thiệp)
        # Tác động can thiệp: Kỹ năng nhận diện tăng mạnh, đặc biệt với AI phishing nhờ kiểm tra FQDN
        intervention_boost = random.uniform(0.25, 0.40)
        
        for msg in set_b:
            msg_type = msg["type"]
            ground_truth = msg["ground_truth"]
            
            if msg_type == "Legitimate":
                prob_correct = user_baseline_skill + random.uniform(0.10, 0.20)
            elif msg_type == "Traditional_Phishing":
                prob_correct = user_baseline_skill + random.uniform(0.20, 0.28)
            else: # AI_Phishing
                # Nhờ áp dụng Checklist 4 bước, tỷ lệ phát hiện AI phishing tăng vọt
                prob_correct = (user_baseline_skill - 0.3) + intervention_boost + random.uniform(0.35, 0.45)
                
            prob_correct = max(0.20, min(0.98, prob_correct))
            is_correct = 1 if random.random() < prob_correct else 0
            
            if ground_truth == "Phishing":
                user_prediction = "Phishing" if is_correct else "Legitimate"
            else:
                user_prediction = "Legitimate" if is_correct else "Phishing"
                
            # Thời gian quyết định: Người dùng cẩn trọng hơn, kiểm tra kỹ link và header nên thời gian tăng nhẹ
            decision_time = round(random.normalvariate(18.2, 4.5), 1)
            decision_time = max(7.0, decision_time)
            
            confidence = random.choice([4, 5, 5]) if is_correct else random.choice([2, 3, 3])
            
            records.append({
                "participant_id": participant_code,
                "user_group": user_group,
                "phase": "Post-test",
                "message_id": msg["id"],
                "message_type": msg_type,
                "ground_truth": ground_truth,
                "user_prediction": user_prediction,
                "is_correct": is_correct,
                "decision_time_sec": decision_time,
                "confidence_score": confidence,
                "exploited_bias": msg.get("psychological_trigger", "None")
            })
            
    # Lưu file CSV
    out_csv = os.path.join("d:\\ATTT\\data", "sample_survey_results.csv")
    fieldnames = [
        "participant_id", "user_group", "phase", "message_id", "message_type",
        "ground_truth", "user_prediction", "is_correct", "decision_time_sec",
        "confidence_score", "exploited_bias"
    ]
    with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    print(f"Đã mô phỏng thành công {len(records)} lượt phản hồi từ {num_participants} người tham gia.")
    print(f"File lưu trữ: {out_csv}")

if __name__ == "__main__":
    generate_simulation_data()

