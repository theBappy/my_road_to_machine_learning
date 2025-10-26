import yt_dlp

def youtube_video_download(video_url):
    ydl_opts = (
        "outtmpl:" "%(title)s.%(ext)s"
    )
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        formats = info_dict.get("formats", None)

        for f in formats:
            print(f"{f['format_id']}:\t{f['ext']} ({f.get('format_note', None)}p)")

        resolution_choice = input(
            "Do you want to select from the available options? (y/n): "
        )

        if resolution_choice.lower() == "y":
            format_id = input("Enter the format id of the video: ")
            ydl_opts["format"] = format_id
        else:
            highest_resolution = max(formats, key=lambda x: x.get("height", 0))
            format_id = highest_resolution["format_id"]
            ydl_opts["format"] = format_id

        ydl.download([video_url])
        print("Download complete using yt-dlp")

if __name__ == "__main__":
    video_url = input("Enter the URL: ")
    youtube_video_download(video_url)
