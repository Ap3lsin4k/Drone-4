from PIL import Image

width=3024
length=4032
result=Image.new('RGB', (3*length, 3*width))
with open("coordinates.txt") as f:
    for string in f.readlines():
        print("loop")
        array = string.split()
        name = array[0]
        lat = int(array[1])
        long = int(array[2])
        print("before open an image")
        image1 = Image.open(name)
        print("Pasting...")
        result.paste(im=image1, box=(long*length,lat*width))
print("Saving")
result.save("result.JPG")
print("The end")
"""
for i in range(1,4,1):
    image1 = Image.open(str(i)+"1.jpg")
    image2 = Image.open(str(i)+"2.jpg")
    image3 = Image.open(str(i)+"3.jpg")
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    (width3, height3) = image3.size

    
    result_width = width1+width2+width3
    result_height = max(height1,height2,height3)

    result=Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0,0))
    #result.paste(im=image2, box=(width2,0))
    result.paste(im=image3, box=(width2+width3,0))
    result.save("result"+str(i)+".jpg")
image11 = Image.open("result1.jpg")
image22 = Image.open("result2.jpg")
image33 = Image.open("result3.jpg")
(width11, height11) = image11.size
(width22, height22) = image22.size
(width33, height33) = image33.size

    
result_width1 = max(width11,width22,width33)
result_height1 = height11+height22+height33

result1=Image.new('RGB', (result_width1, result_height1))
result1.paste(im=image11, box=(0,0))
result1.paste(im=image22, box=(0,height22))
result1.paste(im=image33, box=(0,height22+height33))
result1.save("resultall.jpg")
"""

#result.show()

