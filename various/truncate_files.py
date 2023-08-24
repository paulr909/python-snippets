import os
import re

# remove random file id from file name
# https://www.youtube.com/watch?v=7xGdu3ySXj0

file_path = "/home/paul/Videos/various/"
extensions = (".mp4", ".webm", ".mkv")

for file_name in os.listdir(file_path):
    base_name, extension = os.path.splitext(file_name)

    if extension in extensions:
        try:
            new_file_name = re.sub(r"-[A-Za-z0-9_-]{11}", "", file_name)
        except ValueError:
            print(f"File {file_name} does not match the pattern")
            continue
        new_files = new_file_name

        os.rename(file_name, new_files)

print("Files renamed")
