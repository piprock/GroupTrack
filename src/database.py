import os
import sys
from pathlib import Path

class DataBase:
    NONE_STRING = "---"
    NONE_GROUP = "Unknown"
    NONE_DATE_AND_TIME = "0000-00-00 00:00:00"
    NONE_CODE = "xxx-xxx-xxx"
    
    if getattr(sys, 'frozen', False):
        # Running in a PyInstaller bundle
        RUNNING_FILE = sys.executable
    else:
        # Running in a normal Python process
        RUNNING_FILE = __file__
        
    BASE_PATH = Path(RUNNING_FILE).parent
    DEFAULT_ENCODING = "utf-8-sig"
    DEFAULT_DATA_BASE_FILE_PATH = os.path.join(BASE_PATH, "database", "groups.csv")
    SETTINGS_PATH = os.path.join(BASE_PATH, "settings.json")
    
    def __init__(self):
        self._header_info = None
        self._user_sets = {}
        self._meeting_code = None
        self._created_on = None
        
        self._imported_file_path = None
        self._database_file_path = None

    def get_sorted_list_of_user_sets(self):
        user_sets = self.get_user_sets()
        return self.get_sorted_list_of_dict(user_sets)
    
    def get_sorted_list_of_dict(self, your_dict):
        sorted_list_of_dict = list(your_dict.items())
        sorted_list_of_dict.sort(key=lambda values: (values[1], values[0]))
        return sorted_list_of_dict
    
    def get_imported_file_path(self):
        return self._imported_file_path
    
    def set_imported_file_path(self, imported_file_path):
        self._imported_file_path = imported_file_path


    def set_header_info(self, header_info):
        self._header_info = header_info

    def get_header_info(self):
        return self._header_info


    def set_user_sets(self, user_sets):
        self._user_sets = user_sets
    
    def get_user_sets(self):
        return self._user_sets


    def get_meeting_code(self):
        if self._header_info is not None:
            return self._header_info[1].replace("Meeting code: ", "").lstrip("*").strip()
        return self.NONE_CODE
        
    def get_created_on(self):
        if self._header_info is not None:
            return self._header_info[2].replace("Created on ", "").lstrip("*").strip()
        return self.NONE_DATE_AND_TIME
    
    
    def set_database_file_path(self, database_file_path):
        self._database_file_path = database_file_path
        
    def get_database_file_path(self):
        return self._database_file_path
    
    
    