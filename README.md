# Auto Streamer

Auto Streamer adalah skrip Python untuk melakukan streaming video secara otomatis ke platform YouTube/Facebook menggunakan FFmpeg.

---

## 🚀 Fitur Utama
- Streaming video secara looping tanpa henti
- Mendukung streaming ke YouTube, Facebook, atau keduanya sekaligus
- Menggunakan FFmpeg dengan path absolut untuk menghindari masalah PATH
- Validasi file video dan path agar streaming berjalan lancar
- Penanganan karakter khusus dan spasi pada nama file video

---

## 🛠️ Persyaratan Sistem
- Python 3.x
- FFmpeg terinstal (direkomendasikan menggunakan skrip `install_ffmpeg.ps1` untuk instalasi di Windows)
- Folder `videos` berisi file video dengan format `.mp4`, `.mkv`, atau `.mov`

---

## ⚙️ Cara Instalasi FFmpeg dan Menjalankan Streaming

### 1. Instalasi FFmpeg
Jalankan skrip PowerShell berikut untuk menginstal FFmpeg via winget (Windows 10/11):
```powershell
.\install_ffmpeg.ps1
```

### 2. Tambahkan FFmpeg ke PATH Sistem
Tambahkan FFmpeg ke PATH menggunakan salah satu metode berikut:
- Jalankan skrip PowerShell:
```powershell
.\add_ffmpeg_path.ps1
```
- Atau jalankan batch file:
```cmd
fix_ffmpeg_path.bat
```

### 3. Verifikasi Instalasi FFmpeg
Pastikan FFmpeg sudah terinstal dengan benar:
```bash
python cek_ffmpeg.py
```

### 4. Siapkan Folder Video
Pastikan folder `videos` berisi file video yang ingin Anda streaming.

### 5. Jalankan Skrip Streaming
Mulai streaming dengan menjalankan:
```bash
python live_streamer_fixed.py
```

### 6. Pilih Platform Streaming
- Masukkan `1` untuk YouTube
- Masukkan `2` untuk Facebook
- Masukkan `3` untuk YouTube & Facebook sekaligus

### 7. Masukkan Stream Key
Masukkan stream key yang valid untuk platform yang dipilih.

### 8. Streaming Otomatis
Streaming akan berjalan otomatis dan video akan diulang terus menerus.

---

## ⚠️ Catatan Penting
- Pastikan stream key dan URL RTMP sudah benar dan aktif.
- Jika ada masalah dengan path video atau FFmpeg, pastikan path sudah benar dan file video ada di folder `videos`.
- Skrip sudah menangani karakter khusus dan spasi pada nama file video.

---

## 📁 Struktur Proyek
Berikut adalah struktur isi folder proyek ini agar tidak membingungkan:

```
c:/AUTO-STREAM/
├── add_ffmpeg_path.ps1          # Skrip PowerShell untuk menambahkan FFmpeg ke PATH
├── cek_ffmpeg.py               # Skrip untuk memeriksa instalasi FFmpeg
├── fix_ffmpeg_path.bat         # Batch file untuk menambahkan FFmpeg ke PATH
├── install_ffmpeg.ps1          # Skrip PowerShell untuk instalasi FFmpeg via winget
├── live_streamer_fixed.py      # Skrip utama untuk streaming video dengan path FFmpeg absolut dan validasi path
├── live_streamer_menu.py       # Skrip menu streaming (opsional)
├── live_streamer.py            # Skrip streaming asli (opsional)
├── ffmpeg_path_fix.py          # Skrip bantu untuk verifikasi path FFmpeg (opsional)
└── videos/                     # Folder tempat meletakkan file video untuk streaming
    └── *.mp4, *.mkv, *.mov     # File video yang didukung
```

- `live_streamer_fixed.py` adalah skrip utama yang direkomendasikan untuk digunakan.
- Folder `videos` harus berisi file video yang ingin Anda streaming.

Berikut adalah struktur isi folder proyek ini agar tidak membingungkan:


🌐 Komunitas & Sosial Media
Ingin berdiskusi, bertanya, atau berbagi ide? Bergabunglah dengan komunitas kami!

💬 Telegram Group: [t.me/ytshortuploader](https://t.me/independendropers)

🐦 Twitter/X: [twitter.com/ytshortbot](https://x.com/Deasaputra_12)

🎮 Discord Server: [discord.gg/ytshortuploader](https://discord.gg/Tuy2bR6CkU)
## Buy Me a Coffee

- **EVM:** 0x905d0505Ec007C9aDb5CF005535bfcC5E43c0B66
- **TON:** UQCFO7vVP0N8_K4JUCfqlK6tsofOF4KEhpahEEdXBMQ-MVQL
- **SOL:** BmqfjRHAKXUSKATuhbjPZfcNciN3J2DA1tqMgw9aGMdj

Thank you for visiting this repository, don't forget to contribute in the form of follows and stars.
If you have questions, find an issue, or have suggestions for improvement, feel free to contact me or open an *issue* in this GitHub repository.

**deasaputra**
