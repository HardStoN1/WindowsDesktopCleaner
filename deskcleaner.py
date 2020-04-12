import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import datetime
import platform
import shutil
import sys

isOne = True
dir_dic = {".mp3" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Audio",                                                      ".wav" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Videos",                                                             ".rar" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Compressed",                                                                ".zip" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Compressed",                                                                ".iso" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Other",                                                                     ".sql" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Database",                                                     ".apk" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Android",                                                      ".exe" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Games",                                                                     ".gif" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Gif",                                                                ".png" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",                                                             ".jpg" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",                                                             ".jpeg" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",
    ".psd" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",
    ".tif" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",
    ".tiff" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",
    ".svg" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Images",
    ".py" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Python",
    ".css" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".html" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".htm" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".js" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".php" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".asp" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".aspx" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Web",
    ".ppt" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Presentation",
    ".pptx" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Presentation",
    ".cs" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\C#",
    ".py" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Python",
    ".bat" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Shell",
    ".dart" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Programming\\Android",
    ".avi" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Videos",
    ".mp4" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Videos",
    ".wmv" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Media\\Videos",
    ".pdf" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".txt" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".doc" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".docx" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".odt" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".csv" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Text",
    ".dll" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Other",
    ".msi" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Games",
    ".jfif" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Images",
    ".webp" : r"C:\\Users\\Gal S\\Desktop\\Gal\\Images",}

class Watcher:
    DIRECTORY_TO_WATCH = r"C:\\Users\\Gal S\\Desktop"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            work_single(event.src_path, True)

def get_date_month(path_to_file):
    if platform.system() == "Windows":
        create_time = os.stat(path_to_file).st_ctime
        create_datetime = datetime.datetime.fromtimestamp(create_time)
        return create_datetime.strftime("%m")
    else:
        print("We don't support this OS.")
        return

def get_date_year(path_to_file):
    if platform.system() == "Windows":
        create_time = os.stat(path_to_file).st_ctime
        create_datetime = datetime.datetime.fromtimestamp(create_time)
        return create_datetime.strftime("%Y")
    else:
        print("We don't support this OS.")
        return

def get_file_name(path_to_file):
    return str(os.path.basename(path_to_file))


def get_file_exten(path_to_file):
    try:
        path = str(path_to_file)
        pos = []
        coun = 0
        for c in path:
            if c == '.':
                pos.append(coun)
            coun = 1

        last_point = int(pos[len(pos) - 1])
        return str(path[last_point:])
    except Exception as e:
        print("Oops! from exten -> " + str(e))
        return

def move_file(src, dest):
    shutil.move(src, dest)

def work_single(file_src, isOrigin):
    try:
        if isOrigin:
            print("Working.... for one item at a time in the directory")

        file_exten = str(get_file_exten(file_src))
        year = str(get_date_year(file_src))
        month = str(get_date_month(file_src))

        desired_dir = str(dir_dic[file_exten])
        n_dir = desired_dir + "\\" + year + "\\"
        n_dir_with_month = n_dir + month + "\\"
        filename = get_file_name(file_src)

        if os.path.isfile(n_dir + "\\" + filename):
            tempName = str(filename.split('.')[0])
            extenTemp = str(filename.split('.')[1])
            tempName = str(tempName + " copy")
            filename = str(tempName + "." + extenTemp)


        if not os.path.isdir(n_dir):
            os.mkdir(n_dir)
            os.mkdir(n_dir_with_month)
            move_file(file_src, n_dir_with_month + "\\" + filename)
        elif os.path.isdir(n_dir) == True and os.path.isdir(n_dir_with_month) == False:
            os.mkdir(n_dir_with_month)
            move_file(file_src, n_dir_with_month + "\\" + filename)
        elif os.path.isdir(n_dir) == True and os.path.isdir(n_dir_with_month) == True:
            move_file(file_src, n_dir_with_month + "\\" + filename)

    except Exception as e:
        print("Oops! from work single -> " + str(e))

def work_multi(dir_to_watch):
    global isOne
    print("Working.... for all items in the directory")
    for fn in os.listdir(dir_to_watch):
        t_l = dir_to_watch + "\\" + fn
        if os.path.isdir(t_l) == False:
            exten = get_file_exten(t_l)
            if exten in dir_dic:
                work_single(t_l, False)
                if isOne:
                    w = Watcher()
                    w.run()
                    isOne = False
        else:
            print(str(fn) + ' Is not a file')
            continue


def work_on_file():
    work_multi(r"C:\\Users\\Gal S\\Desktop")

work_on_file()