"""Program to create simple room plans"""

import tkinter as tk
from handler.event_handler import EventHandler

class UI:
    def __init__(self, main):
        self.window = main
        self.window.title("Room Planner")

        # Divides the window into two areas(frames), one for the buttons and one for the canvas area
        self.left_frame = tk.Frame(self.window, bg="gray")
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.right_frame = tk.Frame(self.window, bg="gray")
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH,
                              padx=10, pady=10, expand=True)

        # Creates a canvas on top of the right_frame for the rectangles
        self.canvas = tk.Canvas(self.right_frame, width=800,
                                height=600, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.event_handler = EventHandler(self, self.canvas)
        self.widgets()

    def widgets(self):

        # Error label placement for width and height error
        self.error_label = tk.Label(self.left_frame, fg="red", bg="gray")
        self.error_label.pack(side=tk.TOP, padx=10, pady=10)

        # Text above the input field and input fields for the rectangle width and height and name
        self.width_label = tk.Label(self.left_frame, text="Width (cm):")
        self.width_label.pack(side=tk.TOP, padx=120, pady=5)
        self.width_entry = tk.Entry(self.left_frame)
        self.width_entry.pack(side=tk.TOP, padx=10, pady=5)
        self.height_label = tk.Label(self.left_frame, text="Height (cm):")
        self.height_label.pack(side=tk.TOP, padx=10, pady=5)
        self.height_entry = tk.Entry(self.left_frame)
        self.height_entry.pack(side=tk.TOP, padx=10, pady=5)

        # Add name to the rectangle
        self.name_label = tk.Label(self.left_frame, text="Name")
        self.name_label.pack(side=tk.TOP, padx=10, pady=5)
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.pack(side=tk.TOP, padx=10, pady=5)

        # checkbox to toggle names on/off
        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(self.left_frame,
                                       text="names on/off",
                                       variable=self.checkbox_var)
        self.checkbox.pack(side=tk.TOP, padx=10, pady=10)
        self.checkbox.config(command=self.event_handler.names_on_off)

        # Button for "create rectangle" and passes it to the create_rectangle function
        self.create_button = tk.Button(
            self.left_frame, text="Create Rectangle")
        self.create_button.pack(side=tk.TOP, padx=10, pady=10)
        self.create_button.config(command=self.event_handler.create_rectangle)

        # Button to delete rectangle (calls the delete selected function)
        self.delete_button = tk.Button(
            self.left_frame, text="Delete Rectangle")
        self.delete_button.pack(side=tk.TOP, padx=10, pady=10)
        self.delete_button.config(command=self.event_handler.delete_rectangle)

        # Save and load buttons
        self.save_button = tk.Button(self.left_frame, text="Save")
        self.save_button.pack(side=tk.RIGHT, padx=20, pady=10)
        self.save_button.config(command=self.event_handler.save_popup)

        self.load_button = tk.Button(self.left_frame, text="Load")
        self.load_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.load_button.config(command=self.event_handler.load_popup)

        # And a exit button
        self.exit_button = tk.Button(self.left_frame, text="Exit")
        self.exit_button.pack(side=tk.LEFT, padx=20, pady=30)
        self.exit_button.config(command=self.event_handler.exit_popup)

        # Binds the mouse events to the canvas
        self.canvas.bind("<ButtonPress-1>",
                         self.event_handler.click_move)  # mouse click
        # mouse drag
        self.canvas.bind("<B1-Motion>", self.event_handler.drag_move)
        self.canvas.bind("ButtonRelease-1",
                         self.event_handler.release_move)  # mouse release


root = tk.Tk()
ui = UI(root)
root.mainloop()
