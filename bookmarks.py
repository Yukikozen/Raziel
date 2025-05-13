"""
This module focuses on adding & removing a tool or
a chapter from a guide from the bookmarks list
"""
############################
# STANDARD LIBRARY IMPORTS #
############################
from typing import TextIO, Any

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common

#############
# CONSTANTS #
#############
SEE_BOOKMARKS: str = "See my bookmarks"
EDIT_BOOKMARKS: str = "Edit my bookmarks"


#############
# FUNCTIONS #
#############
def add_remove_bookmark(**kwargs: [tuple, dict]):
    """
    Bookmark an item or remove it from the current list of
    bookmarks, saving the changes into tool_database.json
    and/or guide_database.json

    :param kwargs: A dictionary made up of 1-2 dictionaries
    (tool_db, guide_db) & 2 lists (items, flags).
    tool_db: tool_database.json stored as a dictionary
    guide_db : guide_database.json stored as a dictionary
    items: items to update.
    flags: Whether the item are to be bookmarked or removed
    from bookmarks
    """
    tool_db: dict = {}
    if "tool_db" in kwargs.keys():
        tool_db: dict = kwargs["tool_db"]

    guide_db: dict = {}
    if "guide_db" in kwargs.keys():
        guide_db: dict = kwargs["guide_db"]

    items: list = kwargs["items"]
    bookmark_flags: list = kwargs["bookmark_flags"]

    # Update whether the item should be bookmarked or not
    item: str
    flag: bool
    for item, flag in zip(items, bookmark_flags):
        if item in tool_db:
            tool_db[item]["Bookmarked"] = flag
        else:
            for key in guide_db.keys():
                if item in guide_db[key]:
                    guide_db[key][item]["Bookmarked"] = flag

    # Update tool_database.json
    if bool(tool_db):
        json_file: TextIO
        with open("tool_database.json", "r+") as json_file:
            json_file.seek(0)
            common.json.dump(tool_db, json_file)
            json_file.truncate()

    # Update guide_database.json
    if bool(guide_db):
        json_file: TextIO
        with open("guide_database.json", "r+") as json_file:
            json_file.seek(0)
            common.json.dump(guide_db, json_file)
            json_file.truncate()


def tools_and_guides(tool_db: dict, guide_db: dict) -> list[Any]:
    """
    For edit_bookmarks
    Creates the choices where user can choose which
    tool or chapter (guide) he/she wants to bookmark
    or remove from the bookmarks list

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    :return: Tools & Chapters (Guides) in the form of a list
    where user can choose which to bookmark/remove
    :rtype: list[Any]
    """
    # Adding tools to the list
    bookmarks: list[Any] = [
        f"{key} [Select to remove]"
        if tool_db[key]["Bookmarked"] is True
        else f"{key} [Select to bookmark]"
        for key in tool_db.keys()
    ]

    # Adding a Tools heading to differentiate from Guides
    bookmarks[0:0] = [
        common.questionary.Separator(
            f"Tools\n   {'-' * 5}"
        )
    ]

    # Adding a Guides heading to differentiate from Tools
    bookmarks.append(
        common.questionary.Separator(
            f"\n   Guides\n   {'-' * 5}"
        )
    )

    # Adding chapters (guides) to the list
    key: str
    for key in guide_db.keys():
        for subkey in guide_db[key].keys():
            if guide_db[key][subkey]["Bookmarked"]:
                bookmarks.append(f"<{key}> {subkey} [Select to remove]")
            else:
                bookmarks.append(f"<{key}> {subkey} [Select to bookmark]")

    return bookmarks


