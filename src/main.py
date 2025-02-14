from tkinter import Tk
from groupTrackUI import GroupTrackUI
from database import DataBase

def main():
    db = DataBase()
    
    root = Tk()
    app = GroupTrackUI(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()