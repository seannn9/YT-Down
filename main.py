from pytube import YouTube

link = input("Video Link: ")
yt = YouTube(link)
print(yt.title)
resol = input("Resolution: ")
print(yt.streams.filter(file_extension="mp4", resolution=resol)) 
itag = input("Itag: ")
stream = yt.streams.get_by_itag(itag)
stream.download()
