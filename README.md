# Formulir Identitas Mahasiswa

Aplikasi GUI sederhana berbasis **Python Tkinter** untuk menginput identitas mahasiswa (Nama, NIM, Program Studi, dan Alamat), menampilkan hasil input, serta mereset atau menutup formulir.

Dokumen ini menjelaskan **setiap potongan kode** di dalam program: **apa isinya** dan **untuk apa** dipakai.

---

## 1. Import Library

```python
import tkinter as tk
from tkinter import ttk, messagebox
```

**Untuk apa:**
- `tkinter as tk` → memanggil modul GUI utama. Alias `tk` supaya penulisan widget lebih singkat (`tk.Label`, `tk.Button`, dll).
- `ttk` → modul widget "themed" (tampilan modern). Di sini dipakai untuk **Combobox** (dropdown Program Studi).
- `messagebox` → modul popup dialog. Dipakai untuk menampilkan **peringatan validasi** (misal Nama kosong).

---

## 2. Palet Warna (Tugas 2 — Warna Konsisten)

```python
BG      = "#eef2f7"   # background jendela
CARD    = "#ffffff"   # background form
PRIMARY = "#1e3a8a"   # biru tua judul
ACCENT  = "#2563eb"   # biru tombol simpan
DANGER  = "#dc2626"   # merah tombol keluar
NEUTRAL = "#6b7280"   # abu tombol reset
TEXT    = "#111827"   # teks utama
MUTED   = "#6b7280"   # teks sekunder
BORDER  = "#cbd5e1"   # warna garis
```

**Untuk apa:**
- Menyimpan semua warna **di satu tempat** supaya konsisten di seluruh aplikasi.
- Kalau mau ganti tema, cukup ubah satu baris di sini — semua widget ikut berubah.
- Format `#RRGGBB` = kode warna hexadesimal.
- **Makna warna tombol:**
  - Biru (`ACCENT`) = aksi utama → **Simpan**
  - Abu (`NEUTRAL`) = aksi netral → **Reset**
  - Merah (`DANGER`) = aksi destruktif → **Keluar**

---

## 3. Membuat Jendela Utama

```python
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("500x620")
root.configure(bg=BG)
root.columnconfigure(0, weight=1)
```

**Untuk apa:**
- `tk.Tk()` → membuat **jendela utama** aplikasi. Semua widget nanti ditempel di sini.
- `title(...)` → mengatur **judul di title bar** jendela.
- `geometry("500x620")` → ukuran awal jendela: **500px lebar × 620px tinggi**.
- `configure(bg=BG)` → background jendela memakai warna abu terang dari palet.
- `columnconfigure(0, weight=1)` → kolom 0 diberi bobot 1 supaya widget yang ada di dalamnya **melebar mengikuti ukuran jendela**.

---

## 4. Label Judul

```python
tk.Label(
    root, text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 14, "bold"),
    bg=PRIMARY, fg="white", pady=12
).grid(row=0, column=0, sticky="ew")
```

**Untuk apa:**
- `tk.Label(...)` → widget untuk **menampilkan teks** (tidak bisa diedit user).
- `text=...` → isi teks judul.
- `font=("Arial", 14, "bold")` → font Arial ukuran 14, tebal.
- `bg=PRIMARY, fg="white"` → latar biru tua, teks putih (header kontras).
- `pady=12` → padding dalam label supaya teks tidak mepet atas-bawah.
- `.grid(row=0, column=0, sticky="ew")` → ditempatkan di **baris 0** dan **melebar penuh** (`sticky="ew"` = dari west/kiri sampai east/kanan).

---

## 5. Frame Form (Wadah Input)

```python
form = tk.Frame(
    root, bg=CARD,
    highlightbackground=BORDER, highlightthickness=1
)
form.grid(row=1, column=0, padx=20, pady=15, sticky="ew")
form.columnconfigure(1, weight=1)
```

