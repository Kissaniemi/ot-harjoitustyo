import tkinter as tk
from ui.ui_view import View


def main():
    window = tk.Tk()
    window.title("Room Planner")

    ui_view = View(window)
    ui_view.initialize()
    window.mainloop()


if __name__ == '__main__':
    main()
