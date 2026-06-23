import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

data = {
    "Negara": ["Singapura", "Malaysia", "Vietnam", "Filipina", "Thailand", "Brunei", "Laos"],
    "Frekuensi": [13, 9, 13, 12, 9, 8, 3]
}
df = pd.DataFrame(data)
df["Probabilitas"] = df["Frekuensi"] / df["Frekuensi"].sum()

mean = df["Frekuensi"].mean()
var = df["Frekuensi"].var()
std = df["Frekuensi"].std()

A = df[df["Frekuensi"] >= 10]
p_A = A["Frekuensi"].sum() / df["Frekuensi"].sum()
bayes_result = {}
for negara, f in zip(A["Negara"], A["Frekuensi"]):
    p_si = f / df["Frekuensi"].sum()
    bayes_result[negara] = p_si / p_A

pdf_path = "Tugas_5_Statistika_Insyania.pdf"
with PdfPages(pdf_path) as pdf:
    # -------- Cover --------
    fig1 = plt.figure(figsize=(6,4))
    plt.axis("off")
    plt.text(0.5, 0.8, "Tugas 5 Statistika", ha="center", fontsize=14, weight="bold")
    plt.text(0.1, 0.6, "Nama : Insyania Cahya Wiguna", ha="left", fontsize=12)
    plt.text(0.1, 0.5, "NIM    : 24/533789/SV/23938", ha="left", fontsize=12)
    plt.text(0.1, 0.4, "Kelas  : AA", ha="left", fontsize=12)
    plt.text(0.1, 0.3, "Mata Kuliah : Probabilitas dan Statistika", ha="left", fontsize=12)
    plt.text(0.1, 0.2, "Code : https://github.com/insyania/Probabilitas-dan-Statistika", ha="left", fontsize=8, color="blue")
    pdf.savefig(fig1)
    plt.close(fig1)

    fig2 = plt.figure(figsize=(7,5))
    plt.axis("off")
    plt.title("Peluang Tiap Negara", fontsize=14, weight="bold")
    ypos = 0.8
    for negara, prob in zip(df["Negara"], df["Probabilitas"]):
        plt.text(0.1, ypos, f"P({negara}) = {prob:.3f}", fontsize=12, ha="left")
        ypos -= 0.08
    pdf.savefig(fig2)
    plt.close(fig2)

    fig3 = plt.figure(figsize=(7,5))
    plt.axis("off")
    plt.title("Perhitungan Bayes Rule (P(Si|A))", fontsize=14, weight="bold")
    ypos = 0.8
    for negara, val in bayes_result.items():
        plt.text(0.1, ypos, f"P({negara}|A) = {val:.3f}", fontsize=12, ha="left")
        ypos -= 0.1
    pdf.savefig(fig3)
    plt.close(fig3)

    fig4 = plt.figure(figsize=(7,5))
    plt.axis("off")
    plt.title("Statistik Data", fontsize=14, weight="bold")
    plt.text(0.1, 0.8, f"Mean              = {mean:.2f}", fontsize=12, ha="left")
    plt.text(0.1, 0.7, f"Variance          = {var:.2f}", fontsize=12, ha="left")
    plt.text(0.1, 0.6, f"Standard Deviation = {std:.2f}", fontsize=12, ha="left")
    pdf.savefig(fig4)
    plt.close(fig4)

    fig5 = plt.figure(figsize=(8,5))
    plt.bar(df["Negara"], df["Probabilitas"], color="skyblue", edgecolor="black")
    plt.title("Probability Histogram Frekuensi Penerbangan")
    plt.xlabel("Negara Tujuan")
    plt.ylabel("Probabilitas")
    pdf.savefig(fig5)
    plt.close(fig5)

    fig6 = plt.figure(figsize=(8,5))
    plt.axis("off")
    plt.title("Analisis Histogram Probabilitas", fontsize=14, weight="bold")

    analysis_text = (
    "1. Negara dengan peluang tertinggi adalah Singapura dan Vietnam,\n"
    "   artinya penerbangan ke dua negara ini paling sering terjadi.\n\n"
    "2. Laos memiliki peluang paling kecil sehingga penerbangan ke sana jarang.\n\n"
    "3. Distribusi tidak merata (skewed), karena ada negara yang dominan\n"
    "   sementara beberapa negara lain jarang.\n\n"
    "4. Mean peluang mendekati 0.14, namun ada deviasi yang cukup besar\n"
    "   sehingga sebaran peluang antar negara cukup lebar.\n\n"
    "5. Kesimpulan: terdapat beberapa negara hub utama penerbangan,\n"
    "   sedangkan negara lain berperan lebih kecil."
)
    plt.text(0.05, 0.9, analysis_text, ha="left", va="top", fontsize=11)
    pdf.savefig(fig6)
    plt.close(fig6)


print(f"PDF berhasil dibuat: {pdf_path}")
