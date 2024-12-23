import zipfile
import os

class FileHandle(object):    
    def __init__(self):

        if os.path.exists("students.dat"):
            self.decompress_files()
        if not os.path.exists("data"):
            os.makedirs("data")

    def compress_files(self):
        # Compress all data files into students.dat.
        with zipfile.ZipFile("students.dat", "w") as zipf:
            for file in ["students.pkl", "courses.pkl", "marks.pkl"]:
                filepath = os.path.join("data", file)
                if os.path.exists(filepath):
                    zipf.write(filepath, file)

    def decompress_files(self):
        # Decompress students.dat and extract its contents.
        with zipfile.ZipFile("students.dat", "r") as zipf:
            zipf.extractall("data")

    def exit_program(self, stdscr):
        # Compress all files and exit.
        self.compress_files()
        stdscr.addstr(0,0,"Data compressed into students.dat. Exiting program...")
        stdscr.refresh()
        stdscr.getch()