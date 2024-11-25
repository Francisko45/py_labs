import requests
from PIL import Image 
import io

gif_url = "https://drive.google.com/uc?export=download&id=1JUasGm9IwScxYTgft5TH0oHjuyRIIvZE"  


response = requests.get(gif_url)

if response.status_code == 200:
    image = Image.open(io.BytesIO(response.content))
    width, height = image.size
    with open("validate.txt", "w") as f:
        f.write(f"Ширина: {width}\n")
        f.write(f"Висота: {height}\n")

    print(f"Інформація записана в файл validate.txt: Ширина = {width}, Висота = {height}")
else:
    print("Не вдалося завантажити файл.")
