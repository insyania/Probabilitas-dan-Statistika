import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from matplotlib.backends.backend_pdf import PdfPages

# Dataset penerbangan ke negara ASEAN dalam satu minggu
data = {"Negara Tujuan" : [
    "Singapura", "Malaysia", "Vietnam", "Filipina", "Thailand", "Brunei", "Laos"],
    "Frekuensi Penerbangan Minggu ke-1" : [5, 7, 4, 5, 6, 3, 2],
    "Frekuensi Penerbangan Minggu ke-2" : [8, 2, 9, 7, 3, 5, 1],
    "Jumlah Penumpang Selama Dua Minggu" : [334, 350, 276, 208, 183, 105, 88],
    "Ekonomi" : [214, 180, 240, 188, 125, 90, 80],
    "Bisnis" : [67, 55, 26, 13, 30, 10, 8],
    "First Class" : [33, 15, 10, 7, 28, 5, 0]}

df = pd.DataFrame(data)

pdf_path = "Tugas_2_Statistika_Insyania.pdf"

with PdfPages(pdf_path) as pdf:
     # ==================== Cover ====================
    fig1 = plt.figure(figsize=(6,4))
    plt.axis("off")
    plt.text(0.5, 0.8, "Tugas 2 Statistika", ha="center", fontsize=14, weight="bold")
    plt.text(0.1, 0.6, "Nama : Insyania Cahya Wiguna", ha="left", fontsize=12)
    plt.text(0.1, 0.5, "NIM    : 24/533789/SV/23938", ha="left", fontsize=12)
    plt.text(0.1, 0.4, "Kelas  : AA", ha="left", fontsize=12)
    plt.text(0.1, 0.3, "Mata Kuliah : Probabilitas dan Statistika", ha="left", fontsize=12)
    plt.text(0.1, 0.2, "Code : https://github.com/insyania/Probabilitas-dan-Statistika", ha="left", fontsize=8, color="blue")
    pdf.savefig(fig1)
    plt.close(fig1)

   # ==================== 1. Side-by-Side Horizontal Bars ====================
    fig2, ax = plt.subplots(figsize=(7,5))
    y = np.arange(len(df))
    ax.barh(y-0.2, df["Frekuensi Penerbangan Minggu ke-1"], height=0.4, label="Minggu 1")
    ax.barh(y+0.2, df["Frekuensi Penerbangan Minggu ke-2"], height=0.4, label="Minggu 2")
    ax.set_yticks(y)
    ax.set_yticklabels(df["Negara Tujuan"])
    ax.set_xlabel("Frekuensi Penerbangan")
    ax.set_title("Side-by-Side Horizontal Bars")
    ax.legend()
    pdf.savefig(fig2)
    plt.close(fig2)

    # ==================== 2. Radar / Spider Chart ====================
    categories = list(df["Negara Tujuan"])
    values1 = df["Frekuensi Penerbangan Minggu ke-1"].tolist()
    values2 = df["Frekuensi Penerbangan Minggu ke-2"].tolist()
    N = len(categories)
    angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    values1 += values1[:1]
    values2 += values2[:1]
    angles += angles[:1]

    fig3 = plt.figure(figsize=(6,6))
    ax = plt.subplot(111, polar=True)
    ax.plot(angles, values1, label="Minggu 1")
    ax.fill(angles, values1, alpha=0.25)
    ax.plot(angles, values2, label="Minggu 2")
    ax.fill(angles, values2, alpha=0.25)
    ax.set_thetagrids(np.degrees(angles[:-1]), categories)
    ax.set_title("Radar / Spider Chart")
    ax.legend(loc='lower right', bbox_to_anchor=(1.15, 1))
    pdf.savefig(fig3)
    plt.close(fig3)

    # ==================== 3. Stacked Horizontal Bars ====================
    fig4, ax = plt.subplots(figsize=(7,5))
    ax.barh(df["Negara Tujuan"], df["Ekonomi"], label="Ekonomi")
    ax.barh(df["Negara Tujuan"], df["Bisnis"], left=df["Ekonomi"], label="Bisnis")
    ax.barh(df["Negara Tujuan"],
            df["First Class"],
            left=df["Ekonomi"]+df["Bisnis"],
            label="First Class")
    ax.set_xlabel("Jumlah Penumpang")
    ax.set_title("Stacked Horizontal Bars (Kelas Penumpang)")
    ax.legend()
    pdf.savefig(fig4)
    plt.close(fig4)

        # ==================== 4. 100% Stacked Horizontal Bars ====================
    total = df[["Ekonomi","Bisnis","First Class"]].sum(axis=1)
    ekonomi_pct = df["Ekonomi"] / total
    bisnis_pct = df["Bisnis"] / total
    first_pct = df["First Class"] / total

    fig5, ax = plt.subplots(figsize=(7,5))
    ax.barh(df["Negara Tujuan"], ekonomi_pct, label="Ekonomi")
    ax.barh(df["Negara Tujuan"], bisnis_pct, left=ekonomi_pct, label="Bisnis")
    ax.barh(df["Negara Tujuan"], first_pct, left=ekonomi_pct+bisnis_pct, label="First Class")
    ax.set_xlim(0,1)
    ax.set_xlabel("Proporsi (%)")
    ax.set_title("100% Stacked (Likert-style) Horizontal Bars")
    ax.legend()
    pdf.savefig(fig5)
    plt.close(fig5)

    # ==================== 5. Word Cloud ====================
    word_freq = {negara: frek for negara, frek in zip(df["Negara Tujuan"], df["Jumlah Penumpang Selama Dua Minggu"])}
    # ganti path font sesuai OS kamu
    font_path = "C:/Windows/Fonts/arial.ttf"
    wc = WordCloud(width=800, height=400, background_color="white", font_path=font_path)
    wc.generate_from_frequencies(word_freq)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    plt.title("Word Cloud Negara Tujuan")
    pdf.savefig(fig)
    plt.close(fig)

        # ==================== 6. Dumbbell Chart ====================
    fig7, ax = plt.subplots(figsize=(7,5))
    for i, negara in enumerate(df["Negara Tujuan"]):
        x1 = df.loc[i, "Frekuensi Penerbangan Minggu ke-1"]
        x2 = df.loc[i, "Frekuensi Penerbangan Minggu ke-2"]
        ax.plot([x1, x2], [i, i], 'k-', lw=1)
        ax.plot(x1, i, 'o', color="blue", label="Minggu 1" if i==0 else "")
        ax.plot(x2, i, 'o', color="red", label="Minggu 2" if i==0 else "")
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df["Negara Tujuan"])
    ax.set_xlabel("Frekuensi Penerbangan")
    ax.set_title("Dumbbell Chart (Before–After)")
    ax.legend()
    pdf.savefig(fig7)
    plt.close(fig7)

print(f"PDF berhasil dibuat: {pdf_path}")