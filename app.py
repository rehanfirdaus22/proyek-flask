# app.py
# Tugas: integrasi template Start Bootstrap "Freelancer" ke dalam Flask
# Komponen Flask yang dipakai: Flask(), route, render_template, url_for,
# request, redirect, flash, abort, errorhandler, context_processor

from flask import (
    Flask, render_template, request, redirect, url_for, flash, abort
)

app = Flask(__name__)
app.secret_key = "ganti-dengan-kunci-rahasia-kamu"  # dibutuhkan oleh flash()

# ---------- Data (bisa kamu ganti sesuai identitasmu) ----------
PROFIL = {
    "nama": "Rehan",
    "peran": "Mahasiswa - Semester 3",
    "lokasi": "Surabaya, Jawa Timur",
    "tahun": 2026,
}

PROYEK = [
    {"id": 1, "judul": "Pondok Kayu", "gambar": "cabin.png",
     "deskripsi": "Contoh proyek desain landing page untuk penyewaan pondok wisata."},
    {"id": 2, "judul": "Toko Kue", "gambar": "cake.png",
     "deskripsi": "Contoh proyek katalog produk untuk toko kue rumahan."},
    {"id": 3, "judul": "Sirkus", "gambar": "circus.png",
     "deskripsi": "Contoh proyek halaman jadwal pertunjukan dan pemesanan tiket."},
    {"id": 4, "judul": "Game Arcade", "gambar": "game.png",
     "deskripsi": "Contoh proyek website komunitas pecinta game."},
    {"id": 5, "judul": "Brankas", "gambar": "safe.png",
     "deskripsi": "Contoh proyek halaman informasi layanan penyimpanan dokumen."},
    {"id": 6, "judul": "Kapal Selam", "gambar": "submarine.png",
     "deskripsi": "Contoh proyek website edukasi tentang dunia bawah laut."},
]


# Variabel `profil` otomatis tersedia di semua template
@app.context_processor
def kirim_profil():
    return {"profil": PROFIL}


# ---------- Route ----------

@app.route("/")
def index():
    return render_template("index.html", proyek=PROYEK)


@app.route("/tentang")
def tentang():
    return render_template("about.html")


# Route dinamis: <int:proyek_id> menangkap angka dari URL
@app.route("/proyek/<int:proyek_id>")
def detail_proyek(proyek_id):
    for item in PROYEK:
        if item["id"] == proyek_id:
            return render_template("project.html", item=item)
    abort(404)


# Route dengan dua method: GET menampilkan form, POST memproses isinya
@app.route("/kontak", methods=["GET", "POST"])
def kontak():
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        email = request.form.get("email", "").strip()
        pesan = request.form.get("pesan", "").strip()

        if not nama or not email or not pesan:
            flash("Semua kolom wajib diisi.", "danger")
        elif "@" not in email:
            flash("Format email tidak valid.", "danger")
        else:
            print(f"[PESAN MASUK] {nama} <{email}>: {pesan}")  # tampil di terminal
            flash(f"Terima kasih, {nama}! Pesanmu sudah diterima.", "success")
            return redirect(url_for("kontak"))  # cegah kirim ulang saat refresh

    return render_template("contact.html")


# Halaman khusus untuk error 404
@app.errorhandler(404)
def halaman_tidak_ditemukan(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
