from PIL import Image

width=3024
length=4032
result=Image.new('RGB', (3*length, 3*width))
with open("coordinates.txt") as f:
    for string in f.readlines():
        array = string.split()
        name = array[0]
        lat = int(array[1])
        long = int(array[2])
        try:
            image = Image.open(name)        
            result.paste(im=image, box=(long*length,lat*width))
        except FileNotFoundError: # if file can not be opened show message
            print("FileNotFoundError: [Errno 2] No such file: '11.JPG'")
            print("Не знайдено файл з таким іменем: '11.JPG'")

result.save("result.JPG")
