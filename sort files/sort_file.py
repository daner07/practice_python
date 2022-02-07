import shutil
import os.path
import datetime
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('600x190')
root.title("Сортировка файлов по дате")

directory = 0
path_sorting = 0


def path_from_button():
    global directory
    directory = filedialog.askdirectory() + "/"
    label_from_button.config(text=directory)


def path_into_button():
    global path_sorting
    path_sorting = filedialog.askdirectory() + "/"
    print(path_sorting)
    label_into_button.config(text=path_sorting)


def start_button():
    sum_file = 0
    sum_file_exist = 0


    for root, dirs, files in os.walk(directory, True):
        # print("root:%s" % root)
        # print("dirs:%s" % dirs)
        # print("files", files)

        # вывод времени модификации файлов в папке
        for file in files:
            dir_file = directory + file
            now = os.path.getmtime(dir_file)  # получение даты изменения файла
            print(now)
            mtime_file = datetime.datetime.fromtimestamp(now).strftime('%Y-%m (%b)-%d')

            print(file + "     Date Modif=    " + mtime_file)
            try:
                os.mkdir(path_sorting + mtime_file)
                shutil.copy(dir_file, path_sorting + mtime_file)
                sum_file += 1

            except:
                if os.path.exists(path_sorting + mtime_file):
                    print('Файл уже существует')
                    sum_file_exist += 1
                else:
                    shutil.move(dir_file, path_sorting + mtime_file)

        label_start_button.config(text=f"Копировано файлов {sum_file},  Пропущено файлов {sum_file_exist}")



from_button = Button(root, text="Папка с фото", pady=5, padx=5, command=path_from_button)
from_button.grid(column=0, row=0, padx=10, pady=10)
label_from_button = Label(root, font=("Arial Bold", 12))
label_from_button.grid(column=1, row=0)

into_button = Button(root, text="Куда сохранить", pady=5, padx=5, command=path_into_button)
into_button.grid(column=0, row=1, padx=10, pady=10)
label_into_button = Label(root, font=("Arial Bold", 12))
label_into_button.grid(column=1, row=1)

start_button = Button(root, text="Сортировать", pady=5, padx=5, command=start_button)
start_button.grid(column=0, row=2, padx=10, pady=10)
label_start_button = Label(root, font=("Arial Bold", 12))
label_start_button.grid(column=1, row=2)

root.mainloop()
