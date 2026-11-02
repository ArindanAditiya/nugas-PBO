import tkinter as tk
from tkinter import ttk, messagebox

# ===== Palet warna konsisten (tugas 2) =====
BG      = "#eef2f7"   # background jendela
CARD    = "#ffffff"   # background form
PRIMARY = "#1e3a8a"   # biru tua judul
ACCENT  = "#2563eb"   # biru tombol simpan
DANGER  = "#dc2626"   # merah tombol keluar
NEUTRAL = "#6b7280"   # abu tombol reset
TEXT    = "#111827"   # teks utama
MUTED   = "#6b7280"   # teks sekunder
BORDER  = "#cbd5e1"   # warna garis

root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("500x620")
root.configure(bg=BG)
root.columnconfigure(0, weight=1)

# ===== Judul =====
tk.Label(
    root, text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 14, "bold"),
    bg=PRIMARY, fg="white", pady=12
).grid(row=0, column=0, sticky="ew")

# ===== Form (tugas 4: layout pakai grid) =====
form = tk.Frame(
    root, bg=CARD,
    highlightbackground=BORDER, highlightthickness=1
)
form.grid(row=1, column=0, padx=20, pady=15, sticky="ew")
form.columnconfigure(1, weight=1)

# Nama
tk.Label(form, text="Nama", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=0, column=0, sticky="w", padx=(15, 10), pady=(15, 5))
nama = tk.Entry(form, width=30, font=("Arial", 10))
nama.grid(row=0, column=1, padx=(0, 15), pady=(15, 5), sticky="ew")

# NIM
tk.Label(form, text="NIM", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=1, column=0, sticky="w", padx=(15, 10), pady=5)
nim = tk.Entry(form, width=30, font=("Arial", 10))
nim.grid(row=1, column=1, padx=(0, 15), pady=5, sticky="ew")

# Program Studi
tk.Label(form, text="Program Studi", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=2, column=0, sticky="w", padx=(15, 10), pady=5)
prodi = ttk.Combobox(
    form, values=["Informatika", "Manajemen", "Akuntansi"],
    state="readonly", width=28
)
prodi.grid(row=2, column=1, padx=(0, 15), pady=5, sticky="ew")

# Alamat (tugas 1: widget Text)
tk.Label(form, text="Alamat", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=3, column=0, sticky="nw", padx=(15, 10), pady=(5, 15))
alamat = tk.Text(form, width=30, height=4, font=("Arial", 10),
                 relief="solid", bd=1)
alamat.grid(row=3, column=1, padx=(0, 15), pady=(5, 15), sticky="ew")

# ===== Kotak hasil (dibungkus Frame) =====
hasil_box = tk.Frame(
    root, bg=CARD,
    highlightbackground=BORDER, highlightthickness=1
)
hasil_box.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")
hasil_box.columnconfigure(0, weight=1)

hasil = tk.Label(
    hasil_box,
    text="(hasil input akan tampil di sini)",
    bg=CARD, fg=MUTED,
    font=("Consolas", 10),
    justify="left", anchor="w",
    padx=12, pady=10
)
hasil.grid(row=0, column=0, sticky="ew")

# ===== Fungsi =====
def simpan():
    nama_val   = nama.get().strip()
    nim_val    = nim.get().strip()
    prodi_val  = prodi.get().strip()
    alamat_val = alamat.get("1.0", tk.END).strip()

    # Tugas 3: validasi (diperluas)
    if not nama_val:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        nama.focus_set()
        return
    if not nim_val:
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        nim.focus_set()
        return
    if not nim_val.isdigit():
        messagebox.showwarning("Peringatan", "NIM harus berupa angka!")
        nim.focus_set()
        return
    if not prodi_val:
        messagebox.showwarning("Peringatan", "Pilih program studi dulu!")
        prodi.focus_set()
        return

    hasil.config(
        text=f"Nama          : {nama_val}\n"
             f"NIM           : {nim_val}\n"
             f"Program Studi : {prodi_val}\n"
             f"Alamat        : {alamat_val if alamat_val else '-'}",
        fg=TEXT,
    )

def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="(hasil input akan tampil di sini)", fg=MUTED)
    nama.focus_set()

def keluar():
    root.destroy()

# ===== Tombol =====
tombol = tk.Frame(root, bg=BG)
tombol.grid(row=3, column=0, pady=(0, 15))

tk.Button(tombol, text="Simpan", width=10,
          bg=ACCENT, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=simpan).grid(row=0, column=0, padx=5)

tk.Button(tombol, text="Reset", width=10,
          bg=NEUTRAL, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=reset).grid(row=0, column=1, padx=5)

tk.Button(tombol, text="Keluar", width=10,
          bg=DANGER, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=keluar).grid(row=0, column=2, padx=5)

root.mainloop()