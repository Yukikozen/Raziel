"""
This module contains libraries and function commonly used
throughout this project.So instead of importing the same
libraries over and over again for different files, with
this module, you just have to import common
"""
############################
# STANDARD LIBRARY IMPORTS #
############################
import inspect
import json
import re

from functools import partial
from typing import List, Tuple, Optional
###############################
# RELATED THIRD PARTY IMPORTS #
###############################
import questionary

from questionary import Style

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import bookmarks
import guides
import notes
import tools

from tools_about import print_about
from tools_pros_cons import print_pros_cons

#############
# CONSTANTS #
#############
QMARK: str = "Raziel:"
GO_BACK: str = "Go back"
GO_BACK_BOOKMARKS = "Go back to my bookmarks"
GO_BACK_MAIN_MENU: str = "Go back to main menu"
LATEST_STABLE_RELEASE: str = "Latest stable release"
WANT_TO_KNOW_CHOICES: list[str] = [
    "About",
    "How to install",
    "How to use",
    "Errors & how to fix",
    "Pros & Cons"
]
CUSTOM_STYLE = Style([
    ('answer', 'fg:white bg:default'),
    ('highlighted', 'fg:black bg:cyan'),
    ('separator', 'fg:#8f8f8f')
])


#############
# FUNCTIONS #
#############
def add_options(add_to: list, *args: str) -> list:
    """
    Add more options to the list of choices in add_to
    that mostly aren't the main focus of the options
    (E.g. An option for going back to the previous question)
    :param add_to: The list to add the new options to
    :type add_to: list
    :param args: Contains a tuple of the options we'll be
    adding
    :type args: tuple[str]
    :return: add_to with the options in args added
    :rtype: list
    """
    longest_length: int = len(max(args, key=len))

    to_add = [x for x in list(args) if x not in set(add_to)]
    to_add[:0] = [questionary.Separator(line="-" * (longest_length + 3))]

    add_to.extend(to_add)

    return add_to
