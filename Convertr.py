'''
Convertr
Colin Streck - colinstreck@gmail.com
'''
#Based on https://stackoverflow.com/a/23704144
import subprocess
import sys
import os
try:
  subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
  from PIL import Image as im
except:
  c = input("Pillow library could not be installed. Press ENTER to close program, or C and then ENTER to try to continue.")
  if(c != "C"):
    sys.exit()
mode = 0o666
path = os.path.join(os.path.expandvars("%userprofile%"), "Desktop\\Convertr\\")
try:
  os.makedirs(path)
except:
  print("Path already exists")
print("Move all files to convert into the folder on your desktop labeled 'Convertr'.")
a = input("Press ENTER once you have moved all of the desired photos in.")
print("Exporting to %s" % path)
queue = os.listdir(path)
for file in queue:
  print("Converting %s" % file)
  #Based on: https://datatofish.com/images-to-pdf-python/
  image = im.open(path + file)
  if image.mode == "RGBA":
    image = im.convert("RGB")
  pdf = image.convert('RBG')
  pdf.save(path + file.split(".")[0] + ".pdf")
print("All files converted.")
b = input("Press ENTER to close program.")
