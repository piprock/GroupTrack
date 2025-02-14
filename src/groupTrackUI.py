import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os

from logic import Logic
from database import DataBase

class GroupTrackUI:
    def __init__(self, root, db: DataBase):
        self.db = db
        self.logic = Logic(self.db)
        
        
        # Root
        self.root = root
        self.root.title("GroupTrack")
        self.root.geometry("800x600")
        
        
        # Import settings
        try:
            is_db_found = self.logic.import_settings()
            if not is_db_found:
                messagebox.showinfo("Базу даних змінено", "Невдалося знайти базу даних з налаштувань, тому вибрана база по замовчуванню.")
        except:
            messagebox.showerror("Помилка", f"Файл налаштувань містить помилки! Буде створено новий з налаштуваннями по замовчуванню!")
            self.logic.create_default_settings()
        
        
        # Frames
        left_frame = tk.Frame(root)
        left_frame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        
        right_frame = tk.Frame(root)
        right_frame.grid(row=1, column=1, sticky="nswe", padx=10, pady=10)
        
        right_menu = tk.Frame(root)
        right_menu.grid(row=0, column=1, sticky="nswe", pady=(10,0))
        

        # Buttons
        self.import_button = tk.Button(left_frame, text="Імпортувати список присутніх", command=self.import_attendance_button)
        self.import_button.grid(row=0, pady=5)

        self.process_button = tk.Button(left_frame, text="Присвоїти групи з бази", command=self.import_groups_button)
        self.process_button.grid(row=1, pady=5)

        self.save_button = tk.Button(left_frame, text="Зберегти вихідний файл", command=self.save_output_file_button)
        self.save_button.grid(row=2, pady=5)
        root.bind("<Control-s>", lambda event: self.save_output_file_button())

        self.edit_button = tk.Button(left_frame, text="Відкрити базу даних", command=self.open_database_button)
        self.edit_button.grid(row=3, pady=5)
        
        self.edit_button = tk.Button(left_frame, text="Поміняти базу даних", command=self.change_database_button)
        self.edit_button.grid(row=4, pady=5)

        self.edit_group_button = tk.Button(right_menu, text="Редагувати групи вибрані елементи", command=self.edit_group_in_tree)
        self.edit_group_button.grid(row=0, column=0, padx=10)
        root.bind("<Return>", lambda event: self.edit_group_in_tree())

        self.edit_group_button = tk.Button(right_menu, text="Оновити базу поточними змінами", command=self.apply_changes_to_database_button)
        self.edit_group_button.grid(row=0, column=1, padx=5)

        # Labels
        self.meeting_code_label = ttk.Label(left_frame)
        self.meeting_code_label.grid(row=6, pady=5)

        self.created_on_label = ttk.Label(left_frame)
        self.created_on_label.grid(row=7, pady=5)

        # Treeview
        self.tree = ttk.Treeview(right_frame, columns=("Логін", "Група"), show="headings")
        self.tree.heading("Логін", text="Логін")
        self.tree.heading("Група", text="Група")
        self.tree.grid(sticky="nswe")

        # Setting row and column weight in Treeview
        root.grid_rowconfigure(0, weight=0)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(1, weight=1)
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        self.update_data()
        
        
        
        
        

        
    # Button commands
    def import_attendance_button(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV файли", "*.csv")])
        if file_path:
            self.logic.import_attendance(file_path)
            self.update_data()
            
    def import_groups_button(self):
        try:
            self.logic.import_groups()
            self.update_tree_data()
        except:
            self.database_error()
            
            
    def database_error(self):
        messagebox.showerror("Помилка", f"Поточна база даних містить помилки!")
        self.ask_create_empty_database()

    def save_output_file_button(self):
        default_name = f"FORMATED_meeting_{self.db.get_created_on().replace(":", "-")}"
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV файли", "*.csv")],
            initialfile=default_name
        )
        if file_path:
            self.logic.save_output_file(file_path)

    def open_database_button(self):
        file_path = self.db.get_database_file_path()
        if os.path.exists(file_path):
            os.startfile(file_path)
        else:
            self.ask_create_empty_database()
            
    def apply_changes_to_database_button(self):
        response = messagebox.askyesno(
            "Ви впевнені?",
            "Ви впевнені що хочете замінити існуючи поля бази данних вашими зміненими полями?"
        )
        if response:
            try:
                self.logic.apply_changes_to_database(self.tree)
                self.update_tree_data()
                messagebox.showinfo("Успішно", "База оновлена.")
            except:
                self.database_error()
                
    def edit_group_in_tree(self):
        selected_items = self.tree.selection()
        
        if selected_items:
            edit_window = tk.Toplevel(self.root)
            edit_window.resizable(0, 0)
            edit_window.title("Зміна групи")
            
            group_label = tk.Label(edit_window, text="Нова група")
            group_label.grid(row=0, column=0, padx=10, pady=10)
            
            group_entry = tk.Entry(edit_window)
            group_entry.grid(row=0, column=1, padx=10, pady=10)
            group_entry.focus_set()

            def save_changes():
                new_group = group_entry.get().strip()
                if not new_group:
                    new_group = self.db.NONE_GROUP
                
                user_sets = self.db.get_user_sets()

                for item in selected_items:
                    current_values = self.tree.item(item, "values")
                    user_sets[current_values[0]] = new_group

                self.db.set_user_sets(user_sets)
                self.update_tree_data()
                edit_window.destroy()

            save_button = tk.Button(edit_window, text="Save", command=save_changes)
            save_button.grid(row=1, columnspan=2, padx=10, pady=10)

            edit_window.bind("<Return>", lambda event: save_changes())
    
    
    
    
    
    
    # Other
    def change_database_button(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV файли", "*.csv")])
        if file_path:
            self.logic.change_database(file_path)
    
    def ask_create_empty_database(self):
        response = messagebox.askyesno(
            "Створення порожньої бази даних",
            "Створити порожню базу?"
        )
        if response:
            response2 = True
            if os.path.exists(self.db.DEFAULT_DATA_BASE_FILE_PATH):
                response2 = messagebox.askyesno(
                    "Створення порожньої бази даних",
                    "База по замовчуванню вже існує, ви впевнені що хочете замінити його пустою базою?"
                )
            if response2:
                self.logic.create_default_empty_database()
                messagebox.showinfo("Успішно", "База створена.")
    
    def update_data(self):
        self.update_meta_data()
        self.update_tree_data()
    
    def update_meta_data(self):
        self.meeting_code_label.config(text=f"Код зустрічі: {self.db.get_meeting_code()}")
        self.created_on_label.config(text=f"Дата створення: {self.db.get_created_on()}")

    def update_tree_data(self):
        visual_list = self.db.get_sorted_list_of_user_sets()
        self.tree.delete(*self.tree.get_children())
        for user_set in visual_list:
            self.tree.insert("", "end", values=user_set)
    
            
    

            