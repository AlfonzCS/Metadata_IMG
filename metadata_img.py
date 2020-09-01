#pip3 install Pillow
from PIL import Image
from PIL.ExifTags import TAGS
from colorama import init, Fore
import sys, random, time

init()
def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

                  
                  __  ___     __            __      __           _                
                 /  |/  /__  / /_____ _____/ /___ _/ /_____ _   (_)___ ___  ____ _
                / /|_/ / _ \/ __/ __ `/ __  / __ `/ __/ __ `/  / / __ `__ \/ __ `/
               / /  / /  __/ /_/ /_/ / /_/ / /_/ / /_/ /_/ /  / / / / / / / /_/ / 
              /_/  /_/\___/\__/\__,_/\__,_/\__,_/\__/\__,_/  /_/_/ /_/ /_/\__, /  
                                                                         /____/   

            Nota! : Scanning Port es un escaner 100% funcional, verifique con nmap.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)
ClownLogo()
#
imagen = sys.argv[1]
# path to the image or video
imagename = imagen

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")