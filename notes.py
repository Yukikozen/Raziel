"""
This module focuses on Raziel's note taking feature.
Users can read a note they have made or create a new
one
"""
############################
# STANDARD LIBRARY IMPORTS #
############################
import glob
import webbrowser
import tkinter

from pathlib import Path
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from typing import Union, Any
from prompt_toolkit.validation import Validator, ValidationError

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common

#############
# CONSTANTS #
#############
CANT_FIND = "I can't find the file I'm looking for"


###########
# CLASSES #
###########
class FileValidator(Validator):
    """
    Validate the filepath user enters
    """

    def validate(self, file_to_validate):
        """
        Check if the path user entered exists and that it is a TXT file
        :param file_to_validate: The filepath user enters
        :raises ValidationError: If it's not a TXT file or there's no such
        file
        """
        not_txt: bool = not file_to_validate.text.lower().endswith('.txt')
        file_not_found: bool = not Path(file_to_validate.text).exists()

        exit_cmds: tuple[str, str] = ("exit", "back")
        not_an_exit_cmd: bool = file_to_validate.text.lower() not in exit_cmds

        if not_an_exit_cmd:
            if file_not_found:
                raise ValidationError(
                    message="Error 404: File not found"
                )
            elif not_txt:
                raise ValidationError(
                    message=f"{file_to_validate.text} is not a TXT file"
                )


#############
# FUNCTIONS #
#############
def launch_note_editor():
    """
    Launch a text editor GUI created using Tkinter
    """

    def change_font(*self):
        """
        Change font to whatever new font user selected
        :param self: If not included will throw
        "change_front() takes 0 positional arguments but
        1 was given" due to self being passed when the
        function is called
        """
        text_area.config(
            font=(
                font_name.get(),
                size_box.get()
            )
        )

    def new_file():
        """
        Replace current window with a new, clean window
        """
        new_window = tkinter.Toplevel(window)
        new_window.title("Untitled")
        text_area.delete(1.0, tkinter.END)

    def open_file():
        """
        Open an existing file
        """
        file_to_open = askopenfilename(
            defaultextension=".txt",
            file=[
                ("All Files", "*.*"),
                ("Text Documents", "*.txt")
            ]
        )

        if file_to_open is not None:
            window.title(Path(file_to_open).name)

            text_area.delete(1.0, tkinter.END)

            with open(file_to_open) as selected_file:
                text_area.insert(1.0, selected_file.read())

    def save_file():
        """
        Save the currently opened file
        """
        file_to_save = asksaveasfilename(
            initialfile='untitled.txt',
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Documents", "*.txt")
            ]
        )

        if file_to_save is not None:
            window.title(Path(file_to_save).name)

            with open(file_to_save, 'w') as write_file:
                write_file.write(
                    text_area.get(
                        1.0,
                        tkinter.END
                    )
                )

    def cut():
        """
        Allow user to cut a text and paste it
        somewhere else
        """
        text_area.event_generate("<<Cut>>")

    def copy():
        """
        Allow user to copy text
        """
        text_area.event_generate("<<Copy>>")

    def paste():
        """
        Allow user to paste the text he/she
        had copied
        """
        text_area.event_generate("<<Paste>>")

    def about():
        """
        Show user what this program is about
        """
        showinfo(
            "About this program",
            "This is a text editor for you to quickly take down any notes you need"
        )

    window = tkinter.Tk()
    window.title("Untitled")

    window_width = 800
    window_height = 500
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = int(screen_width / 2 - window_width / 2)
    y_coordinate = int(screen_height / 2 - window_height / 2)

    window.geometry(
        f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}"
    )

    font_name = tkinter.StringVar(window)
    font_name.set("Arial")

    font_size = tkinter.StringVar(window)
    font_size.set("16")

    text_area = tkinter.Text(
        window,
        font=(
            font_name.get(),
            font_size.get()
        )
    )

    text_area.grid(
        sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W
    )

    scroll_bar = tkinter.Scrollbar(text_area)
    scroll_bar.pack(
        side=tkinter.RIGHT,
        fill=tkinter.Y
    )

    text_area.config(yscrollcommand=scroll_bar.set)

    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    frame = tkinter.Frame(window)
    frame.grid()

    font_box = tkinter.OptionMenu(
        frame,
        font_name,
        *font.families(),
        command=change_font
    )
    font_box.grid(row=0, column=1)

    size_box = tkinter.Spinbox(
        frame,
        from_=1,
        to=100,
        textvariable=font_size,
        command=change_font
    )
    size_box.grid(row=0, column=2, padx=10)

    menu_bar = tkinter.Menu(window)
    window.config(menu=menu_bar)

    file_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.destroy)

    edit_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)

    help_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    window.mainloop()


def read_notes():
    """
    Show a list of notes user has made in which he/she
    can select to read and further edit
    If a note is not listed, the user is given the
    option to try and find the file via the filepath
    """
    while True:
        files: list[
            Union[Union[bytes, str], Any]
        ] = glob.glob("Raziel Notes/*.txt")

        common.add_options(files, CANT_FIND, common.GO_BACK)

        # Ask user which file he/she wants to read
        open_file: str = common.questionary.select(
            message="Select the file you want to read",
            qmark=common.QMARK,
            choices=files,
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        cant_find_file: bool = open_file == CANT_FIND
        file_selected: bool = open_file != common.GO_BACK and not cant_find_file

        # Open the file selected in the user's default
        # text editor
        if cant_find_file:
            open_file: str = common.questionary.path(
                message="Not able to find your file? Try typing it out! "
                        "(Enter \"exit\" or \"back\" to go back to the "
                        "file selection screen)\nFile: ",
                qmark=common.QMARK,
                validate=FileValidator
            ).ask()

            if open_file in ("exit", "back"):
                continue

            if open_file != "":
                file_selected = True

        # Launch a text editor if user selects a file
        if file_selected:
            webbrowser.open(open_file)
        else:
            break


def query_notes():
    """
    Ask user whether he/she wants to create a new note
    or see an existing note
    """
    while True:
        notes_choices: list[str] = [
            "Create a new note",
            "See existing notes"
        ]

        common.add_options(
            notes_choices,
            common.GO_BACK_MAIN_MENU
        )

        # Ask user whether he/she wants to create a new note
        # or open those that has been made
        notes: str = common.questionary.select(
            message="Would you like to create a new note "
                    "or see those you've created?",
            qmark=common.QMARK,
            choices=notes_choices,
            use_shortcuts=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        see_notes: bool = notes == notes_choices[1]
        new_note: bool = notes == notes_choices[0]

        # If user wants to create a new note, launch the Tkinter
        # text editor. Else, if user wants to see an existing note,
        # open that file in the computer's default text editor
        # (E.g. Notepad)
        if new_note:
            launch_note_editor()
        elif see_notes:
            read_notes()
        else:
            break
