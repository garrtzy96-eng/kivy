"""
database.py
-----------
Modul database SQLite untuk aplikasi "Pentol Mama Reta".

Menangani 3 hal:
1. Akun pengguna (daftar / login)
2. Data menu (produk pentol)
3. Riwayat pesanan

File database (pentol.db) akan otomatis dibuat di folder yang sama
dengan file ini saat aplikasi pertama kali dijalankan.
"""

import sqlite3
import hashlib
import os

DB_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pentol.db")


def get_connection():
    """Membuka koneksi baru ke database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # supaya hasil query bisa diakses seperti dict
    return conn


def hash_password(password: str) -> str:
    """Mengenkripsi password sebelum disimpan (jangan simpan password polos)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def init_db():
    """Membuat semua tabel jika belum ada, lalu mengisi menu awal jika tabel produk kosong."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            harga INTEGER NOT NULL,
            deskripsi TEXT,
            gambar TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS riwayat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            kode_transaksi TEXT,
            detail_item TEXT,
            total_harga INTEGER,
            tanggal TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)

    conn.commit()

    # Isi menu awal hanya jika tabel produk masih kosong (baru pertama kali run)
    cur.execute("SELECT COUNT(*) FROM produk")
    jumlah_produk = cur.fetchone()[0]
    if jumlah_produk == 0:
        produk_awal = [
            ("Pentol Paket 1", 10000, "Satu porsi bakso lumer lengkap dengan siraman sambal pedas.", "tugas2.jpeg"),
            ("Pentol Paket 2", 15000, "Bakso isi keju premium satuan, tambah ekstra lumer.", "tugas.jpeg"),
        ]
        cur.executemany(
            "INSERT INTO produk (nama, harga, deskripsi, gambar) VALUES (?, ?, ?, ?)",
            produk_awal,
        )
        conn.commit()

    conn.close()


# =========================================================
# USER: DAFTAR (REGISTER) & MASUK (LOGIN)
# =========================================================

def daftar_user(nama: str, email: str, password: str):
    """
    Mendaftarkan akun baru.
    Return (True, pesan_sukses) jika berhasil, (False, pesan_error) jika gagal.
    """
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (nama, email, password) VALUES (?, ?, ?)",
            (nama, email.lower().strip(), hash_password(password)),
        )
        conn.commit()
        return True, "Pendaftaran berhasil! Silakan masuk."
    except sqlite3.IntegrityError:
        return False, "Email sudah terdaftar, gunakan email lain."
    finally:
        conn.close()


def login_user(email: str, password: str):
    """
    Mengecek email & password.
    Return dict data user jika cocok, None jika salah/tidak ditemukan.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email.lower().strip(),))
    row = cur.fetchone()
    conn.close()

    if row and row["password"] == hash_password(password):
        return dict(row)
    return None


# =========================================================
# PRODUK (MENU)
# =========================================================

def get_all_produk():
    """Mengambil semua menu, diurutkan dari yang paling lama ditambahkan."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produk ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def tambah_produk(nama, harga, deskripsi, gambar="tugas2.jpeg"):
    """Menambahkan menu baru ke database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO produk (nama, harga, deskripsi, gambar) VALUES (?, ?, ?, ?)",
        (nama, harga, deskripsi, gambar),
    )
    conn.commit()
    conn.close()


def hapus_produk(produk_id):
    """Menghapus menu berdasarkan id-nya."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM produk WHERE id = ?", (produk_id,))
    conn.commit()
    conn.close()


# =========================================================
# RIWAYAT PESANAN
# =========================================================

def tambah_riwayat(user_id, kode_transaksi, detail_item, total_harga, tanggal):
    """Menyimpan satu transaksi/pesanan baru."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO riwayat (user_id, kode_transaksi, detail_item, total_harga, tanggal)
           VALUES (?, ?, ?, ?, ?)""",
        (user_id, kode_transaksi, detail_item, total_harga, tanggal),
    )
    conn.commit()
    conn.close()


def get_riwayat_by_user(user_id):
    """Mengambil semua riwayat pesanan milik satu user, terbaru di atas."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM riwayat WHERE user_id = ? ORDER BY id DESC",
        (user_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]
