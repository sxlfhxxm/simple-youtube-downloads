import yt_dlp
# yt-dlp 2023.10.13  


def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': '%(title)s'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        video_title = info_dict.get('title', None)
        if video_title:
            print(f"Downloading: {video_title}")
            ydl.download([link])
            print(f"Successfully Downloaded: {video_title}")
        else:
            print("Couldn't fetch video title.")

link = 'your link'
download_audio(link)
