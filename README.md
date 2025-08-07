# Auto Streamer

Auto Streamer adalah skrip Python untuk melakukan streaming video secara otomatis ke platform YouTube dan/atau Facebook menggunakan FFmpeg.

## Fitur
- Streaming video secara looping tanpa henti
- Mendukung streaming ke YouTube, Facebook, atau keduanya sekaligus
- Menggunakan FFmpeg dengan path absolut untuk menghindari masalah PATH
- Validasi file video dan path agar streaming berjalan lancar

## Persyaratan
- Python 3.x
- FFmpeg terinstal (direkomendasikan menggunakan skrip `install_ffmpeg.ps1` untuk instalasi di Windows)
- Folder `videos` berisi file video dengan format `.mp4`, `.mkv`, atau `.mov`

## Cara Instalasi FFmpeg dan Menjalankan Streaming
1. Jalankan skrip PowerShell `install_ffmpeg.ps1` untuk menginstal FFmpeg via winget (Windows 10/11):
   ```powershell
   .\install_ffmpeg.ps1
   ```
2. Tambahkan FFmpeg ke PATH sistem menggunakan `add_ffmpeg_path.ps1` atau `fix_ffmpeg_path.bat`:
   ```powershell
   .\add_ffmpeg_path.ps1
   ```
   atau jalankan batch file:
   ```cmd
   fix_ffmpeg_path.bat
   ```
3. Verifikasi instalasi dengan menjalankan:
   ```bash
   python cek_ffmpeg.py
   ```
4. Pastikan folder `videos` berisi video yang ingin di-streaming
5. Jalankan skrip streaming:
   ```bash
   python live_streamer_fixed.py
   ```
3. Pilih platform streaming:
   - Masukkan `1` untuk YouTube
   - Masukkan `2` untuk Facebook
   - Masukkan `3` untuk YouTube & Facebook sekaligus
4. Masukkan stream key yang valid untuk platform yang dipilih
5. Streaming akan berjalan otomatis dan video akan diulang terus menerus

## Catatan
- Pastikan stream key dan URL RTMP sudah benar dan aktif
- Jika ada masalah dengan path video atau FFmpeg, pastikan path sudah benar dan file video ada di folder `videos`
- Skrip sudah menangani karakter khusus dan spasi pada nama file video

## Struktur Proyek
- `live_streamer_fixed.py`: Skrip utama untuk streaming video dengan path FFmpeg absolut dan validasi path
- `install_ffmpeg.ps1`: Skrip PowerShell untuk instalasi FFmpeg via winget
- `add_ffmpeg_path.ps1` / `fix_ffmpeg_path.bat`: Skrip untuk menambahkan FFmpeg ke PATH sistem
- `cek_ffmpeg.py`: Skrip untuk memeriksa instalasi FFmpeg
- `videos/`: Folder tempat meletakkan file video untuk streaming

## Lisensi
MIT License

---

Jika Anda membutuhkan bantuan lebih lanjut, silakan hubungi.
