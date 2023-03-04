import pytube
#from pytube import YouTube
link = input("enter the URL to download:\t")
video_link = pytube.YouTube(link)
#you = YouTube('https://youtu.be/9bZkp7q19f0').streams.get_highest_resolution()
print(video_link)
high_video = video_link.streams.get_highest_resolution()
#print(video_link.streams.filter(progressive=True))
high_video.download("C:\\Vidhun\\Personal\\video")
print("Download completed")