from PIL import Image, ImageDraw, ImageFont
import numpy as np
import argparse
# importing modules 

parser = argparse.ArgumentParser()
parser.add_argument("--inp", "-i", help="The File location of the image to be converted to ascii art, this field must be specified")
parser.add_argument("--chunk", "-c", help="[OPTIONAL] The size of the chunk, default is 10. Lower the parameter, the higher the resolution.")
parser.add_argument("--out", "-o", help="[OPTIONAL] The output path of the image default is out.png")
# adding arguments to parser 

args = parser.parse_args()
# parsing arguments 

if args.inp == None:
    raise ValueError("Image Location Not Specified")

imgLocation = str(args.inp)
chunk_size = int(args.chunk) if args.chunk != None else 10
outputLocation = str(args.out) if args.out != None else "out.png"
# getting arguments 

print(f"Opening Image at {imgLocation} with a chunk size of {chunk_size} that will be outputted to {outputLocation}")
# printing the input for confirmation 

characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# specifying characters based on the brightness 

brightnessDict = {x/len(characters):characters[x] for x in range(len(characters))}
brightnessArray = np.array(list(brightnessDict.keys()))
# creating a dictionary and numpy array of brightness values of each character 

img = Image.open(imgLocation).convert('L')
matrix = np.array(img)/255
# opening the image in lightness mode and making a numpy matrix 

chunks = matrix.reshape(matrix.shape[0]//chunk_size, chunk_size,
                        -1, chunk_size).swapaxes(1,2).reshape(-1,
                        chunk_size, chunk_size)
# converting the matrix into chunks 

newValues = chunks.mean(axis=(1,2)).reshape(int(matrix.shape[0]/chunk_size), -1)
# reshaping the matrix 

asciiImage = Image.new('RGB', img.size, (255, 255, 255))
drawer = ImageDraw.Draw(asciiImage)
font = ImageFont.truetype('arial.ttf', chunk_size)
# initializing a blank image, drawer and a font 

print("Processing started..\n")

for x in range(newValues.shape[0]):
    for y in range(newValues.shape[1]):
        # looping through the image 

        index = brightnessArray[np.abs(brightnessArray-newValues[y][x]).argmin()]
        character = brightnessDict[index]
        # getting the character to draw 

        drawer.text((x*chunk_size, y*chunk_size), character, align='left', font=font, fill=(0, 0, 0))
        # drawing the character 

    if x % 25 == 0:
        print(f"{round((x/newValues.shape[0])*100, 2)}% complete", end='\r')
        # printing progress 

print("\nProcessing end")

asciiImage.save(outputLocation)
