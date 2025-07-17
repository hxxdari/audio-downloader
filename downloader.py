
import yt_dlp
import os

def download_audio(url, audio_format="mp3"):
    output_template = f"downloads/audio.%(ext)s"
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        file_path = output_template.replace("%(ext)s", audio_format)
        return file_path
    except Exception as e:
        print("Error:", e)
        return None
