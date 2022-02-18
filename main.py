from youtubesearchpython import VideosSearch

song = VideosSearch("infinity ink - infinity", limit = 1)
link = song.result().get("result")[0].get("link")
print(link)