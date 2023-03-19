#!/usr/bin/env python
# coding: utf-8



import os





class analyze_txt():
    
    def __init__(self,folder_path):
        
        """
        Initialize the analyze_txt class with a folder path.
        
        Parameters:
        folder_path (str): The path to the folder containing the txt files.
        
        """
        self.folder_path = folder_path
        
    def get_empty_txts(self):
        
        """
        Returns a list of empty .txt files in the folder.
        
        """
        
        empty_txts = []
        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name) # create full path to file like path/filename.txt
            if os.path.isfile(file_path) and file_name.endswith(".txt") and os.stat(file_path).st_size == 0:
                empty_txts.append(file_name)
            
        return empty_txts
                        
                    
    def delete_empty(self):
        
        """
        Deletes empty .txt files from the folder.
        """   
        empty_txt = self.get_empty_txts()    
            
        for file_name in empty_txts:
            file_path = os.path.join(self.folder_path, file_name)
            os.remove(file_path)
                
        print(f"{len(empty_txts)} empty .txt files deleted.")
        

