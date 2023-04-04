import tkinter as ttk
from tkinter import *

"""
Program to create simple room plans
"""

class UI:
    def __init__(self):
        self._window = Tk()
        self._window.title("Room Planner")

        # Divides the window into two areas(frames), one for the buttons and one for the canvas area
        self.left_frame = ttk.Frame(self._window, bg="gray")
        self.left_frame.pack(side=LEFT, padx=10, pady=10)
        self.right_frame = ttk.Frame(self._window, bg="gray")
        self.right_frame.pack(side=LEFT, fill=BOTH, padx=10, pady=10, expand=True)
        
        # Creates a vanvas on top of the right_frame for the rectangles
        self.canvas = Canvas(self.right_frame, width=800, height=600, bg="white")
        self.canvas.pack(side=TOP, fill=BOTH,expand=True)

        # Error label placement for width and height error
        self.error_label = Label(self.left_frame, fg="red", bg="gray")
        self.error_label.pack(side=TOP, padx=10, pady=10)

        # Text above the input field and input fields for the rectangle width and height (and name)
        self.width_label = Label(self.left_frame, text="Width (cm):")
        self.width_label.pack(side=TOP, padx=120, pady=5)
        self.width_entry = Entry(self.left_frame)
        self.width_entry.pack(side=TOP, padx=10, pady=5)
        self.height_label = Label(self.left_frame, text="Height (cm):")
        self.height_label.pack(side=TOP, padx=10, pady=5)
        self.height_entry = Entry(self.left_frame)
        self.height_entry.pack(side=TOP, padx=10, pady=5)

        #This doesnt yet add the name to the rectangle
        self.name_label = Label(self.left_frame, text="Name")
        self.name_label.pack(side=TOP, padx=10, pady=5)
        self.name_entry = Entry(self.left_frame)
        self.name_entry.pack(side=TOP, padx=10, pady=5)
        
        # Button for "create rectangle" and passes it to the create_rectangle function(will be changed to "create room" and "create furniture" buttons)
        self.square_button = Button(self.left_frame, text="Create Rectangle")
        self.square_button.pack(side=TOP, padx=10, pady=10)
        self.square_button.config(command=self.create_rectangle)

        # Button to delete rectangle (calls the delete selected function)
        self.square_button = Button(self.left_frame, text="Delete Rectangle")
        self.square_button.pack(side=TOP, padx=10, pady=10)
        self.square_button.config(command=self.delete_rectangle)

        # And a exit button
        self.square_button = Button(self.left_frame, text="Exit")
        self.square_button.pack(side=TOP, padx=10, pady=50)
        self.square_button.config(command=self.exit)

        # List to keep track of the rectangles (will later be used with a save function)
        self.rectangles = []

        # Binds the mouse events to the canvas
        self.canvas.bind("<ButtonPress-1>", self.click_move) # mouse click
        self.canvas.bind("<B1-Motion>", self.drag_move)           # mouse drag
        self.canvas.bind("ButtonRelease-1", self.release_move) # mouse release
 
        # Variables to keep track of the selected rectangle and the offset between the mouse and the rectangle
        self.selected_rectangle = None
        self.offset_x = 0
        self.offset_y = 0

    # Find the clicked rectangle
    def click_move(self, event):
        clicked_rectangle = None
        overlapping_rectangles = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        if overlapping_rectangles:
            clicked_rectangle = overlapping_rectangles[-1] # Get the topmost rectangle if rectangles overlap
            
        # If a rectangle is clicked make it the selected rectangle and calculate the offset between the mouse and the rectangle
        if clicked_rectangle:
            self.selected_rectangle = clicked_rectangle
            self.offset_x = event.x - self.canvas.coords(clicked_rectangle)[0]   # event.x and event.y tracks the mouse position
            self.offset_y = event.y - self.canvas.coords(clicked_rectangle)[1]  

    # Move the selected rectangle with the mouse
    def drag_move(self, event):  
        if self.selected_rectangle:
            x1, y1, x2, y2 = self.canvas.coords(self.selected_rectangle)
            new_x1 = event.x - self.offset_x   # event.x and event.y tracks the mouse position
            new_y1 = event.y - self.offset_y
            new_x2 = new_x1 + (x2 - x1)
            new_y2 = new_y1 + (y2 - y1)
            self.canvas.coords(self.selected_rectangle, new_x1, new_y1, new_x2, new_y2) # Changes the coordinates for the rectangle

    # Deselect the rectangle when the mouse is released
    def release_move(self, event):
        self.selected_rectangle = None

    # Creates a rectangle from the inputs
    def create_rectangle(self):
        # checks that the width and height inputs are integers
        try:
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())

            # Calls the Rectangle class and appends the rectangle to the list
            rectangle = Rectangle(width, height)
            self.rectangles.append(rectangle)
            self.canvas.create_rectangle(50, 50, rectangle.width+50, rectangle.height+50, fill="white")
            self.error_label.config(text="", bg="gray")
      
        except ValueError:
            self.error_label.config(text="Width and height must be a number!", bg="lightgray")

    # Deletes the last selected rectangle
    def delete_rectangle(self):
        self.canvas.delete(self.selected_rectangle)
    
    
    def exit(self):
        self._window.quit()


#Rectangle class to store info of the rectangle (coordinates will be stored here, also will differentiate between a "Room" rectangle and "Furniture rectangle)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
      
ui = UI()
ui._window.mainloop()
