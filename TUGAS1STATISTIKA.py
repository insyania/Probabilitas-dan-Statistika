import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Dataset penerbangan ke negara ASEAN dalam satu minggu
data = {"Negara Tujuan" : [
    "Singapura", "Malaysia", "Vietnam", "Filipina", "Thailand", "Brunei", "Laos"],
    "Frekuensi Penerbangan" : [5, 7, 4, 5, 6, 3, 2]}

df = pd.DataFrame(data)

pdf_path = "Tugas_1_Statistika_Insyania.pdf"

with PdfPages(pdf_path) as pdf:
     # ==================== Cover ====================
    fig1 = plt.figure(figsize=(6,4))
    plt.axis("off")
    plt.text(0.5, 0.8, "Tugas 1 Statistika", ha="center", fontsize=14, weight="bold")
    plt.text(0.1, 0.6, "Nama : Insyania Cahya Wiguna", ha="left", fontsize=12)
    plt.text(0.1, 0.5, "NIM    : 24/533789/SV/23938", ha="left", fontsize=12)
    plt.text(0.1, 0.4, "Kelas  : AA", ha="left", fontsize=12)
    plt.text(0.1, 0.3, "Mata Kuliah : Probabilitas dan Statistika", ha="left", fontsize=12)
    plt.text(0.1, 0.2, "Code : https://github.com/insyania/Probabilitas-dan-Statistika", ha="left", fontsize=8, color="blue")
    pdf.savefig(fig1)
    plt.close(fig1)

    # ==================== Tabel ====================
    fig2 = plt.figure(figsize=(6,4))
    plt.axis("off")
    plt.title("Tabel Jumlah Penerbangan ke Negara ASEAN dalam Satu Minggu", 
              fontsize=10, weight="bold")
    cell_text = [[row["Negara Tujuan"], row["Frekuensi Penerbangan"]] for _, row in df.iterrows()]
    plt.table(cellText=cell_text, colLabels=list(df.columns), loc="center", cellLoc="center")
    pdf.savefig(fig2)
    plt.close(fig2)

    # ==================== Grafik Batang ====================
    fig3 = plt.figure(figsize=(6,4))
    plt.bar(df["Negara Tujuan"], df["Frekuensi Penerbangan"], color="red")
    plt.title("Diagram Batang Jumlah Penerbangan", fontsize=10, weight="bold")
    plt.xlabel("Negara Tujuan")
    plt.ylabel("Frekuensi")
    plt.xticks(rotation=0, ha="right", fontsize=8)
    pdf.savefig(fig3)
    plt.close(fig3)

    # ==================== Grafik Garis ====================
    fig4 = plt.figure(figsize=(6,4))
    plt.plot(df["Negara Tujuan"], df["Frekuensi Penerbangan"], marker="o", color="green")
    plt.title("Diagram Garis Jumlah Penerbangan", fontsize=10, weight="bold")
    plt.xlabel("Negara Tujuan")
    plt.ylabel("Frekuensi")
    plt.xticks(rotation=0, ha="right", fontsize=8)
    pdf.savefig(fig4)
    plt.close(fig4)

    # ==================== Pie Chart ====================
    fig5 = plt.figure(figsize=(6,4))
    plt.pie(df["Frekuensi Penerbangan"], labels=df["Negara Tujuan"], autopct="%1.1f%%", startangle=90)
    plt.title("Diagram Lingkaran Persentase Penerbangan", fontsize=10, weight="bold")
    plt.axis("equal")  # biar lingkarannya bulat sempurna
    pdf.savefig(fig5)
    plt.close(fig5)





