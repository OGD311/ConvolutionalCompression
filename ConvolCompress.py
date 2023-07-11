#Image Compressor
from PIL import Image, ImageDraw
import time
#How much compression?

try:
    print("Compression value is default at 1/9 (9 original pixels compressed to 1)")
    print("Compression is calculated by the sequence 4n^2 -4n + 1")
    compVal = int(input("How much compression (Enter 1 for default): ")) 

except:
    compVal = 1

numPix = (4*((compVal+1)**2))-(4*(compVal+1))+1
print(f"Compression set to {numPix} pixels compressed to 1 (1/{numPix})")


#Initialise
file = "Original.png"
orig = Image.open(file)
orig.convert(mode="RGB")
compr = Image.new(mode="RGB", color=(256, 256, 256), size=(orig.width-1, orig.height-1))
newFile = file.replace(".png","")+" Compressed"
#print(newFile)
compr.save(f"{newFile}.png")

#functions
def avglist(list):
    total = 0
    for i in range(len(list)):
        total += int(list[i])

    avg = (total/len(list))
    return int(avg)



#Check each pixel
dred = []
dgreen = []
dblue = []

start = time.time()
for x in range(0,orig.width-1):
    for y in range(0,orig.height-1):
        try:
            for h in range(x-compVal,x+compVal):
                for w in range(y-compVal,y+compVal):
                    data = orig.getpixel((h,w))
                    dred.append(data[0])
                    dgreen.append(data[1])
                    dblue.append(data[2])
        except:
            pass
        
        compr.putpixel((x,y),(avglist(dred),avglist(dgreen),avglist(dblue)))
        dred, dgreen, dblue = [],[],[]

       




#Save
compr.save(f"{newFile}.png")
end = time.time()
timeTaken = str(end-start)
print(f"Image compressed by 1/{numPix} times in {(timeTaken[0:timeTaken.index('.')+2])} seconds")