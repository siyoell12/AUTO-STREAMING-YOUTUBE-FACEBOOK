import os
import time
import random
from colorama import Fore, Style, init
import threading

init(autoreset=True)

# ====================== BANNER ============================ 
banner = f"""
{Fore.RED}{Style.BRIGHT}
 █████╗ ██╗   ██╗████████╗ ██████╗     ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║
███████║██║   ██║   ██║   ██║   ██║    ███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║
██╔══██║██║   ██║   ██║   ██║   ██║    ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
"""
print(banner)
# ===========================================================

# FFmpeg path from winget installation
FFMPEG_PATH = r"C:\Users\mbulm\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"

# 1. Menu pilihan platform streaming
print(f"{Fore.GREEN}Pilih platform streaming:")
print("1. YouTube")
print("2. Facebook")
print("3. YouTube & Facebook")
choice = input(f"{Fore.YELLOW}Masukkan pilihan (1/2/3): {Fore.RESET}")

# 2. Ambil stream key sesuai pilihan
youtube_key = None
facebook_key = None

if choice == "1":
    youtube_key = input(f"{Fore.YELLOW}🔴 Masukkan YouTube Stream Key: {Fore.RESET}")
elif choice == "2":
    facebook_key = input(f"{Fore.BLUE}🔵 Masukkan Facebook Stream Key: {Fore.RESET}")
elif choice == "3":
    youtube_key = input(f"{Fore.YELLOW}🔴 Masukkan YouTube Stream Key: {Fore.RESET}")
    facebook_key = input(f"{Fore.BLUE}🔵 Masukkan Facebook Stream Key: {Fore.RESET}")
else:
    print(f"{Fore.RED}[!] Pilihan tidak valid. Program dihentikan.")
    exit()

# 3. Path ke video (bisa 1 file atau folder berisi banyak video)
video_folder = "videos"
if not os.path.exists(video_folder):
    os.makedirs(video_folder)
    print(f"{Fore.GREEN}[✓] Folder 'videos' dibuat. Silakan letakkan video di sana.")
    exit()

def get_random_video():
    files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.mkv', '.mov'))]
    return os.path.join(video_folder, random.choice(files)) if files else None

def stream(platform, stream_key, rtmp_url):
    """Stream video to specified platform using fixed ffmpeg path"""
    while True:
        video_file = get_random_video()
        if not video_file:
            print(f"{Fore.RED}[!] Tidak ada file video ditemukan di folder 'videos'.")
            break

        # Use absolute path for video file
        abs_video_file = os.path.abspath(video_file)
        if not os.path.exists(abs_video_file):
            print(f"{Fore.RED}[!] File video tidak ditemukan: {abs_video_file}")
            break

        print(f"{Fore.CYAN}[▶️] Streaming {platform} dengan video: {abs_video_file}")
        
        # Use full path to ffmpeg
        # Escape special characters in path by wrapping in double quotes and prefixing with ^ for cmd.exe
        safe_video_file = abs_video_file.replace('!', '^!')
        command = f'"{FFMPEG_PATH}" -re -stream_loop -1 -i "{safe_video_file}" -c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k -pix_fmt yuv420p -g 50 -c:a aac -b:a 160k -f flv "{rtmp_url}/{stream_key}"'
        
        print(f"{Fore.GREEN}[✓] Menjalankan: {command}")
        os.system(command)
        print(f"{Fore.YELLOW}[🔁] Mengulang video...")

# 4. RTMP endpoints
rtmp_youtube = "rtmp://a.rtmp.youtube.com/live2"
rtmp_facebook = "rtmps://live-api-s.facebook.com:443/rtmp"

# 5. Jalankan streaming sesuai pilihan
threads = []

if youtube_key:
    t_youtube = threading.Thread(target=stream, args=("YouTube", youtube_key, rtmp_youtube))
    threads.append(t_youtube)

if facebook_key:
    t_facebook = threading.Thread(target=stream, args=("Facebook", facebook_key, rtmp_facebook))
    threads.append(t_facebook)

if not threads:
    print(f"{Fore.RED}[!] Tidak ada platform streaming yang dipilih. Program dihentikan.")
    exit()

print(f"{Fore.GREEN}[✓] Memulai streaming...")
for t in threads:
    t.start()

for t in threads:
    t.join()
