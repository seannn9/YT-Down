from pytube import YouTube

down_path = "/Users/seanulric/Downloads"
link = input("Video Link: ")
yt = YouTube(link)
print(yt.title)
highest = int(input("Highest res or itag (1 or 2): "))
if highest == 1:
    stream = yt.streams.get_highest_resolution()
    stream.download(down_path)
else:
    resol = input("Resolution: ")
    print(yt.streams.filter(file_extension="mp4", res=resol)) 
    itag = input("Itag: ")
    stream = yt.streams.get_by_itag(itag)
    stream.download(down_path)