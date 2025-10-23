from PIL import Image
import matplotlib.pyplot as plt
import glob
import os

image_list = []
for file_name in glob.glob("images/*.jpeg"): #assuming gif
    img = Image.open(file_name)
    image_list.append(img)
    plt.imshow(img)

    water_mark = Image.open("result_img.png")
    size = (500, 50)
    crop_image = water_mark
    crop_image.thumbnail(size)

    copied_image = img.copy()
    copied_image.paste(crop_image, (20, 20))

    if not os.path.exists("output"):
        os.makedirs("output")

    copied_image.save("output/" + os.path.basename("result_img" + file_name))

print(image_list)

