import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from statistics import mode
from matplotlib.backends.backend_pdf import PdfPages

data = {"Negara Tujuan" : [
    "Singapura", "Malaysia", "Vietnam", "Filipina", "Thailand", "Brunei", "Laos"],
    "Frekuensi Penerbangan Selama Dua Minggu" : [13, 9, 13, 12, 9, 8, 3],
    "Jumlah Penumpang Selama Dua Minggu" : [334, 350, 276, 208, 183, 105, 88]}

df = pd.DataFrame(data)

x = df["Frekuensi Penerbangan Selama Dua Minggu"]
y = df["Jumlah Penumpang Selama Dua Minggu"]

mean_x, mean_y = np.mean(x), np.mean(y)

r_num = np.sum((x - mean_x) * (y - mean_y))
r_den = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
r_manual = r_num / r_den

b_manual = np.sum((x - mean_x)*(y - mean_y)) / np.sum((x - mean_x)**2)
a_manual = mean_y - b_manual*mean_x

pdf_path = "Tugas_4_Statistika_Insyania.pdf"

r_scipy, _ = stats.pearsonr(x, y)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

with PdfPages(pdf_path) as pdf:
     # ==================== Cover ====================
    fig1 = plt.figure(figsize=(6,4))
    plt.axis("off")
    plt.text(0.5, 0.8, "Tugas 4 Statistika", ha="center", fontsize=14, weight="bold")
    plt.text(0.1, 0.6, "Nama : Insyania Cahya Wiguna", ha="left", fontsize=12)
    plt.text(0.1, 0.5, "NIM    : 24/533789/SV/23938", ha="left", fontsize=12)
    plt.text(0.1, 0.4, "Kelas  : AA", ha="left", fontsize=12)
    plt.text(0.1, 0.3, "Mata Kuliah : Probabilitas dan Statistika", ha="left", fontsize=12)
    plt.text(0.1, 0.2, "Code : https://github.com/insyania/Probabilitas-dan-Statistika", ha="left", fontsize=8, color="blue")
    pdf.savefig(fig1)
    plt.close(fig1)

    fig2 = plt.figure(figsize=(7,5))
    plt.axis("off")
    plt.title("Hasil Perhitungan Regresi Linier", fontsize=14, weight="bold")
    y_start = 5 
    line_spacing = 0.5
    plt.text(0.1, 0.8, f"Koefisien Korelasi manual (r): {r_manual:.4f}", fontsize=12, ha="left")
    plt.text(0.1, 0.75, f"Koefisien Korelasi scipy (r): {r_scipy:.4f}", fontsize=12, ha="left")
    plt.text(0.1, 0.70, f"Persamaan Regresi: Y = {intercept:.2f} + {slope:.2f}X", fontsize=12, ha="left")
    plt.text(0.1, 0.65, f"Intercept (a): {intercept:.2f}", fontsize=12, ha="left")
    plt.text(0.1, 0.60, f"Slope (b): {slope:.2f}", fontsize=12, ha="left")
    pdf.savefig(fig2)
    plt.close(fig2)

    fig3 = plt.figure(figsize=(8,5))
    plt.scatter(x, y, color="hotpink", label="Data Asli")
    plt.plot(x, intercept + slope*x, color="red", label=f"Regresi: Y = {intercept:.2f} + {slope:.2f}X")
    plt.title("Regresi Linier Frekuensi vs Jumlah Penumpang")
    plt.xlabel("Frekuensi Penerbangan Selama Dua Minggu")
    plt.ylabel("Jumlah Penumpang Selama Dua Minggu")
    plt.legend()
    plt.grid(True)
    pdf.savefig(fig3)  
    plt.close(fig3)

print(f"PDF berhasil dibuat: {pdf_path}")