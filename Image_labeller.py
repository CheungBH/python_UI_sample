import os
import cv2
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

folder_path = "UI_images/cat_dog"  # Specify the folder path directly
classes_list = ["cat", "dog", "pig", "cxk"]  # Add your desired classes here

class ImageClassifierGUI:
    def __init__(self, root):
        self.root = root
        self.image_files = []
        self.current_index = 0
        self.classification_results = {}
        self.classes = []

        self.create_widgets()

    def create_widgets(self):
        self.root.title("Image Classifier")

        # Create buttons frame at the top
        self.buttons_frame_top = tk.Frame(self.root)
        self.buttons_frame_top.pack(side=tk.TOP, pady=10)

        # Create back button
        self.back_button = tk.Button(self.buttons_frame_top, text="Back", command=self.previous_image)
        self.back_button.pack(side=tk.LEFT, padx=5)
        self.back_button.config(state=tk.DISABLED)

        # Create next button
        self.next_button = tk.Button(self.buttons_frame_top, text="Next", command=self.next_image)
        self.next_button.pack(side=tk.RIGHT, padx=5)

        # Create a frame to display the image
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        # Create buttons frame at the bottom
        self.buttons_frame_bottom = tk.Frame(self.root)
        self.buttons_frame_bottom.pack(pady=10)

    def load_images(self):
        self.image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if len(self.image_files) == 0:
            messagebox.showerror("Error", "No image files found in the selected folder.")
            return
        self.classes = classes_list  # Add your desired classes here

        self.class_buttons = []
        for i, class_name in enumerate(self.classes):
            button = tk.Button(self.buttons_frame_bottom, text=class_name, command=lambda x=class_name: self.label_image(x))
            button.grid(row=0, column=i, padx=5)
            self.class_buttons.append(button)

        self.display_image()

    def display_image(self):
        image_path = os.path.join(folder_path, self.image_files[self.current_index])
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize image to fit the GUI window
        max_height = 500
        max_width = 600
        image_height, image_width, _ = image.shape
        if image_height > max_height or image_width > max_width:
            scale = min(max_height / image_height, max_width / image_width)
            image = cv2.resize(image, None, fx=scale, fy=scale)

        self.photo = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        self.photo = Image.fromarray(self.photo)
        self.photo = ImageTk.PhotoImage(self.photo)

        self.image_label = tk.Label(self.image_frame, image=self.photo)
        self.image_label.pack()

        self.update_button_colors()

    def label_image(self, class_name):
        self.classification_results[self.image_files[self.current_index]] = class_name
        self.next_image()

    def next_image(self):
        self.current_index += 1
        if self.current_index < len(self.image_files):
            self.image_label.destroy()
            self.display_image()
            self.back_button.config(state=tk.NORMAL)
        else:
            self.save_results()
            messagebox.showinfo("Info", "Image labeling complete.")
            self.root.destroy()

    def previous_image(self):
        self.current_index -= 1
        self.image_label.destroy()
        self.display_image()
        if self.current_index == 0:
            self.back_button.config(state=tk.DISABLED)

    def update_button_colors(self):
        for button in self.class_buttons:
            button.configure(bg="SystemButtonFace")  # Reset button color

        current_image = self.image_files[self.current_index]
        if current_image in self.classification_results:
            class_name = self.classification_results[current_image]
            for button in self.class_buttons:
                if button["text"] == class_name:
                    button.configure(bg="green")

    def save_results(self):
        results_file = open('classification_results.txt', 'w')
        for image_file, class_name in self.classification_results.items():
            results_file.write(f'{image_file}: {class_name}\n')
        results_file.close()


root = tk.Tk()

classifier_gui = ImageClassifierGUI(root)

classifier_gui.load_images()

root.mainloop()