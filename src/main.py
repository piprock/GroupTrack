from tkinter import Tk
from ui import GroupTrackUI
from database import DataBase

def main(): 
    db = DataBase()
    
    root = Tk()
    app = GroupTrackUI(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()