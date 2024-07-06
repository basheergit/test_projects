from pytube import YouTube

def download_youtube_video(url):
    # Create a YouTube object
    yt = YouTube(url)
    
    # Get the highest resolution stream
    stream = yt.streams.get_highest_resolution()
    
    # Download the video
    stream.download()
    
    print(f"Video downloaded successfully: {yt.title}")

# Example usage
url = "https://www.youtube.com/watch?v=Wb2Tp35dZ-I&list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy&index=7"  # Replace with your video URL
download_youtube_video(url)