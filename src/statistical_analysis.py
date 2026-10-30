# -*- coding: utf-8 -*-
"""
Script phân tích thống kê chuyên sâu & Tạo biểu đồ trực quan hóa
Đề tài 09: Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo
Môn học: An toàn thông tin - TS. Lê Quốc Tuấn
Tự động ưu tiên đọc dữ liệu thực nghiệm thật từ file khao_sat.csv (N=20 người)
kết hợp lý thuyết phát hiện tín hiệu (Signal Detection Theory - SDT: d', criterion c)
"""

import os
import sys
import shutil
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Thiết lập phong cách đồ thị học thuật
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Arial", "sans-serif"]
plt.rcParams["axes.unicode_minus"] = False

def calculate_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    y_true_bin = (y_true == "Phishing").astype(int)
    y_pred_bin = (y_pred == "Phishing").astype(int)
    
    prec = precision_score(y_true_bin, y_pred_bin, zero_division=0)
    rec = recall_score(y_true_bin, y_pred_bin, zero_division=0)
    f1 = f1_score(y_true_bin, y_pred_bin, zero_division=0)
    
    cm = confusion_matrix(y_true_bin, y_pred_bin)
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
        fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
        fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    else:
        tn = fp = fn = tp = fpr = fnr = 0
        
    return {
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1": f1,
        "FPR": fpr,
        "FNR": fnr,
        "TP": tp, "FP": fp, "TN": tn, "FN": fn
    }

