from PIL import Image, ImageDraw
import random

width = 200
height = 200
img = Image.new(mode="RGB", color=(256, 256, 256), size=(width, height))

img.save("Image.png")

#background
for y in range(height):
    for x in range(width):

        img.putpixel((x, y), (255,255,255))
  
img.save("Image.png")

#axis lines
horiz = height // 2
for i in range(0,width):
    img.putpixel((i,horiz),(0,0,0))

vert = width // 2
for i in range(0,height):
    img.putpixel((vert,i),(0,0,0))

img.save("Image.png")


#equation input:

try:
    xcof = int(input("Enter coefficient of x: "))
except:
    xcof = 1
#try:
#    xpow = int(input("Enter the power of x (default is 1) : "))
#except:
#    xpow = 1
try:   
    c = int(input("Enter y intercept: "))
except:
    c = 0


#graphing line
start = -1 * horiz
end = horiz

for x in range(start,(end//xcof)+1):
    y = -((xcof *(x))+c)

    try:
        img.putpixel((horiz+x,vert+y),(255,0,0))
        #print(x, y)
    except:
        if x < 0 or y < 0:
            pass
        else:
            break

img.save("Image.png")

x = start
while True:
    x += 1
    if -((xcof *(x))+c) == 0:
        break
print("Passes through the y axis at 0",c)
print("Passes through the x axis at",x,"0")