import requests
import re
import os

images = []
url = "https://unsplash.com/"

for i in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        images.append(response.content)
    url = "https://unsplash.com/" + response.headers["X-Unsplash-Image-ID"]
folders = ["animals", "nature", "people", "places", "technology"]
for image in images:
    filename = image.filename.split("/")[-1]
    folder = folders[i % len(folders)]
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(os.path.join(folder, filename), "wb") as f:
        f.write(image)






response = requests.get("https://www.accuweather.com/ru/kz/astana/200021/weather-forecast/200021")
html_code = response.text
pattern = re.compile(r"<p class=\"phrase\">.+?</p>", re.DOTALL)
weather_string = pattern.findall(html_code)[0]
weather_elements = weather_string.split(";")
current_temperature = weather_elements[0]
print(current_temperature)