**Untuk apa:**
- `tk.Frame(...)` → **container** kosong untuk mengelompokkan widget input → tampil seperti "kartu".
- `bg=CARD` → background putih.
- `highlightbackground=BORDER, highlightthickness=1` → memberi **garis tepi 1px** berwarna abu (efek kartu modern).
- `.grid(...)` → ditempatkan di baris 1 dengan jarak 20px kiri-kanan dan 15px atas-bawah dari jendela.
- `form.columnconfigure(1, weight=1)` → kolom ke-1 (tempat input) **melebar** saat jendela diperbesar. Kolom 0 (tempat label) lebarnya tetap.

---

## 6. Field Nama (Tugas 4 — Grid Layout)

```python
tk.Label(form, text="Nama", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=0, column=0, sticky="w", padx=(15, 10), pady=(15, 5))
nama = tk.Entry(form, width=30, font=("Arial", 10))
nama.grid(row=0, column=1, padx=(0, 15), pady=(15, 5), sticky="ew")
```

**Untuk apa:**
- `tk.Label(form, text="Nama", ...)` → label "Nama" ditempel di dalam `form`.
- `.grid(row=0, column=0, sticky="w")` → diletakkan di **baris 0 kolom 0**, rata kiri (`w` = west).
- `padx=(15, 10)` → jarak horizontal: **15px kiri, 10px kanan** (tuple dibaca "kiri, kanan").
- `pady=(15, 5)` → jarak vertikal: **15px atas, 5px bawah**.
- `tk.Entry(...)` → **kotak input satu baris** untuk Nama, lebar 30 karakter.
- `nama.grid(row=0, column=1, ...)` → diletakkan **sebaris** dengan label tapi di kolom kanan (kolom 1).
- `sticky="ew"` → Entry melebar mengisi kolom.

> **Pola ini diulang untuk semua field** (label di kolom 0, input di kolom 1) → itulah inti layout `grid()`.

---

## 7. Field NIM

```python
tk.Label(form, text="NIM", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=1, column=0, sticky="w", padx=(15, 10), pady=5)
nim = tk.Entry(form, width=30, font=("Arial", 10))
nim.grid(row=1, column=1, padx=(0, 15), pady=5, sticky="ew")
```

**Untuk apa:**
- Struktur sama dengan field Nama, hanya pindah ke **baris 1**.
- `nim` menyimpan referensi widget → nanti dipakai untuk `.get()` (ambil isi) dan `.delete()` (hapus isi).

---

## 8. Field Program Studi (Combobox)

```python
tk.Label(form, text="Program Studi", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=2, column=0, sticky="w", padx=(15, 10), pady=5)
prodi = ttk.Combobox(
    form, values=["Informatika", "Manajemen", "Akuntansi"],
    state="readonly", width=28
)
prodi.grid(row=2, column=1, padx=(0, 15), pady=5, sticky="ew")
```

**Untuk apa:**
- `ttk.Combobox(...)` → **dropdown** (kotak pilihan) untuk Program Studi.
- `values=[...]` → daftar pilihan yang muncul saat dropdown dibuka.
- `state="readonly"` → user **hanya bisa memilih** dari daftar, **tidak bisa mengetik** bebas. Ini supaya data konsisten.
- Ditempatkan di **baris 2**, sejajar dengan label.

---

## 9. Field Alamat (Tugas 1 — Widget Text)

```python
tk.Label(form, text="Alamat", bg=CARD, fg=TEXT,
         font=("Arial", 10)).grid(
    row=3, column=0, sticky="nw", padx=(15, 10), pady=(5, 15))
alamat = tk.Text(form, width=30, height=4, font=("Arial", 10),
                 relief="solid", bd=1)
alamat.grid(row=3, column=1, padx=(0, 15), pady=(5, 15), sticky="ew")
```

**Untuk apa:**
- `tk.Text(...)` → widget input **multi-baris** (bisa tekan Enter untuk baris baru). Cocok untuk **alamat** yang panjang.
- `height=4` → tinggi 4 baris teks.
- `relief="solid", bd=1` → memberi **border solid 1px** supaya mirip dengan Entry.
- Label pakai `sticky="nw"` (bukan `"w"`) → karena `Text` lebih tinggi dari label, label **nempel di atas** (north) bukan di tengah.

---

