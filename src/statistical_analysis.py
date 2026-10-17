# -*- coding: utf-8 -*-
"""
Script phân tích thống kê chuyên sâu & Tạo biểu đồ trực quan hóa
Đề tài 09: Đo hiệu quả nhận diện nội dung lừa đảo được tạo bởi trí tuệ nhân tạo
Môn học: An toàn thông tin - TS. Lê Quốc Tuấn
"""

import os
import sys
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
    # Phishing = 1 (Positive), Legitimate = 0 (Negative)
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
    csv_file = os.path.join("d:\\ATTT\\data", "sample_survey_results.csv")
    if not os.path.exists(csv_file):
        print(f"Không tìm thấy file: {csv_file}")
        return
        
    df = pd.read_csv(csv_file, encoding="utf-8-sig")
    print("=" * 70)
    print(" BÁO CÁO PHÂN TÍCH THỐNG KÊ THỰC NGHIỆM ĐỀ TÀI 09")
    print(" ĐO HIỆU QUẢ NHẬN DIỆN NỘI DUNG LỪA ĐẢO ĐƯỢC TẠO BỞI AI")
    print("=" * 70)
    
    pre_df = df[df["phase"] == "Pre-test"]
    post_df = df[df["phase"] == "Post-test"]
    
    pre_metrics = calculate_metrics(pre_df["ground_truth"], pre_df["user_prediction"])
    post_metrics = calculate_metrics(post_df["ground_truth"], post_df["user_prediction"])
    
    print("\n1. BẢNG SO SÁNH CHỈ SỐ TỔNG THỂ (OVERALL METRICS)")
    print(f"{'Chỉ số':<20} | {'Pre-test (Trước)':<18} | {'Post-test (Sau)':<18} | {'Mức cải thiện':<15}")
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
    
    # 2. KIỂM ĐỊNH THỐNG KÊ (PAIRED T-TEST & WILCOXON)
    user_scores = df.groupby(["participant_id", "phase"])["is_correct"].mean().unstack()
    t_stat, p_val_t = stats.ttest_rel(user_scores["Post-test"], user_scores["Pre-test"])
    w_stat, p_val_w = stats.wilcoxon(user_scores["Post-test"], user_scores["Pre-test"])
    
    print("\n2. KẾT QUẢ KIỂM ĐỊNH GIẢ THUYẾT THỐNG KÊ (N=40)")
    print(f"- Điểm số trung bình Pre-test : {user_scores['Pre-test'].mean() * 100:.2f}% (SD: {user_scores['Pre-test'].std() * 100:.2f}%)")
    print(f"- Điểm số trung bình Post-test: {user_scores['Post-test'].mean() * 100:.2f}% (SD: {user_scores['Post-test'].std() * 100:.2f}%)")
    print(f"- Paired Samples t-test: t-statistic = {t_stat:.4f}, p-value = {p_val_t:.4e}")
    print(f"- Wilcoxon Signed-Rank Test: statistic = {w_stat:.4f}, p-value = {p_val_w:.4e}")
    if p_val_t < 0.001:
        print("=> KẾT LUẬN: Sự cải thiện năng lực nhận diện sau can thiệp huấn luyện là CỰC KỲ CÓ Ý NGHĨA THỐNG KÊ (p < 0.001).")
        
    # 3. PHÂN TÍCH THEO LOẠI THÔNG ĐIỆP (AI PHISHING VS TRADITIONAL PHISHING)
    print("\n3. ĐỘ CHÍNH XÁC THEO TỪNG LOẠI THÔNG ĐIỆP (MESSAGE TYPE BREAKDOWN)")
    type_acc = df.groupby(["phase", "message_type"])["is_correct"].mean().unstack() * 100
    print(type_acc.round(2))
    
    # Tỷ lệ sập bẫy AI phishing trước can thiệp
    pre_ai_acc = type_acc.loc["Pre-test", "AI_Phishing"]
    post_ai_acc = type_acc.loc["Post-test", "AI_Phishing"]
    print(f"=> Độ chính xác nhận diện AI Phishing đã tăng từ {pre_ai_acc:.1f}% lên {post_ai_acc:.1f}% (Tăng {post_ai_acc - pre_ai_acc:+.1f}%)")
    
    # 4. XUẤT CÁC BIỂU ĐỒ MINH CHỨNG
    charts_dir = os.path.join("d:\\ATTT\\src\\app\\static", "charts")
    data_dir = "d:\\ATTT\\data"
    os.makedirs(charts_dir, exist_ok=True)
    
    # BIỂU ĐỒ 1: SO SÁNH CHỈ SỐ PRE VS POST
    fig, ax = plt.subplots(figsize=(8, 5))
    metrics_names = ["Accuracy", "Precision", "Recall (Detection)", "F1-Score"]
    pre_vals = [pre_metrics["Accuracy"]*100, pre_metrics["Precision"]*100, pre_metrics["Recall"]*100, pre_metrics["F1"]*100]
    post_vals = [post_metrics["Accuracy"]*100, post_metrics["Precision"]*100, post_metrics["Recall"]*100, post_metrics["F1"]*100]
    
    x = np.arange(len(metrics_names))
    width = 0.35
    rects1 = ax.bar(x - width/2, pre_vals, width, label="Pre-test (Trước can thiệp)", color="#e74c3c", alpha=0.9)
    rects2 = ax.bar(x + width/2, post_vals, width, label="Post-test (Sau can thiệp)", color="#2ecc71", alpha=0.9)
    
    ax.set_ylabel("Tỷ lệ (%)", fontsize=12)
    ax.set_title("So sánh Hiệu năng Nhận diện Tổng thể (Pre-test vs Post-test)", fontsize=14, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(metrics_names, fontsize=11)
    ax.set_ylim(0, 110)
    ax.legend(fontsize=11)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10)
    for r in rects2:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=10, fontweight="bold")
        
    plt.tight_layout()
    fig1_path = os.path.join(charts_dir, "fig1_pre_post_metrics.png")
    fig.savefig(fig1_path, dpi=300)
    fig.savefig(os.path.join(data_dir, "fig1_pre_post_metrics.png"), dpi=300)
    plt.close()
    print(f"- Đã lưu Biểu đồ 1: {fig1_path}")
    
    # BIỂU ĐỒ 2: PHÂN TÍCH NHẬN DIỆN AI PHISHING VS TRADITIONAL PHISHING
    fig, ax = plt.subplots(figsize=(9, 5))
    types = ["Legitimate (Hợp lệ)", "Traditional Phishing (Truyền thống)", "AI-Generated Phishing (Do AI tạo)"]
    pre_t = [type_acc.loc["Pre-test", "Legitimate"], type_acc.loc["Pre-test", "Traditional_Phishing"], type_acc.loc["Pre-test", "AI_Phishing"]]
    post_t = [type_acc.loc["Post-test", "Legitimate"], type_acc.loc["Post-test", "Traditional_Phishing"], type_acc.loc["Post-test", "AI_Phishing"]]
    
    x = np.arange(len(types))
    rects1 = ax.bar(x - width/2, pre_t, width, label="Pre-test", color="#3498db", alpha=0.85)
    rects2 = ax.bar(x + width/2, post_t, width, label="Post-test", color="#9b59b6", alpha=0.85)
    
    ax.set_ylabel("Độ chính xác (%)", fontsize=12)
    ax.set_title("Độ chính xác theo Từng Nhóm Thông điệp: AI vs Truyền thống", fontsize=14, fontweight="bold")
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
    fig2_path = os.path.join(charts_dir, "fig2_ai_vs_traditional_accuracy.png")
    fig.savefig(fig2_path, dpi=300)
    fig.savefig(os.path.join(data_dir, "fig2_ai_vs_traditional_accuracy.png"), dpi=300)
    plt.close()
    print(f"- Đã lưu Biểu đồ 2: {fig2_path}")
    
    # BIỂU ĐỒ 3: CONFUSION MATRIX PRE VS POST
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    labels = ["Legitimate", "Phishing"]
    
    cm_pre = confusion_matrix(pre_df["ground_truth"], pre_df["user_prediction"], labels=labels)
    cm_post = confusion_matrix(post_df["ground_truth"], post_df["user_prediction"], labels=labels)
    
    sns.heatmap(cm_pre, annot=True, fmt="d", cmap="Reds", ax=axes[0], xticklabels=labels, yticklabels=labels, cbar=False, annot_kws={"size": 13})
    axes[0].set_title(f"Pre-test Confusion Matrix\n(Accuracy: {pre_metrics['Accuracy']*100:.1f}%)", fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Dự đoán của người dùng", fontsize=11)
    axes[0].set_ylabel("Thực tế (Ground Truth)", fontsize=11)
    
    sns.heatmap(cm_post, annot=True, fmt="d", cmap="Greens", ax=axes[1], xticklabels=labels, yticklabels=labels, cbar=False, annot_kws={"size": 13})
    axes[1].set_title(f"Post-test Confusion Matrix\n(Accuracy: {post_metrics['Accuracy']*100:.1f}%)", fontsize=12, fontweight="bold")
    axes[1].set_xlabel("Dự đoán của người dùng", fontsize=11)
    axes[1].set_ylabel("Thực tế (Ground Truth)", fontsize=11)
    
    plt.tight_layout()
    fig3_path = os.path.join(charts_dir, "fig3_confusion_matrices.png")
    fig.savefig(fig3_path, dpi=300)
    fig.savefig(os.path.join(data_dir, "fig3_confusion_matrices.png"), dpi=300)
    plt.close()
    print(f"- Đã lưu Biểu đồ 3: {fig3_path}")
    
    # BIỂU ĐỒ 4: BIỂU ĐỒ LỖI THEO NHÓM DẤU HIỆU / ĐÒN BẨY TÂM LÝ (BẮT BUỘC THEO ĐỀ CƯƠNG)
    phish_df = df[df["ground_truth"] == "Phishing"].copy()
    phish_df["error"] = 1 - phish_df["is_correct"]
    error_summary = phish_df.groupby(["phase", "exploited_bias"])["error"].mean().unstack() * 100
    
    fig, ax = plt.subplots(figsize=(10, 5))
    bias_order = error_summary.mean().sort_values(ascending=False).index[:6]
    
    x = np.arange(len(bias_order))
    pre_err = [error_summary.loc["Pre-test", b] if b in error_summary.columns else 0 for b in bias_order]
    post_err = [error_summary.loc["Post-test", b] if b in error_summary.columns else 0 for b in bias_order]
    
    rects1 = ax.bar(x - width/2, pre_err, width, label="Tỷ lệ sập bẫy Pre-test", color="#d35400", alpha=0.9)
    rects2 = ax.bar(x + width/2, post_err, width, label="Tỷ lệ sập bẫy Post-test", color="#27ae60", alpha=0.9)
    
    ax.set_ylabel("Tỷ lệ phán đoán sai / Sập bẫy (%)", fontsize=12)
    ax.set_title("Biểu đồ Phân tích Lỗi theo Nhóm Đòn bẩy Tâm lý & Ngữ cảnh (Error Analysis Breakdown)", fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    clean_labels = [b.replace(" & ", "\n")[:25] for b in bias_order]
    ax.set_xticklabels(clean_labels, fontsize=9, rotation=15)
    ax.set_ylim(0, 100)
    ax.legend(fontsize=11)
    
    for r in rects1:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=9)
    for r in rects2:
        h = r.get_height()
        ax.annotate(f"{h:.1f}%", xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=9, fontweight="bold")
        
    plt.tight_layout()
    fig4_path = os.path.join(charts_dir, "fig4_error_breakdown_by_indicators.png")
    fig.savefig(fig4_path, dpi=300)
    fig.savefig(os.path.join(data_dir, "fig4_error_breakdown_by_indicators.png"), dpi=300)
    plt.close()
    print(f"- Đã lưu Biểu đồ 4: {fig4_path}")
    
    print("\n=> QUÁ TRÌNH PHÂN TÍCH THỐNG KÊ HOÀN TẤT XUẤT SẮC!")

if __name__ == "__main__":
    main()

