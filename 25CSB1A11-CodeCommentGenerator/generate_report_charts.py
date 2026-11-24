import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"C:\Users\saksh\OneDrive\Documents\CodeCommentGenerator\report_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Figure 2(a): SafeDocGen Natural Language Generation Quality (BLEU vs ROUGE)
# -------------------------------------------------------------
def make_fig2a():
    categories = ['Docstring\nGen', 'Inline\nComments', 'Loop\nLogic', 'Function\nSummary', 'Class\nOverview', 'Exception\nBlocks', 'Security\nAudit']
    bleu_scores = [0.438, 0.424, 0.410, 0.446, 0.418, 0.412, 0.442]
    rouge_scores = [0.528, 0.514, 0.496, 0.534, 0.485, 0.498, 0.526]
    
    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=300)
    
    # Custom styling matching Saksham's original PDF
    rects1 = ax.bar(x - width/2, bleu_scores, width, label='BLEU-4 Score (Mean: 0.428)', color='#1d4ed8', edgecolor='#1e40af', alpha=0.9)
    rects2 = ax.bar(x + width/2, rouge_scores, width, label='ROUGE-L Score (Mean: 0.512)', color='#10b981', edgecolor='#059669', alpha=0.9)

    # Horizontal mean lines
    ax.axhline(0.428, color='#1d4ed8', linestyle=':', linewidth=1.5, label='Avg BLEU (0.428)')
    ax.axhline(0.512, color='#10b981', linestyle=':', linewidth=1.5, label='Avg ROUGE (0.512)')

    ax.set_ylabel('Score (0.0 - 1.0)', fontsize=10, fontweight='bold')
    ax.set_title('Figure 2(a): SafeDocGen Natural Language Generation Quality (BLEU vs ROUGE)', fontsize=11, fontweight='bold', pad=12)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 0.65)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    ax.legend(loc='upper right', framealpha=0.9, fontsize=8.5)

    # Add value labels on top of bars
    for r in rects1:
        h = r.get_height()
        ax.annotate(f'{h:.3f}', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 2),
                    textcoords="offset points", ha='center', va='bottom', fontsize=7, rotation=45)
    for r in rects2:
        h = r.get_height()
        ax.annotate(f'{h:.3f}', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 2),
                    textcoords="offset points", ha='center', va='bottom', fontsize=7, rotation=45)

    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "fig2a_bleu_rouge.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print("Saved:", out_path)

# -------------------------------------------------------------
# 2. Figure 2(b): Confusion Matrix for Threat Detection
# -------------------------------------------------------------
def make_fig2b():
    cm = np.array([
        [100, 0, 0, 0],
        [0, 98, 2, 0],
        [0, 2, 97, 1],
        [0, 1, 1, 98]
    ])
    labels = ['Normal Code', 'Direct Injection', 'Indirect Comment', 'Malicious Code']

    fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=300)
    cax = ax.matshow(cm, cmap='Blues', vmin=0, vmax=100)
    fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)

    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    ax.set_xticklabels(labels, fontsize=8.5, rotation=25, ha='left')
    ax.set_yticklabels(labels, fontsize=8.5)

    ax.set_xlabel('Predicted Label (Stage 0 Classifier)', fontsize=10, fontweight='bold', labelpad=10)
    ax.set_ylabel('Actual Label (Ground Truth)', fontsize=10, fontweight='bold')
    ax.set_title('Figure 2(b): Confusion Matrix for Threat Detection (400 Samples)', fontsize=11, fontweight='bold', pad=25)

    # Print numbers in cells
    for i in range(len(labels)):
        for j in range(len(labels)):
            val = cm[i, j]
            color = 'white' if val > 50 else 'black'
            ax.text(j, i, str(val), ha='center', va='center', color=color, fontweight='bold', fontsize=11)

    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "fig2b_confusion_matrix.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print("Saved:", out_path)

# -------------------------------------------------------------
# 3. Figure 3: Training Convergence & ROC Performance
# -------------------------------------------------------------
def make_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=300)

    # Subplot (a): F1-score convergence
    epochs = np.arange(1, 21)
    train_f1 = [0.18, 0.42, 0.58, 0.70, 0.78, 0.84, 0.88, 0.90, 0.92, 0.935, 0.945, 0.955, 0.962, 0.968, 0.972, 0.975, 0.978, 0.980, 0.982, 0.985]
    val_f1 =   [0.10, 0.35, 0.52, 0.64, 0.72, 0.79, 0.83, 0.86, 0.88, 0.895, 0.910, 0.925, 0.940, 0.950, 0.956, 0.960, 0.962, 0.963, 0.963, 0.963]

    ax1.plot(epochs, train_f1, 'b.-', label='Training F1', linewidth=1.8, markersize=6)
    ax1.plot(epochs, val_f1, 'rs-', label='Validation F1', linewidth=1.8, markersize=5)
    ax1.set_title('(a) F1-Score Convergence', fontsize=10, fontweight='bold')
    ax1.set_xlabel('Epochs', fontsize=9, fontweight='bold')
    ax1.set_ylabel('F1 Score', fontsize=9, fontweight='bold')
    ax1.set_ylim(0, 1.05)
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.legend(loc='lower right', fontsize=8.5)

    # Subplot (b): Threat Detection ROC Curve
    fpr = np.array([0.0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0])
    tpr = np.array([0.0, 0.88,  0.92, 0.95, 0.97, 0.98, 0.985, 0.99, 0.993, 0.996, 0.998, 1.0])

    ax2.plot(fpr, tpr, color='#15803d', linewidth=2.2, label='SafeDocGen ROC (AUC = 0.992)')
    ax2.plot([0, 1], [0, 1], color='#94a3b8', linestyle='--', linewidth=1.5, label='Random Baseline')
    ax2.set_title('(b) Threat Detection ROC Curve', fontsize=10, fontweight='bold')
    ax2.set_xlabel('False Positive Rate', fontsize=9, fontweight='bold')
    ax2.set_ylabel('True Positive Rate', fontsize=9, fontweight='bold')
    ax2.set_ylim(-0.02, 1.05)
    ax2.set_xlim(-0.02, 1.02)
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.legend(loc='lower right', fontsize=8.5)

    fig.suptitle('Figure 3: Training Convergence and Classification ROC Performance', fontsize=11, fontweight='bold', y=0.98)
    plt.tight_layout()
    out_path = os.path.join(ASSETS_DIR, "fig3_training_roc.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print("Saved:", out_path)

make_fig2a()
make_fig2b()
make_fig3()
