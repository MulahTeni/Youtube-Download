from src.yt_dlp_downloader import download_videos

if __name__ == "__main__":
    input_file = "video_urls.txt"
    output_dir = "./vids/downloaded"
    
    try:
        download_videos(input_file, output_dir)
    except FileNotFoundError:
        print(f"Hata: {input_file} dosyası bulunamadı. Lütfen doğru bir dosya yolu belirtin.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
