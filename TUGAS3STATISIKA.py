import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statistics import mode
from matplotlib.backends.backend_pdf import PdfPages

data = {"Negara Tujuan" : [
    "Singapura", "Malaysia", "Vietnam", "Filipina", "Thailand", "Brunei", "Laos"],
    "Frekuensi Penerbangan Selama Dua Minggu" : [13, 9, 13, 12, 9, 8, 3],
    "Jumlah Penumpang Selama Dua Minggu" : [334, 350, 276, 208, 183, 105, 88]}

df = pd.DataFrame(data)

mean_freq = df["Frekuensi Penerbangan Selama Dua Minggu"].mean()
median_freq = df["Frekuensi Penerbangan Selama Dua Minggu"].median()
mode_freq = mode(df["Frekuensi Penerbangan Selama Dua Minggu"])
var_freq = df["Frekuensi Penerbangan Selama Dua Minggu"].var()
std_freq = df["Frekuensi Penerbangan Selama Dua Minggu"].std()

mean_pass = df["Jumlah Penumpang Selama Dua Minggu"].mean()
median_pass = df["Jumlah Penumpang Selama Dua Minggu"].median()
mode_pass = mode(df["Jumlah Penumpang Selama Dua Minggu"])
var_pass = df["Jumlah Penumpang Selama Dua Minggu"].var()
std_pass = df["Jumlah Penumpang Selama Dua Minggu"].std()

pdf_path = "Tugas_3_Statistika_Insyania.pdf"
with PdfPages(pdf_path) as pdf:
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

    fig2 = plt.figure(figsize=(8,5))
    plt.boxplot(
    [df["Frekuensi Penerbangan Selama Dua Minggu"], 
     df["Jumlah Penumpang Selama Dua Minggu"]],
    vert=False,  
    patch_artist=True,
    tick_labels=["Frekuensi Penerbangan", "Jumlah Penumpang"],
    boxprops=dict(facecolor="#ADD8E6", color="black", ),
    medianprops=dict(color="red"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black"),
    flierprops=dict(markerfacecolor="orange", marker="o", markersize=5, linestyle="none"))
    plt.title("Boxplot Frekuensi & Jumlah Penumpang Selama Dua Minggu")
    pdf.savefig(fig2)
    plt.close(fig2)

print(f"PDF berhasil dibuat: {pdf_path}")