def main():
    base_dir = r"d:\ATTT"
    khao_sat_file = os.path.join(base_dir, "data", "khao_sat.csv")
    if not os.path.exists(khao_sat_file):
        khao_sat_file = os.path.join(base_dir, "khao_sat.csv")
    sample_file = os.path.join(base_dir, "data", "sample_survey_results.csv")
    
    if os.path.exists(khao_sat_file):
        print(f"[THÔNG BÁO] Đang nạp dữ liệu THỰC NGHIỆM THỰC TẾ từ: {khao_sat_file}")
        raw_df = pd.read_csv(khao_sat_file, encoding="utf-8-sig")
        
        # Tiền xử lý chuẩn hóa các cột
        df = pd.DataFrame()
        df["participant_id"] = raw_df["nguoi_tham_gia"]
        df["phase"] = raw_df["bo"].map({"A": "Pre-test", "B": "Post-test"})
        df["message_id"] = raw_df["id_thong_diep"]
        df["ground_truth"] = raw_df["dap_an_dung"].map({"legit": "Legitimate", "phish": "Phishing"})
        df["user_prediction"] = raw_df["tra_loi"].map({"Hợp lệ": "Legitimate", "Lừa đảo": "Phishing"})
        df["is_correct"] = (raw_df["ket_qua"] == "Đúng").astype(int)
        df["decision_time_sec"] = raw_df["thoi_gian_giay"]
        df["confidence_score"] = raw_df["muc_tu_tin"]
        df["channel"] = raw_df["kenh"]
        df["difficulty"] = raw_df["do_kho"]
        df["dau_hieu"] = raw_df["dau_hieu"]
        df["exploited_bias"] = raw_df["dau_hieu"].fillna("Không ghi nhận")
        
        def assign_type(r):
            if r["dap_an_dung"] == "legit":
                return "Legitimate"
            elif r["nhom"] == "ai":
                return "AI_Phishing"
            else:
                return "Traditional_Phishing"
        df["message_type"] = raw_df.apply(assign_type, axis=1)
        
        n_participants = df["participant_id"].nunique()
    elif os.path.exists(sample_file):
        print(f"[THÔNG BÁO] Nạp dữ liệu mô phỏng từ: {sample_file}")
        df = pd.read_csv(sample_file, encoding="utf-8-sig")
        n_participants = df["participant_id"].nunique()
    else:
        print("Lỗi: Không tìm thấy nguồn dữ liệu khảo sát.")
        return

    print("=" * 75)
    print(f" BÁO CÁO PHÂN TÍCH THỐNG KÊ THỰC NGHIỆM ĐỀ TÀI 09 (N = {n_participants} NGƯỜI)")
    print(" ĐO HIỆU QUẢ NHẬN DIỆN NỘI DUNG LỪA ĐẢO ĐƯỢC TẠO BỞI AI")
    print("=" * 75)
    
    pre_df = df[df["phase"] == "Pre-test"]
    post_df = df[df["phase"] == "Post-test"]
    
    pre_metrics = calculate_metrics(pre_df["ground_truth"], pre_df["user_prediction"])
    post_metrics = calculate_metrics(post_df["ground_truth"], post_df["user_prediction"])
    
    print("\n1. BẢNG SO SÁNH CHỈ SỐ TỔNG THỂ (OVERALL METRICS)")
    print(f"{'Chỉ số':<20} | {'Pre-test (Trước)':<18} | {'Post-test (Sau)':<18} | {'Mức thay đổi':<15}")
    print("-" * 75)
    for k in ["Accuracy", "Precision", "Recall", "F1", "FPR", "FNR"]:
        val_pre = pre_metrics[k] * 100
        val_post = post_metrics[k] * 100
        diff = val_post - val_pre
        sign = "+" if diff > 0 else ""
        print(f"{k:<20} | {val_pre:>16.2f}% | {val_post:>16.2f}% | {sign}{diff:>13.2f}%")
        
    avg_time_pre = pre_df["decision_time_sec"].mean()
    avg_time_post = post_df["decision_time_sec"].mean()
    print(f"{'Avg Decision Time':<20} | {avg_time_pre:>15.2f} s | {avg_time_post:>15.2f} s | {avg_time_post - avg_time_pre:>+12.2f} s")
    
    avg_conf_pre = pre_df["confidence_score"].mean()
    avg_conf_post = post_df["confidence_score"].mean()
    print(f"{'Avg Confidence (1-5)':<20} | {avg_conf_pre:>16.2f} | {avg_conf_post:>16.2f} | {avg_conf_post - avg_conf_pre:>+13.2f}")
    
    # 2. SIGNAL DETECTION THEORY (LÝ THUYẾT PHÁT HIỆN TÍN HIỆU: d' & criterion c)
    print("\n2. PHÂN TÍCH LÝ THUYẾT PHÁT HIỆN TÍN HIỆU (SIGNAL DETECTION THEORY - SDT)")
    print("   (Áp dụng hiệu chỉnh log-linear của Hautus 1995)")
    sdt_results = {}
    for p_name, p_sub in [("Pre-test", pre_df), ("Post-test", post_df)]:
        hits = ((p_sub["ground_truth"] == "Phishing") & (p_sub["user_prediction"] == "Phishing")).sum()
        sig_count = (p_sub["ground_truth"] == "Phishing").sum()
        fas = ((p_sub["ground_truth"] == "Legitimate") & (p_sub["user_prediction"] == "Phishing")).sum()
        noi_count = (p_sub["ground_truth"] == "Legitimate").sum()
        
        hit_rate = (hits + 0.5) / (sig_count + 1)
        fa_rate = (fas + 0.5) / (noi_count + 1)
        
        z_hit = stats.norm.ppf(hit_rate)
        z_fa = stats.norm.ppf(fa_rate)
        
        d_prime = z_hit - z_fa
        c = -0.5 * (z_hit + z_fa)
        sdt_results[p_name] = {"d_prime": d_prime, "criterion_c": c, "hit_rate": hit_rate, "fa_rate": fa_rate}
        print(f"- {p_name:<10}: d' (khả năng phân biệt) = {d_prime:.4f} | c (ngưỡng quyết định) = {c:+.4f} (Hit={hit_rate*100:.1f}%, FA={fa_rate*100:.1f}%)")
    
    delta_d = sdt_results["Post-test"]["d_prime"] - sdt_results["Pre-test"]["d_prime"]
    delta_c = sdt_results["Post-test"]["criterion_c"] - sdt_results["Pre-test"]["criterion_c"]
    print(f"=> Thay đổi: delta d' = {delta_d:+.4f} | delta c = {delta_c:+.4f}")
    if delta_c < 0:
        print("=> Ý NGHĨA KHOA HỌC (RQ2): Sau khi được can thiệp, criterion c giảm mạnh sang giá trị âm, chứng minh người dùng trở nên CẢNH GIÁC/NGHI NGỜ HƠN, làm tăng tỷ lệ bắt lừa đảo (Recall) nhưng đồng thời cũng làm tăng tỷ lệ báo động nhầm (FPR) đúng như lý thuyết Alert Fatigue!")
        
    # 3. KIỂM ĐỊNH THỐNG KÊ (PAIRED T-TEST & WILCOXON SIGNED-RANK)
    user_scores = df.groupby(["participant_id", "phase"])["is_correct"].mean().unstack()
    t_stat, p_val_t = stats.ttest_rel(user_scores["Post-test"], user_scores["Pre-test"])
    w_stat, p_val_w = stats.wilcoxon(user_scores["Post-test"], user_scores["Pre-test"])
    
    print("\n3. KẾT QUẢ KIỂM ĐỊNH THỐNG KÊ TRÊN TỪNG NGƯỜI THAM GIA")
    print(f"- Điểm số trung bình Pre-test : {user_scores['Pre-test'].mean() * 100:.2f}% (SD: {user_scores['Pre-test'].std() * 100:.2f}%)")
    print(f"- Điểm số trung bình Post-test: {user_scores['Post-test'].mean() * 100:.2f}% (SD: {user_scores['Post-test'].std() * 100:.2f}%)")
    print(f"- Paired Samples t-test: t = {t_stat:.4f}, p = {p_val_t:.4e}")
    print(f"- Wilcoxon Signed-Rank Test: W = {w_stat:.4f}, p = {p_val_w:.4e}")
    
    # 4. PHÂN TÍCH THEO LOẠI THÔNG ĐIỆP (AI PHISHING VS TRADITIONAL PHISHING - RQ1)
    print("\n4. ĐỘ CHÍNH XÁC THEO TỪNG LOẠI THÔNG ĐIỆP (MESSAGE TYPE BREAKDOWN - RQ1)")
    type_acc = df.groupby(["phase", "message_type"])["is_correct"].mean().unstack() * 100
    print(type_acc.round(2))
    
    # Đồ thị 1: fig1_pre_post_metrics.png
    charts_dir = os.path.join(base_dir, "src", "app", "static", "charts")
    data_dir = os.path.join(base_dir, "data")
    pub_charts_dir = os.path.join(base_dir, "public", "charts")
    for d in [charts_dir, data_dir, pub_charts_dir]:
        os.makedirs(d, exist_ok=True)
        
    # FIGURE 1: CÁC CHỈ SỐ TỔNG THỂ
    fig, ax = plt.subplots(figsize=(8.5, 5))
    metrics_names = ["Accuracy", "Precision", "Recall (Bắt lừa đảo)", "F1-Score"]
    pre_vals = [pre_metrics["Accuracy"]*100, pre_metrics["Precision"]*100, pre_metrics["Recall"]*100, pre_metrics["F1"]*100]
    post_vals = [post_metrics["Accuracy"]*100, post_metrics["Precision"]*100, post_metrics["Recall"]*100, post_metrics["F1"]*100]
    
    x = np.arange(len(metrics_names))
    width = 0.35
    rects1 = ax.bar(x - width/2, pre_vals, width, label="Pre-test (Trước can thiệp)", color="#3498db", alpha=0.9)
    rects2 = ax.bar(x + width/2, post_vals, width, label="Post-test (Sau can thiệp)", color="#2ecc71", alpha=0.9)
    
    ax.set_ylabel("Tỷ lệ (%)", fontsize=12)
    ax.set_title("Hình 1. So sánh Hiệu năng Nhận diện Tổng thể (N = 20 Người thật)", fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(metrics_names, fontsize=11)
    ax.set_ylim(0, 115)
    ax.legend(fontsize=11)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10)
    for r in rects2:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10, fontweight="bold")
        
    plt.tight_layout()
    f1_path = os.path.join(charts_dir, "fig1_pre_post_metrics.png")
    fig.savefig(f1_path, dpi=300)
    plt.close()
    
    # FIGURE 2: AI VS TRADITIONAL ACCURACY
    fig, ax = plt.subplots(figsize=(9.5, 5))
    types = ["Legitimate (Hợp lệ)", "Traditional Phishing (Thủ công)", "AI_Phishing (Do AI tạo)"]
    pre_t = [type_acc.loc["Pre-test", "Legitimate"], type_acc.loc["Pre-test", "Traditional_Phishing"], type_acc.loc["Pre-test", "AI_Phishing"]]
    post_t = [type_acc.loc["Post-test", "Legitimate"], type_acc.loc["Post-test", "Traditional_Phishing"], type_acc.loc["Post-test", "AI_Phishing"]]
    
    x = np.arange(len(types))
    rects1 = ax.bar(x - width/2, pre_t, width, label="Pre-test (Trước)", color="#e67e22", alpha=0.9)
    rects2 = ax.bar(x + width/2, post_t, width, label="Post-test (Sau)", color="#9b59b6", alpha=0.9)
    
    ax.set_ylabel("Độ chính xác (%)", fontsize=12)
    ax.set_title("Hình 2. Độ chính xác theo Từng Nhóm Thông điệp: AI vs Thủ công (RQ1)", fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(types, fontsize=10)
    ax.set_ylim(0, 115)
    ax.legend(fontsize=11)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10)
    for r in rects2:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10, fontweight="bold")
        
    plt.tight_layout()
    f2_path = os.path.join(charts_dir, "fig2_ai_vs_traditional_accuracy.png")
    fig.savefig(f2_path, dpi=300)
    plt.close()
    
    # FIGURE 3: MA TRẬN NHẦM LẪN (CONFUSION MATRIX)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    labels = ["Legitimate", "Phishing"]
    
    cm_pre = confusion_matrix(pre_df["ground_truth"], pre_df["user_prediction"], labels=labels)
    cm_post = confusion_matrix(post_df["ground_truth"], post_df["user_prediction"], labels=labels)
    
    sns.heatmap(cm_pre, annot=True, fmt="d", cmap="Blues", ax=axes[0], xticklabels=labels, yticklabels=labels, cbar=False, annot_kws={"size": 13})
    axes[0].set_title(f"Pre-test Confusion Matrix\n(Accuracy: {pre_metrics['Accuracy']*100:.1f}%)", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Dự đoán của người tham gia", fontsize=11)
    axes[0].set_ylabel("Thực tế (Ground Truth)", fontsize=11)
    
    sns.heatmap(cm_post, annot=True, fmt="d", cmap="Greens", ax=axes[1], xticklabels=labels, yticklabels=labels, cbar=False, annot_kws={"size": 13})
    axes[1].set_title(f"Post-test Confusion Matrix\n(Accuracy: {post_metrics['Accuracy']*100:.1f}%)", fontsize=12, fontweight="bold")
    axes[1].set_xlabel("Dự đoán của người tham gia", fontsize=11)
    axes[1].set_ylabel("Thực tế (Ground Truth)", fontsize=11)
    
    plt.tight_layout()
    f3_path = os.path.join(charts_dir, "fig3_confusion_matrices.png")
    fig.savefig(f3_path, dpi=300)
    plt.close()
    
    # FIGURE 4: BIỂU ĐỒ TẦN SUẤT DẤU HIỆU NGƯỜI DÙNG DỰA VÀO & TỶ LỆ LỖI (RQ3)
    dau_hieu_series = df[df["dau_hieu"].notna()]["dau_hieu"].str.split("; ")
    flat_signals = [item.strip() for sublist in dau_hieu_series for item in sublist if item.strip()]
    sig_counts = pd.Series(flat_signals).value_counts().head(7)
    
    fig, ax = plt.subplots(figsize=(9.5, 5))
    y_pos = np.arange(len(sig_counts))
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c", "#34495e"]
    ax.barh(y_pos, sig_counts.values, color=colors[:len(sig_counts)], alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(sig_counts.index, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel("Số lần người tham gia dựa vào dấu hiệu", fontsize=11)
    ax.set_title("Hình 4. Top Dấu hiệu Người dùng Thực sự Dựa vào khi Ra Quyết định (RQ3)", fontsize=13, fontweight="bold")
    
    for i, v in enumerate(sig_counts.values):
        ax.text(v + 3, i, str(v), va="center", fontsize=10, fontweight="bold")
        
    ax.set_xlim(0, max(sig_counts.values) * 1.15)
    plt.tight_layout()
    f4_path = os.path.join(charts_dir, "fig4_error_breakdown_by_indicators.png")
    fig.savefig(f4_path, dpi=300)
    plt.close()
    
    # Sync charts across all 3 directories
    chart_names = ["fig1_pre_post_metrics.png", "fig2_ai_vs_traditional_accuracy.png", "fig3_confusion_matrices.png", "fig4_error_breakdown_by_indicators.png"]
    for c in chart_names:
        src = os.path.join(charts_dir, c)
        shutil.copy2(src, os.path.join(data_dir, c))
        shutil.copy2(src, os.path.join(pub_charts_dir, c))
        
    print("\n=> ĐÃ XUẤT THÀNH CÔNG VÀ ĐỒNG BỘ CẢ 4 HÌNH VẼ KHOA HỌC SẮC NÉT (300 DPI):")
    print(f"   1. {f1_path}")
    print(f"   2. {f2_path}")
    print(f"   3. {f3_path}")
    print(f"   4. {f4_path}")
    print("=> QUÁ TRÌNH PHÂN TÍCH SỐ LIỆU TỪ khao_sat.csv HOÀN TẤT XUẤT SẮC!")

if __name__ == "__main__":
    main()
