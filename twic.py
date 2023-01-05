import requests, zipfile, io
import time

START_NUM = 1313
END_NUM = 1469

for num in range(START_NUM, END_NUM + 1):
    url = f"https://theweekinchess.com/zips/twic{num}g.zip"
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    }
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == requests.codes.ok:
        zip = zipfile.ZipFile(io.BytesIO(response.content))
        zip.extractall("./Downloads/")
        print(f"{url} successfully downloaded")
    else:
        print(f"Error with {url}")
        print(f"Response code: {response.status_code}")
    time.sleep(5)
    