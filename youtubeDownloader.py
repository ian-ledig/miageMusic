import os
import sys
import yt_dlp as youtube_dl

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'youtube.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            new_filename = "youtube.mp3"
            os.rename("youtube." + info_dict['ext'], new_filename)
            print("Ok")

    except Exception as e:
        print("Une erreur s'est produite lors du téléchargement :", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Veuillez spécifier l'URL de la vidéo YouTube.")
    else:
        url = sys.argv[1]
        download_video(url)