## 10. Kotak Hasil (Tugas 6 — Tampilkan Hasil di Label)

```python
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
```

**Untuk apa:**
- `hasil_box = tk.Frame(...)` → **kotak pembungkus ber-border** supaya hasil input terlihat jelas "ada di dalam kotak".
- `text="(hasil input akan tampil di sini)"` → **placeholder** awal. Kalau dibiarkan kosong (`""`), label tidak punya tinggi dan layout akan **"melompat"** begitu data muncul.
- `fg=MUTED` → teks abu-abu (karena masih placeholder, bukan hasil asli).
- `font=("Consolas", 10)` → font **monospace** supaya titik dua `:` pada hasil rata vertikal.
- `justify="left"` → teks multi-baris rata kiri.
- `anchor="w"` → isi label menempel kiri, bukan di tengah.
- `padx=12, pady=10` → padding dalam label biar teks tidak menempel ke border.

---

## 11. Fungsi `simpan()` (Tugas 3 — Validasi & Tampilkan Hasil)

```python
def simpan():
    nama_val   = nama.get().strip()
    nim_val    = nim.get().strip()
    prodi_val  = prodi.get().strip()
    alamat_val = alamat.get("1.0", tk.END).strip()
```

**Untuk apa:**
- `nama.get()` → **mengambil isi** dari widget Entry.
- `.strip()` → **membuang spasi/newline di awal & akhir**. Penting agar user yang hanya mengetik spasi dianggap kosong.
- `alamat.get("1.0", tk.END)` → khusus `Text`, cara ambil isinya pakai **indeks**:
  - `"1.0"` = baris 1, kolom 0 (awal dokumen)
  - `tk.END` = sampai akhir dokumen
  - Hasilnya selalu diakhiri `\n`, jadi `.strip()` wajib.

```python
    if not nama_val:
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        nama.focus_set()
        return
```

**Untuk apa:**
- `if not nama_val:` → bernilai **True** kalau variabel berisi string kosong.
- `messagebox.showwarning(...)` → popup peringatan ke user.
- `nama.focus_set()` → **kembalikan kursor** ke field Nama agar user bisa langsung mengisi.
- `return` → **hentikan fungsi**, kode di bawahnya tidak dijalankan.

```python
    if not nim_val:
        messagebox.showwarning("Peringatan", "NIM tidak boleh kosong!")
        nim.focus_set()
        return
```

**Untuk apa:** validasi NIM tidak boleh kosong (pola sama dengan Nama).

```python
    if not nim_val.isdigit():
        messagebox.showwarning("Peringatan", "NIM harus berupa angka!")
        nim.focus_set()
        return
```

**Untuk apa:**
- `.isdigit()` → `True` kalau **semua karakter angka**. Kalau NIM mengandung huruf → ditolak.

```python
    if not prodi_val:
        messagebox.showwarning("Peringatan", "Pilih program studi dulu!")
        prodi.focus_set()
        return
```

**Untuk apa:** Combobox `readonly` **tetap bisa kosong** kalau user belum memilih → jadi harus divalidasi.

```python
    hasil.config(
        text=f"Nama          : {nama_val}\n"
             f"NIM           : {nim_val}\n"
             f"Program Studi : {prodi_val}\n"
             f"Alamat        : {alamat_val if alamat_val else '-'}",
        fg=TEXT,
    )
```

**Untuk apa:**
- `hasil.config(text=...)` → **mengubah teks** pada label `hasil` yang sudah ada (bukan membuat label baru).
- `f"..."` → **f-string**, `{variabel}` di dalamnya otomatis diisi nilainya.
- `\n` → pindah baris.
- `alamat_val if alamat_val else '-'` → **ternary**: kalau alamat kosong, tampilkan `-` supaya tidak ada baris kosong menggantung.
- `fg=TEXT` → ubah warna teks dari abu (placeholder) ke hitam (hasil asli).

---

## 12. Fungsi `reset()` (Tugas 7 — Tombol Reset)

```python
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="(hasil input akan tampil di sini)", fg=MUTED)
    nama.focus_set()
```

