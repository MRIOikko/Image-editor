import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps

class ImageEditor:
    def __init__(self, root): 
        self.root = root
        self.root.title("Image Editor")
        self.image = None
        self.photo = None
        self.canvas = tk.Canvas(root, width=800, height=600, bg='black')
        self.canvas.pack()
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Grayscale", command=self.convert_grayscale)
        edit_menu.add_command(label="Rotate 90°", command=self.rotate_image)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def save_image(self):   
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.image.save(file_path)
            else:
                messagebox.showerror("Error", "No file specified.")
        else: 
            messagebox.showerror("Error", "No image to save.")
    def convert_grayscale(self):
        if self.image:
            self.image = ImageOps.grayscale(self.image)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            messagebox.showerror("Error", "No image loaded.")
    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            messagebox.showerror("Error", "No image loaded.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = ImageEditor(root)
    root.mainloop() 
