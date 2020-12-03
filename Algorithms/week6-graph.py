#image examples
#if PIL isn't available in your installation
#run
#pip3 install Pillow
#or
#python -m install Pillow
#from the commandline (also see book)
        
#import PIL.Image
from math import floor

def flood(fname, pixel, col = (255,0,0)):
    'flood image fname with col starting at pixel'

    image = PIL.Image.open(fname)

    height = image.height
    width = image.width
    mode = image.mode
    size = image.size    

    #print(height, width)
    newImage = PIL.Image.new(mode, size)
    #copy image
    for x in range(width):
        for y in range(height):
            colpix = image.getpixel( (x,y) )
            newImage.putpixel( (x,y), colpix)

    #flood (replace white pixels starting at pixel)
            
    to_flood = [pixel]
    visited = []
    while len(to_flood) > 0:
        (x,y) = to_flood.pop()
        visited.append((x,y))
        colpix = image.getpixel( (x,y) )
        if colpix == (255,255,255):
            newImage.putpixel( (x,y), col)
            for (dx,dy) in [(-1,0),(0,1),(1,0),(0,-1)]:
                #only left, up, right, down; no diagonal connections
                xp, yp = x+dx, y+dy
                if (xp,yp) not in visited and 0 <= xp < width and \
                   0 <= yp < height:
                    visited.append((xp, yp))
                    to_flood.append((xp, yp))
        
    newImage.save('flooded_{}_{}_{}'.format(str(pixel),str(col),fname))
def maze(G): 
    n = len(G)
    tasks = [(0,0)]
    marked = []

    while(len(tasks) > 0):
        x,y = tasks.pop()
        if (x, y) not in marked:
            marked.append((x,y))
            dist = G[x][y]
            for (xp, yp) in [(x-dist, y), (x+dist, y), (x, y+dist), (x, y-dist)]:
                if 0 <= xp < n and 0 <= yp < n:
                    tasks.append((xp, yp))
    return (n-1, n-1) in marked
    

        
maze([[3,5,7,4,6], [5,3,1,5,3], [2,8,3,1,4], [4,5,7,2,3], [3,1,3,2,0]])

