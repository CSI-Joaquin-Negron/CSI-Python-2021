import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67623/pg67623.txt")
res.raise_for_status()
playFile = open("sailors.text", "wb")
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()