import pytube

def Download(link):
    video_obj = pytube.YouTube(link)
    video_obj = video_obj.streams.get_highest_resolution()
    try:
        video_obj.download("C:\\Vidhun\\Personal\\video")
    except:
        print("An error has occurred")
    print("Title: ", video_obj.title)
    print("Downloading.........")
    print("Download is completed successfully")
    inp = str.lower((input("Do you want to downlaod again?: ")))
    if (inp == "yes"):
       url = input("enter the url: ")
       Download(url)


link = input("Enter the YouTube video URL: ")
Download(link)