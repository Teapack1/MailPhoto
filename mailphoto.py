import os
import sys
from PIL import Image

while True:
    answer = input("Změnit velikost všech obrázků na 1024p? (y/n)")
    if answer.lower() == "y":
        break
    elif answer.lower() == "n":
        exit()
    else:
        print("y = pokračovat, n = zrušit")



files = os.listdir("./")

imlist = []
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        img = Image.open(file)
        ratio = img.width / img.height
        new_width = int(1024 * ratio)
        img = img.resize((new_width, 1024), Image.LANCZOS)
        img.save(os.path.join("./", file))

print("Všechny soubory .jpg a .png upraveny.")
