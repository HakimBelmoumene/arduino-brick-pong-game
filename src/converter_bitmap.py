from PIL import Image
import numpy as np
img = Image.open("/home/sung/Documents/PlatformIO/Projects/learn_C_game/src/sung.jpg")
img=img.resize((64,64))
# data = [img.getpixel((x, y)) for x in range(img.width) for y in range(img.height)]
# da = np.reshape(data,(64,64))
# print(da)
# chkp= []
# for i in range(0,64):
#     chkp.append(",".join(da[i,:]))
# print(chkp)
# img = Image.merge("RGB", (r, g, b))
img.save("/home/sung/Documents/PlatformIO/Projects/learn_C_game/src/s.png")
# with open ("/home/sung/Documents/PlatformIO/Projects/learn_C_game/src/jinwoo.txt","w") as text:
    
#     text.write(str(data))