def edit_bookmarks(tool_db: dict, guide_db: dict):
    """
    Add item to the list of bookmarks
    or remove an item from it

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    """
    bookmarks = tools_and_guides(tool_db, guide_db)

    # Get user to select whatever he/she wants removed or bookmarked
    # If "Go back" is selected, the user is not allowed to select
    # any other item
    bookmark_or_not: list[str] = common.questionary.checkbox(
        message="Select those you want to bookmark or remove",
        qmark=common.QMARK,
        choices=common.add_options(
            bookmarks,
            common.GO_BACK
        ),
        validate=lambda selection: (
            True if (len(selection) == 1 and selection[0] == bookmarks[-1]
                     ) or bookmarks[-1] not in selection
            else "You can't select another option if you have selected \"Go back\""
        ),
        use_jk_keys=True,
        style=common.CUSTOM_STYLE
    ).ask()

    go_back_not_selected = common.GO_BACK not in bookmark_or_not

    if go_back_not_selected:
        # Update the bookmarks list with those user selected
        # The regex is to remove the "(Select to ...)" substring
        bookmarks: list[str] = [
            common.re.sub(r"\s\[.*]", "", element)
            for element in bookmark_or_not
        ]

        bookmarks: list[str] = [
            common.re.sub(r"^<.*>\s", "", element)
            for element in bookmarks
        ]

        # Create a list of booleans that will be used together with
        # the bookmarks list
        bookmark_or_remove: list[bool] = [
            not tool_db[element]["Bookmarked"]
            for element in bookmarks
            if element in tool_db
        ]

        for key in guide_db.keys():
            for element in bookmarks:
                if element in guide_db[key]:
                    bookmark_or_remove.append(
                        not guide_db[key][element]["Bookmarked"]
                    )

        # Add item to bookmark or remove it from the list
        add_remove_bookmark(
            tool_db=tool_db,
            guide_db=guide_db,
            items=bookmarks,
            bookmark_flags=bookmark_or_remove
        )


def get_bookmarks(tool_db: dict, guide_db: dict):
    """
    Get all the bookmarks user has made & create a list from it

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    :return: A list of bookmarks
    """
    # Get tools user bookmarked
    list_of_bookmarks: list[Any] = [
        key for key in tool_db.keys()
        if tool_db[key]["Bookmarked"] is True
    ]

    # Add a Tools heading to differentiate it from Guides
    list_of_bookmarks[0:0] = [
        common.questionary.Separator(
            f"Bookmarked Tools\n   {'-' * 16}"
        )
    ]

    # Add a Guides heading to differentiate it from Tools
    list_of_bookmarks.append(
        common.questionary.Separator(
            f"\n   Bookmarked Guides Chapters\n   {'-' * 26}"
        )
    )

    # Get chapters user bookmarked
    for key in guide_db.keys():
        for subkey in guide_db[key].keys():
            if guide_db[key][subkey]["Bookmarked"]:
                list_of_bookmarks.append(subkey)

    return list_of_bookmarks


def see_bookmarks(tool_db: dict, guide_db: dict):
    """
    List all tools that has been bookmarked

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    """
    while True:
        list_of_bookmarks = get_bookmarks(tool_db, guide_db)

        # List tools that have been bookmarked
        # Pressing enter on a tool will allow you
        # to see more info about the tool
        bookmarks: str = common.questionary.select(
            message="My bookmarks",
            qmark=common.QMARK,
            choices=common.add_options(
                list_of_bookmarks,
                common.GO_BACK
            ),
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        go_back_chosen: bool = bookmarks == common.GO_BACK
        is_tool_bookmark = bookmarks in tool_db

        if go_back_chosen:
            break

        if is_tool_bookmark:
            common.tools.query_interest(
                tool_db,
                bookmarks,
                "from bookmarks"
            )
        else:
            for guide in guide_db:
                if bookmarks in guide_db[guide]:
                    common.guides.query_subchapters(
                        guide_db,
                        guide,
                        bookmarks,
                        "from bookmarks"
                    )


def query_bookmarks(tool_db: dict, guide_db: dict):
    """
    Ask user whether he/she wants to see
    every tool bookmarked or add/remove
    tools from the bookmark list

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    """
    while True:
        list_or_edit_menu: list[str] = [
            SEE_BOOKMARKS,
            EDIT_BOOKMARKS
        ]

        common.add_options(
            list_or_edit_menu,
            common.GO_BACK_MAIN_MENU
        )

        # Ask user if he/she would like to view his/her bookmarks
        # or add/remove from the list of bookmarks
        see_or_edit: str = common.questionary.select(
            message="Would you like to see / edit your bookmarks",
            qmark=common.QMARK,
            choices=list_or_edit_menu,
            use_shortcuts=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        # Execute the function based on what user selects
        if see_or_edit in (SEE_BOOKMARKS, EDIT_BOOKMARKS):
            {
                SEE_BOOKMARKS: common.partial(
                    see_bookmarks,
                    tool_db,
                    guide_db
                ),
                EDIT_BOOKMARKS: common.partial(
                    edit_bookmarks,
                    tool_db,
                    guide_db
                )
            }[see_or_edit]()
        else:
            break
