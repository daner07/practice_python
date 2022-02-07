from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x500+1000+300')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    messagebox.showinfo(title='About Program', message='Daniil')


def notepad_quit():
    answer = messagebox.askquestion(title='Quit program', message='Quit??')
    if answer == 'yes':
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='File...', filetypes=(("Texts", "*.txt"), ("All files", "*.*")))
    if file_path:
        text_area.delete('1.0', END)
        text_area.insert('1.0', open(file_path, encoding='utf8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(title='Save File', filetypes=(("Texts", "*.txt"), ("All files", "*.*")))
    f = open(file_path, 'w', encoding='utf8')
    text = text_area.get('1.0', END)
    f.write(text)
    f.close()


def change_theme(theme):
    text_area['bg'] = theme_colors[theme]['text_bg']
    text_area['fg'] = theme_colors[theme]['text_fg']
    text_area['insertbackground'] = theme_colors[theme]['cursor']
    text_area['selectbackground'] = theme_colors[theme]['select_bg']


# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=notepad_quit)

main_menu.add_cascade(label='File', menu=file_menu)

# Themes
themes_menu = Menu(main_menu, tearoff=0)
themes_menu_sub = Menu(themes_menu, tearoff=0)
themes_menu_sub.add_command(label="Lite themes", command=lambda: change_theme('light'))
themes_menu_sub.add_command(label="Dark themes", command=lambda: change_theme('dark'))
themes_menu.add_cascade(label="Themes", menu=themes_menu_sub)
themes_menu.add_command(label='About program', command=about_program)
main_menu.add_cascade(label='Settings', menu=themes_menu)

theme_colors = {
    "dark": {
        "text_bg": "#343D46", "text_fg": "#C6DEC1", "cursor": "white", "select_bg": "#4E5a65"
    },
    "light": {
        "text_bg": "white", "text_fg": "black", "cursor": "#8000FF", "select_bg": "#777"
    }
}

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_area = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10,
                 wrap=WORD, insertbackground=theme_colors['dark']['cursor'],
                 selectbackground=theme_colors['dark']['select_bg'], spacing1=5, width=30, font=('CourierNew', 15))

text_area.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_area.yview())
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)

root.mainloop()
