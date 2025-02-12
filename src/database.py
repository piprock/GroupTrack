import os
import sys
import json
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
    
    def __init__(self):
        self._header_info = None
        self._user_sets = {}
        self._meeting_code = None
        self._created_on = None
        
        self._imported_file_path = None
        self._database_file_path = os.path.join(self.BASE_PATH, "database", "groups.csv")
        self._setting_file_path = os.path.join(self.BASE_PATH, "settings.json")
        
        self.import_setting()

    def get_sorted_list_of_user_sets(self):
        user_sets = self.get_user_sets()
        sorted_list_of_user_sets = list(user_sets.items())
        sorted_list_of_user_sets.sort(key=lambda visual_list: (visual_list[1], visual_list[0]))
        return sorted_list_of_user_sets
    
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
    
    
    def set_setting_file_path(self, setting_file_path):
        self._setting_file_path = setting_file_path
    
    def get_setting_file_path(self):
        return self._setting_file_path
    
    
    def import_setting(self):
        with open(self.get_setting_file_path(), "r", encoding=self.DEFAULT_ENCODING) as f:
            settings = json.load(f)
        self.set_database_file_path(settings["database_file_path"])
        self.set_setting_file_path(settings["setting_file_path"])
    
    def export_setting(self):
        settings = {
            "database_file_path" : self.get_database_file_path(),
            "setting_file_path" : self.get_setting_file_path(),
        }
        with open(self.get_setting_file_path(), "w", encoding=self.DEFAULT_ENCODING) as file:
            json.dump(settings, file, indent=4)
        
        
        