from PIL import Image, ImageDraw
import random
import time

def create():
    try:
        width = int(input("Enter the size of graph: "))
        height = width
    except:
        print("The size of the graph must be integer - defaulting to 500x500")
        width = 500
        height = width
    img = Image.new(mode="RGB", color=(256, 256, 256), size=(width, height))
    img.save("Graph.png")
    print("\n")
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
        xcof = 0
    #try:
    #    xpow = int(input("Enter the power of x (default is 1) : "))
    #except:
    #    xpow = 1
    try:   
        c = float(input("Enter y intercept: "))
    except:
        c = ""


    if xcof == 0 and c == "":
        xpa = float(input("Enter x intercept: "))
    else:
        xpa = ""

    return xcof, c, xpa


def graphline(horiz,vert,img,xcof,c,xpa):
    start = -1 * horiz
    end = horiz*2
    colours = [[255,0,0],[0,255,0],[0,0,255]]
    colour = (random.choice(colours))

    for x in range(start,end):

        try:
            y = -((xcof *(x))+c)
        except:
            y = -((xcof *(x)))
                
        y = int(round(y,1))

        if (-1*y) > int(end/2):
            break
        
        if xcof != 0 or c != "":
            try:
                img.putpixel(((horiz+x),(vert+y)),(colour[0],colour[1],colour[2]))
                #print(x, int(-1*y))            

            except:
                if x < 0 or y < 0:
                    #print("E",x,-1*y)
                    pass
                else:
                    break

        else:
            try:
                img.putpixel(((horiz+int(xpa)),(vert+x)),(colour[0],colour[1],colour[2]))
                #print(xpa,x)

            except:
                if x < 0 or y < 0:
                    #print("E",x,-1*y)
                    pass
                else:
                    break

            
           
        
    img.save("Graph.png")


def intercepts(c,xcof,xpa):
    if c != "" and xpa == "":
        try:
            xint = "Passes through the x axis at ("+str(round((c/xcof),2)*-1)+" , 0)"
        except:
            xint = "line does not intercept x axis"
        c = "Passes through the y axis at (0 , "+str(c)+")"
       

    else:
        c = "The line does not the intercept y axis"
        xint = "Passes through the x axis at ("+str(xpa)+" , 0)"
    
    print(c)
    print(xint)


width, height, img = create()
horiz, vert, img = axisline(width,height,img)

while True:
    xcof, c, xpa = equinp()
    graphline(horiz,vert,img,xcof,c,xpa)
    intercepts(c,xcof,xpa)
    print("\n")
    adanl = input("Add another line (Y/N): ").lower()
    if adanl != "y":
        break