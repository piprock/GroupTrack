import os

class DataBase:
    NONE_STRING = "---"
    NONE_GROUP = "Unknown"
    NONE_DATE_AND_TIME = "0000-00-00 00:00:00"
    NONE_CODE = "xxx-xxx-xxx"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_FILE_NAME = "groups.csv"
    DATABASE_FILE_PATH = os.path.join(BASE_DIR, "database", DATABASE_FILE_NAME)
    DEFAULT_ENCODING = "utf-8-sig"
    
    def __init__(self):
        self._header_info = None
        self._user_sets = {}
        self._meeting_code = None
        self._created_on = None
        
        self._imported_file_path = None

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
    
    
    