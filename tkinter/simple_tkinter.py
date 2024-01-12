import tkinter as tk
from tkinter import ttk
from tkinter import font
import cv2
import os
from PIL import Image, ImageTk

LARGE_FONT = ("Verdana", 12)
UI_path = "../UI_images/tkinter/"
geometric = (1280, 720)


def update_image(canvas, image, size):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, size)
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo


def load_image(canvas, path, size):
    image = cv2.imread(path)
    update_image(canvas, image, size)


class Demo(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("{0}x{1}".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        # self.geometry("{0}x{1}".format(geometric[0], geometric[1]))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, FontCheck):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        win_width, win_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # win_width, win_height = geometric[0], geometric[1]

        # video to be played
        canvas_video = tk.Canvas(self, width=win_width*0.55, height=win_height*0.55, bg="black")
        canvas_video.pack()
        # canvas_video.place(x=win_width*0.17, y=win_height*0.05, anchor="nw")
        canvas_video.place(relx=0.475, rely=0.35, anchor="center")
        load_image(canvas_video, os.path.join(UI_path, "processed.JPG"), size=(int(win_width * 0.55), int(win_height * 0.55)))
        tk.Label(self, text="Video", font=("Verdana", 20)).place(relx=0.475, rely=0.05, anchor="center")

        # speed map
        canvas_speed = tk.Canvas(self, width=win_width*0.19, height=win_width*0.19*0.75, bg="#137f42")
        canvas_speed.pack()
        # canvas_speed.place(x=win_width*0.825, y=win_height*0.125, anchor="center")
        canvas_speed.place(relx=0.875, rely=0.2, anchor="center")
        load_image(canvas_speed, os.path.join(UI_path, "speed_tmp.png"), size=(int(win_width * 0.19), int(win_width * 0.19*0.75)))
        tk.Label(self, text="Speed Map", font=("Verdana", 14)).place(relx=0.875, rely=0.055, anchor="center")

        # heat map
        canvas_heatmap = tk.Canvas(self, width=win_width*0.19, height=win_width*0.19*0.75, bg="#257f30")
        canvas_heatmap.pack()
        # canvas_heatmap.place(x=win_width*0.825, y=win_height*0.375, anchor="center")
        canvas_heatmap.place(relx=0.875, rely=0.5, anchor="center")
        load_image(canvas_heatmap, os.path.join(UI_path, "heatmap_tmp.png"), size=(int(win_width * 0.19), int(win_width * 0.19*0.75)))
        tk.Label(self, text="Heatmap", font=("Verdana", 14)).place(relx=0.875, rely=0.3525, anchor="center")

        # birdseyeview of field (players)
        canvas_players = tk.Canvas(self, width=win_width*0.1, height=win_width*0.1*64/36, bg="#137f42")
        canvas_players.pack()
        # canvas_players.place(x=win_width*0.675, y=win_height*0.5, anchor="nw")
        canvas_players.place(relx=0.825, rely=0.66+0.05*256/81, anchor="center")
        load_image(canvas_players, os.path.join(UI_path, "bw1.jpg"), size=(int(win_width * 0.1), int(win_width * 0.1*64/36)))
        tk.Label(self, text="Player", font=("Verdana", 14)).place(relx=0.825, rely=0.6425, anchor="center")

        # birdseyeview of field (ball)
        canvas_ball = tk.Canvas(self, width=win_width*0.1, height=win_width*0.1*64/36, bg="#257f30")
        canvas_ball.pack()
        # canvas_ball.place(x=win_width*0.835, y=win_height*0.5, anchor="nw")
        canvas_ball.place(relx=0.935, rely=(0.66+0.05*256/81), anchor="center")
        load_image(canvas_ball, os.path.join(UI_path, "bw2.jpg"), size=(int(win_width * 0.1), int(win_width * 0.1*64/36)))
        tk.Label(self, text="Ball", font=("Verdana", 14)).place(relx=0.935, rely=0.6425, anchor="center")

        # player 1 skeleton
        canvas_player1 = tk.Canvas(self, width=win_height*0.25, height=win_height*0.25, bg="#257f30")
        canvas_player1.pack()
        # canvas_player1.place(x=win_width*0.085, y=win_height*0.25, anchor="center")
        canvas_player1.place(relx=0.0925, rely=0.195, anchor="center")
        load_image(canvas_player1, os.path.join(UI_path, "3d1.png"), size=(int(win_height * 0.25), int(win_height * 0.25)))
        tk.Label(self, text="Player 1 skeleton", font=("Verdana", 14)).place(relx=0.0925, rely=0.055, anchor="center")

        # player 2 skeleton
        canvas_player2 = tk.Canvas(self, width=win_height*0.25, height=win_height*0.25, bg="#257f30")
        canvas_player2.pack()
        # canvas_player2.place(x=win_width*0.085, y=win_height*0.625, anchor="center")
        canvas_player2.place(relx=0.0925, rely=0.505, anchor="center")
        load_image(canvas_player2, os.path.join(UI_path, "3d2.png"), size=(int(win_height * 0.25), int(win_height * 0.25)))
        tk.Label(self, text="Player 2 skeleton", font=("Verdana", 14)).place(relx=0.0925, rely=0.365, anchor="center")

        button_calibrate = tk.Button(self, text="Calibrate", font=("Verdana", 30), command=self.enableStart)
        button_calibrate.pack()
        button_calibrate.place(relx=0.125, rely=0.825, anchor="center", relwidth=0.2, relheight=0.2)

        button_start = tk.Button(self, text="Start", font=("Verdana", 30), )
        button_start.pack()
        button_start.place(relx=0.375, rely=0.825, anchor="center", relwidth=0.2, relheight=0.2)

        button_report = tk.Button(self, text="Report", font=("Verdana", 30), command=lambda: controller.show_frame(PageOne))
        button_report.pack()
        button_report.place(relx=0.625, rely=0.825, anchor="center", relwidth=0.2, relheight=0.2)

        # image_button = tk.Button(self, text="Load Image", command=lambda: load_image(canvas_video, "sample/IMG_4029.JPG", size=(int(win_width*0.5), int(win_height*0.5))))
        # image_button.pack()
        # image_button.place(x=win_width*0.45, y=win_height*0.65, anchor="center",)

    def enableStart(self):
        pass


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        win_width, win_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # win_width, win_height = geometric[0], geometric[1]

        canvas1 = tk.Canvas(self, width=win_width * 0.3, height=win_width * 0.75 * 0.3, bg="white")
        canvas1.pack()
        canvas1.place(relx=0.225, rely=0.7, anchor="center")

        canvas_graph1 = tk.Canvas(self, width=win_width*0.3, height=win_width*0.75*0.3, bg="#137f42")
        canvas_graph1.pack()
        canvas_graph1.place(relx=0.225, rely=0.275, anchor="center")

        canvas_heatmap = tk.Canvas(self, width=win_width*0.3, height=win_height*0.3, bg="#257f30")
        canvas_heatmap.pack()
        canvas_heatmap.place(relx=0.8, rely=0.2, anchor="center")

        canvas_players = tk.Canvas(self, width=win_width*0.15, height=win_width*0.15*16/9, bg="#137f42")
        canvas_players.pack()
        canvas_players.place(relx=0.715, rely=0.4, anchor="nw")

        button_back = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button_back.pack()
        button_back.place(relx=0.02, rely=0.02, anchor='nw')

        image_button = tk.Button(self, text="Load Image", command=lambda: load_image(canvas1, "sample/IMG_7330.JPG",
                                                                                     size=(400, 300)))
        image_button.pack()
        image_button.place(relx=0.1, rely=0.95, anchor='center')

        button_report = tk.Button(self, text="Tmp")
        button_report.place(relx=0.2, rely=0.95, anchor='center')

        selectionVar = tk.StringVar()
        select_combobox = ttk.Combobox(self, textvariable=selectionVar)
        select_combobox['values'] = ('just', 'random', 'entries')
        select_combobox['state'] = 'readonly'
        select_combobox.place(relx=0.5, rely=0.05, anchor='center')

class FontCheck(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        win_width, win_height = self.winfo_screenwidth(), self.winfo_screenheight()
        # win_width, win_height = geometric[0], geometric[1]

        fonts = list(font.families())
        fonts.sort()

        def populate(frame):
            # Put in the fonts
            listnumber = 1
            for item in fonts:
                label = "listlabel" + str(listnumber)
                label = tk.Label(frame, text=item, font=(item, 16)).pack()
                listnumber += 1

        def onFrameConfigure(canvas):
            # Reset the scroll region to encompass the inner frame
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        frame = tk.Frame(canvas, background="#ffffff")
        vsb = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4, 4), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

        populate(frame)

app = Demo()
app.mainloop()
