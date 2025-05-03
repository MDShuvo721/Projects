import pytubefix as pytube
import sys
from pathlib import Path
import re

# This Function removes invalid chars from the yt title
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

if len(sys.argv) < 2:
    print("Usage: python script.py <YouTube_URL>")
    sys.exit(1)

url = sys.argv[1]

yt = pytube.YouTube(url)

path = Path("D:/YouTube")

# if yt.length <= 600:
#     stream = yt.streams.filter(res="1080p", progressive=True, file_extension="mp4").first()
#     print("Video is short, selecting 1080p resolution.")
# else:
#     stream = yt.streams.filter(res="720p", progressive=True, file_extension="mp4").first()
#     print("Video is long, selecting 720p resolution.")

# # If 1080p or 720p aren't available, select the highest resolution available
# if not stream:
#     stream = yt.streams.get_highest_resolution()

# # Sanitize the filename to ensure it's valid
# filename = sanitize_filename(f"{yt.title}.mp4")

# stream.download(output_path=path, filename=filename)

audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

audio_stream.download(output_path=path)

print(f"{yt.title} has downloaded to {path}")