# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 16:13:37 2025

@author: Paul
"""
import os

def rename_file(old_file_path, new_file_name):
    """
        old_file_path (str): The current path to the file.
        new_file_name (str): The new name for the file (without the directory path).
        bool: True if the rename was successful, False otherwise.
    """
    directory = os.path.dirname(old_file_path)
    new_file_path = os.path.join(directory, new_file_name)

    try:
        os.rename(old_file_path, new_file_path)
        print(f"File successfully renamed to: {new_file_path}")
        return True
    except FileNotFoundError:
        print(f"Error: File not found at {old_file_path}")
        return False
    except FileExistsError:
        print(f"Error: A file with the name '{new_file_name}' already exists in the directory.")
        return False
    except Exception as e:
        print(f"An error occurred while renaming the file: {e}")
        return False

if __name__ == "__main__":
    directory = 'C:/Users/Paul/Nexford' # Store the directory path
    old_file = "netflix_data.csv"
    new_name = "Netflix_Shows_Movies.csv"

    old_file_path = os.path.join(directory, old_file) # Full path to old file
    new_file_path = os.path.join(directory, new_name) # Full path to new file

    rename_success = rename_file(old_file_path, new_name)

    if rename_success:
        print("File renaming process completed.")
