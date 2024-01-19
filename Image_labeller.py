import os
import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

folder_path = "UI_images/cat_dog"

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

        # Create a frame to display the image
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        # Create buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        # Create next button
        self.next_button = tk.Button(self.buttons_frame, text="Next", command=self.next_image)
        self.next_button.grid(row=0, column=0, padx=5)

    def load_images(self):
        # folder_path = filedialog.askdirectory()
        if folder_path:
            self.image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if len(self.image_files) == 0:
                messagebox.showerror("Error", "No image files found in the selected folder.")
                return
            self.classes = ["cat", "dog"]  # Add your desired classes here

            # Create class buttons
            for i, class_name in enumerate(self.classes):
                button = tk.Button(self.buttons_frame, text=class_name, command=lambda x=class_name: self.label_image(x))
                button.grid(row=0, column=i+1, padx=5)

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

        # Convert the image to Tkinter format and display it
        self.photo = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        self.photo = Image.fromarray(self.photo)
        self.photo = ImageTk.PhotoImage(self.photo)

        # Create a label widget to display the image
        self.image_label = tk.Label(self.image_frame, image=self.photo)
        self.image_label.pack()

    def label_image(self, class_name):
        self.classification_results[self.image_files[self.current_index]] = class_name
        self.next_image()

    def next_image(self):
        self.current_index += 1
        if self.current_index < len(self.image_files):
            self.image_label.destroy()
            self.display_image()
        else:
            self.save_results()
            messagebox.showinfo("Info", "Image labeling complete.")
            self.root.destroy()

    def save_results(self):
        results_file = open('classification_results.txt', 'w')
        for image_file, class_name in self.classification_results.items():
            results_file.write(f'{image_file}: {class_name}\n')
        results_file.close()


# Create the root window
root = tk.Tk()

# Create the ImageClassifierGUI instance
classifier_gui = ImageClassifierGUI(root)

# Load images when the application starts
classifier_gui.load_images()

# Run the Tkinter event loop
root.mainloop()