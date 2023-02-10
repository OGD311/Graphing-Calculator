from PIL import Image, ImageDraw
import random
import time

def create():
    width = 1000
    height = 1000
    img = Image.new(mode="RGB", color=(256, 256, 256), size=(width, height))
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), (255,255,255))
    
    img.save("Graph.png")
    return width,height,img


def axisline(width,height,img):
    horiz = height // 2
    for i in range(0,width):
        img.putpixel((i,horiz),(0,0,0))

    vert = width // 2
    for i in range(0,height):
        img.putpixel((vert,i),(0,0,0))

    img.save("Graph.png")
    return horiz, vert, img

def equinp():
    try:
        xcof = float(input("Enter coefficient of x: "))
    except:
        xcof = 1
    #try:
    #    xpow = int(input("Enter the power of x (default is 1) : "))
    #except:
    #    xpow = 1
    try:   
        c = float(input("Enter y intercept: "))
    except:
        c = 0

    return xcof, c


def graphline(horiz,vert,img,xcof,c):
    start = -1 * horiz
    end = horiz
    colours = [[255,0,0],[0,255,0],[0,0,255]]
    colour = (random.choice(colours))

    for x in range(start,(end//(int(round(xcof,0))))+15):
        y = -((xcof *(x))+c)
        y = int(round(y,1))
        try:
            img.putpixel((horiz+x,vert+y),(colour[0],colour[1],colour[2]))
           # print(x, int(vert+y))

        except:
            if x < 0 or y < 0:
              #  print("E",x,y)
                pass
            else:
                break

    img.save("Graph.png")



    yint = c
    xint = (round((c/xcof),2))
    print("Passes through the y axis at (0 , "+str(yint)+")")
    print("Passes through the x axis at ("+str(xint)+" , 0)")


width, height, img = create()
horiz, vert, img = axisline(width,height,img)

while True:
    xcof, c = equinp()
    graphline(horiz,vert,img,xcof,c)
    adanl = input("Add another line (Y/N): ").lower()
    if adanl != "y":
        break