import pandas as pd
from database import DataBase

class Logic:
    def __init__(self, db: DataBase):
        self.db = db

    def import_attendance(self, file_path):
        self.db.set_imported_file_path(file_path)
        
        with open(file_path, "r", encoding=DataBase.DEFAULT_ENCODING) as file:
            lines = file.readlines()

        self.db.set_header_info(lines[:5])
        
        df = pd.read_csv(file_path, skiprows=4)

        user_sets = {}
        for _, row in df.iterrows():
            login = row.iloc[0]
            user_sets[login] = DataBase.NONE_GROUP
        
        self.db.set_user_sets(user_sets)
        
    def import_groups(self):
        user_sets = self.db.get_user_sets()
        
        groups_df = pd.read_csv(self.db.get_database_file_path(), encoding=DataBase.DEFAULT_ENCODING)
        groups_dict = {row['Login']: row['Group'] for _, row in groups_df.iterrows()}
        
        updated_user_sets = {}
        for login, group in user_sets.items():
            group = groups_dict.get(login, self.db.NONE_GROUP)
            updated_user_sets[login] = group
        
        self.db.set_user_sets(updated_user_sets)

    def save_output_file(self, file_path):
        df = pd.DataFrame(self.db.get_sorted_list_of_user_sets(), columns=["Login", "Group"])
        with open(file_path, "w", encoding=DataBase.DEFAULT_ENCODING) as f:
            f.write("".join(self.db.get_header_info()[:-1]))
        df.to_csv(file_path, index=False, encoding=DataBase.DEFAULT_ENCODING, mode="a")
        
    def create_empty_database(self):
        file_path = self.db.get_database_file_path()
        df = pd.DataFrame(columns=["Login", "Group"])
        df.to_csv(file_path, index=False, encoding=DataBase.DEFAULT_ENCODING)
    
    def apply_changes_to_database(self, tree):
        all_items_id = tree.get_children()
        user_sets = self.db.get_user_sets()

        for id in all_items_id:
            values = tree.item(id, "values")
            if values[1] != DataBase.NONE_GROUP:
                user_sets[values[0]] = values[1]
                
        self.db.set_user_sets(user_sets)
        df = pd.DataFrame(self.db.get_sorted_list_of_user_sets(), columns=["Login", "Group"])
        df.to_csv(self.db.get_database_file_path(), index=False, encoding=DataBase.DEFAULT_ENCODING)
        
    
        
        