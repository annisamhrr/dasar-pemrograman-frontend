import tkinter as tk
from tkinter import ttk

# Tabel biaya berdasarkan kota
biaya_jarak = {
    ("Banyuwangi", "Banyuwangi"): 5000,
    ("Banyuwangi", "Jember"): 7500,
    ("Banyuwangi", "Probolinggo"): 10000,
    ("Banyuwangi", "Surabaya"): 15000,
    ("Jember", "Banyuwangi"): 7500,
    ("Jember", "Jember"): 5000,
    ("Jember", "Probolinggo"): 8500,
    ("Jember", "Surabaya"): 12500,
    ("Probolinggo", "Banyuwangi"): 10000,
    ("Probolinggo", "Jember"): 8500,
    ("Probolinggo", "Probolinggo"): 6000,
    ("Probolinggo", "Surabaya"): 6500,
    ("Surabaya", "Banyuwangi"): 15000,
    ("Surabaya", "Jember"): 12500,
    ("Surabaya", "Probolinggo"): 6500,
    ("Surabaya", "Surabaya"): 5000,
}

# Fungsi untuk menghitung biaya berdasarkan berat
def hitung_biaya_berat(berat):
    if berat <= 1:
        return 1500
    elif berat <= 5:
        return 2500
    elif berat <= 10:
        return 3500
    else:
        return 4500

# Fungsi untuk menghitung biaya total
def hitung_biaya():
    asal = asal_var.get()
    tujuan = tujuan_var.get()
    try:
        berat = float(berat_entry.get())
        if (asal, tujuan) in biaya_jarak:
            biaya_berat = hitung_biaya_berat(berat)
            biaya_jarak_nilai = biaya_jarak[(asal, tujuan)]
            biaya_total = biaya_berat + biaya_jarak_nilai
            hasil_var.set(f"Rp {biaya_total:,}")
        else:
            hasil_var.set("Rute tidak valid")
    except ValueError:
        hasil_var.set("Masukkan berat yang valid")

# Membuat jendela utama
root = tk.Tk()
root.title("Perhitungan Biaya Kirim Paket")

# Label dan input
tk.Label(root, text="Nomor Resi:").grid(row=0, column=0, sticky="e")
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Berat Barang (Kg):").grid(row=1, column=0, sticky="e")
berat_entry = tk.Entry(root)
berat_entry.grid(row=1, column=1)

tk.Label(root, text="Kota Asal:").grid(row=2, column=0, sticky="e")
asal_var = tk.StringVar()
asal_combo = ttk.Combobox(root, textvariable=asal_var, state="readonly")
asal_combo['values'] = ["Banyuwangi", "Jember", "Probolinggo", "Surabaya"]
asal_combo.grid(row=2, column=1)

tk.Label(root, text="Kota Tujuan:").grid(row=3, column=0, sticky="e")
tujuan_var = tk.StringVar()
tujuan_combo = ttk.Combobox(root, textvariable=tujuan_var, state="readonly")
tujuan_combo['values'] = ["Banyuwangi", "Jember", "Probolinggo", "Surabaya"]
tujuan_combo.grid(row=3, column=1)

tk.Label(root, text="Total Biaya Pengiriman:").grid(row=4, column=0, sticky="e")
hasil_var = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_var)
hasil_label.grid(row=4, column=1)

# Tombol untuk menghitung biaya
hitung_tombol = tk.Button(root, text="Hitung Biaya", command=hitung_biaya)
hitung_tombol.grid(row=5, column=0, columnspan=2)

# Mulai loop utama
root.mainloop()
