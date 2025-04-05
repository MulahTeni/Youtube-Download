import os
from yt_dlp import YoutubeDL

def download_videos(input_file, output_dir):
    # TXT dosyasından video URL'lerini oku
    with open(input_file, 'r') as file:
        video_urls = [line.strip() for line in file if line.strip()]

    # İndirilecek dizin
    os.makedirs(output_dir, exist_ok=True)  # Dizin oluşturulur (varsa hata vermez)

    # YouTube-DLP ayarları
    ydl_opts = {
        'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best',  # 480p video ve en iyi ses formatı
        'hls_prefer_ffmpeg': True,  # HLS indirme için ffmpeg kullan
        'outtmpl': os.path.join(output_dir, 'vid_%(id)s.%(ext)s'),  # Çıktı dosyası ismi
        'verbose': True,  # Ayrıntılı çıktı göster
    }

    # İndirme işlemi
    with YoutubeDL(ydl_opts) as ydl:
        for video_url in video_urls:
            print(f"İndiriliyor: {video_url}")
            try:
                ydl.download([video_url])
            except Exception as e:
                print(f"Hata oluştu: {e}")

    print("Tüm videolar indirildi!")
