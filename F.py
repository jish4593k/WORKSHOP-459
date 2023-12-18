import tkinter as tk
from tkinter import filedialog
import torch
import torchvision.transforms as transforms
from PIL import Image, ImageTk

class ImageProcessor:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Processor")

        self.original_image_path = tk.StringVar()
        self.result_image_path = tk.StringVar()

        tk.Label(master, text="Original Image:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.original_image_path, state="readonly", width=50).grid(row=0, column=1)
        tk.Button(master, text="Select", command=self.select_image).grid(row=0, column=2)

        tk.Button(master, text="Process Image", command=self.process_image).grid(row=1, column=1)

        tk.Label(master, text="Result Image:").grid(row=2, column=0)
        tk.Entry(master, textvariable=self.result_image_path, state="readonly", width=50).grid(row=2, column=1)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.original_image_path.set(file_path)

    def process_image(self):
        if self.original_image_path.get():
            img = Image.open(self.original_image_path.get())

            
            img_tensor = transforms.ToTensor()(img)
            img_tensor = torch.mul(img_tensor, 255).byte()  # Convert to byte tensor

           
            processed_tensor = 255 - img_tensor

            
            processed_image = transforms.ToPILImage()(processed_tensor)

            result_path = self.original_image_path.get().rsplit('.', 1)[0] + '_result.jpg'
            processed_image.save(result_path)
            self.result_image_path.set(result_path)
        else:
            tk.messagebox.showerror("Error", "Please select an image.")

if __name__ == "__main__":
    root = tk.Tk()
    processor = ImageProcessor(root)
    root.mainloop()