**Untuk apa:**
- `nama.delete(0, tk.END)` → **hapus isi Entry** dari indeks 0 sampai akhir. Entry pakai indeks **angka**.
- `prodi.set("")` → hapus isi Combobox dengan `.set("")` (isi dengan string kosong) — **bukan** `.delete()`.
- `alamat.delete("1.0", tk.END)` → hapus isi `Text`, indeksnya **beda**: pakai `"1.0"` (baris-kolom), bukan `0`.
- `hasil.config(...)` → kembalikan label hasil ke **placeholder semula**, warna kembali ke abu.
- `nama.focus_set()` → kursor otomatis balik ke field Nama → user siap isi lagi.

---

## 13. Fungsi `keluar()` (Tugas 5 — Tombol Keluar)

```python
def keluar():
    root.destroy()
```

**Untuk apa:**
- `root.destroy()` → **menutup jendela utama** dan seluruh isinya → program **benar-benar berhenti**.
- Kenapa bukan `root.quit()`?
  - `quit()` hanya keluar dari `mainloop()` — jendela bisa **masih tampil**.
  - `destroy()` menutup jendela **dan** memberhentikan program → lebih "bersih".

---

## 14. Frame Tombol

```python
tombol = tk.Frame(root, bg=BG)
tombol.grid(row=3, column=0, pady=(0, 15))
```

**Untuk apa:**
- `tk.Frame(...)` → container untuk **3 tombol** supaya bisa disusun **sejajar horizontal**.
- `.grid(row=3, column=0, ...)` → ditempatkan di **baris 3** (paling bawah) dengan jarak 15px dari bawah jendela.

---

## 15. Tombol Simpan

```python
tk.Button(tombol, text="Simpan", width=10,
          bg=ACCENT, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=simpan).grid(row=0, column=0, padx=5)
```

**Untuk apa:**
- `tk.Button(...)` → widget tombol.
- `command=simpan` → saat diklik, panggil fungsi `simpan`. **Tanpa tanda kurung**! Kalau ditulis `simpan()`, fungsi akan langsung jalan saat tombol dibuat, bukan saat diklik.
- `bg=ACCENT, fg="white"` → background biru, teks putih (warna aksi utama).
- `relief="flat"` → hilangkan efek border 3D bawaan Tkinter → tampilan lebih modern.
- `cursor="hand2"` → kursor berubah jadi tangan saat di atas tombol (isyarat "bisa diklik").
- `.grid(row=0, column=0, padx=5)` → tombol pertama di kolom 0, jarak 5px kiri-kanan.

---

## 16. Tombol Reset

```python
tk.Button(tombol, text="Reset", width=10,
          bg=NEUTRAL, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=reset).grid(row=0, column=1, padx=5)
```

**Untuk apa:**
- Struktur sama dengan tombol Simpan.
- `command=reset` → memanggil fungsi `reset` saat diklik.
- `bg=NEUTRAL` → warna abu (netral).
- Ditempatkan di **kolom 1** (tengah).

---

## 17. Tombol Keluar

```python
tk.Button(tombol, text="Keluar", width=10,
          bg=DANGER, fg="white", font=("Arial", 10, "bold"),
          relief="flat", cursor="hand2",
          command=keluar).grid(row=0, column=2, padx=5)
```

**Untuk apa:**
- `command=keluar` → memanggil fungsi `keluar` saat diklik.
- `bg=DANGER` → warna **merah** sebagai tanda aksi destruktif (menutup aplikasi).
- Ditempatkan di **kolom 2** (kanan).

---

## 18. Menjalankan Aplikasi

```python
root.mainloop()
```

**Untuk apa:**
- `mainloop()` → **event loop** Tkinter: menjalankan jendela dan **menunggu interaksi** user (klik, ketik, dsb).
- Setiap interaksi memicu callback yang sesuai (misal klik Simpan → `simpan()` dipanggil).
- Loop berhenti ketika jendela ditutup (lewat tombol X atau `root.destroy()`).
- **Tanpa `mainloop()`**, jendela tidak akan tampil (atau muncul sekilas lalu langsung tertutup).

---
