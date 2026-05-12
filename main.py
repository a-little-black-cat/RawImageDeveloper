# For window management
import tkinter as tk
from tkinter import filedialog

# For image manip.
from PIL import Image
from PIL.ExifTags import TAGS

def upload_photo():
    # can select single/multiple images, store them in an array before passing into processing
    file_paths = filedialog.askopenfilenames(title="Select photo(s) to develop...", filetypes=[("NEF",('*.NEF')),("CRV",('*.CRV')),("CR2",('*.CR2')),("ARW",('*.ARW')),("RAF",('*.RAF')),("JPEG",('*.JPEG')),("PNG",('*.PNG')),("JPG",('*.JPG')),("MPEG",('*.MPG')),])
    filenames = root.tk.splitlist(file_paths)
    for i in filenames:
        # add each individual file path to array to access
        image_array.append(i)
        print("file added to image_array: ", i)

    get_metadata(image_array)


def get_metadata(image_array):
    ## print(image_array)

    for file in image_array:
        print("Image in process: ", file)
        image = Image.open(str(file))
        ## image.show()


        exifData = image.getexif()

        print("exifData: ", str(exifData))
        print("\n ======================================= \n")

        for tagid in exifData:
            # get tag name
            tagname = TAGS.get(tagid, tagid)

            value = exifData.get(tagid)

            print(f"{tagname:25}: {value}")




# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    root = tk.Tk()
    image_array = []
    image_metadata_table = []

    root.title("Raw Photo Developer - @a-little-black-cat")

    root.configure(background="white")

    root.minsize(200, 200)
    root.maxsize(1920, 1080)

    root.geometry("450x450+50+50")

    select_file_button = tk.Button(root, text="Select File(s)", command=upload_photo)
    select_file_button.pack(pady=15)


    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
