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


    print("Selected Files: ", filenames)

def get_metadata(image_array):
    for i in image_array:
        images = Image.open(image_array[i])

# Everything in terms of managing window below here vvvv


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    root = tk.Tk()
    image_array = []

    root.title("Raw Photo Developer - @a-little-black-cat")

    root.configure(background="white")

    root.minsize(200, 200)
    root.maxsize(1920, 1080)

    root.geometry("450x450+50+50")

    select_file_button = tk.Button(root, text="Select File(s)", command=upload_photo)
    select_file_button.pack(pady=15)


    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
