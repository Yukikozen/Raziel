"""
This module focuses on the guides users can
select to read
"""
##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common


#############
# FUNCTIONS #
#############
def subchapters_option(
        guide_chapter: dict,
        chapter: str,
        chapter_bookmarked: bool,
        *args: list
) -> tuple[list, str, str]:
    """
    Get all subchapters from guide_database.json
    & include an option to launch a text editor,
    an option to bookmark the chapter (or remove
    it from bookmarks), & and option to get out

    :param guide_chapter: A dictionary with all values from the chapter key
    :type guide_chapter: dict
    :param chapter: The chapter user wants to read
    :type chapter: str
    :param chapter_bookmarked: Has the chapter been bookmarked?
    :type chapter_bookmarked: bool
    :param args: Indicate where user came from
    :type args: list
    :return: All the options needed for asking user to choose a subchapter
    in query_subchapters
    :rtype: tuple[list, str, str]
    """
    bookmark_option = f"Remove bookmark for {chapter}" \
        if chapter_bookmarked else f"Bookmark {chapter}"

    came_from_bookmarks: bool = bool(args) and args[0] == "from bookmarks"

    back_option = common.GO_BACK_BOOKMARKS \
        if came_from_bookmarks else "Read another chapter"

    subchapters: list[str] = list(guide_chapter["Subchapters"].keys())

    # Don't show the option "Read the whole chapter"
    # if there's only 1 subchapter since it would be
    # redundant
    more_than_one_subchapter = len(subchapters) > 1
    more_than_one_subchapter and subchapters.append("Read the whole chapter")

    return subchapters, bookmark_option, back_option


def query_subchapters(guide_db: dict, guide: str, chapter: str, *args: str):
    """
    Ask user to select a subchapter from the selected chapter to read
    or read the whole chapter

    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    :param guide: The guide user wants to read
    :type guide: str
    :param chapter: The chapter user wants to read
    :type chapter: str
    :param args: Indicate where user came from
    :type args: list
    """
    while True:
        guide_chapter = guide_db[guide][chapter]

        chapter_bookmarked = guide_chapter["Bookmarked"]

        subchapters, bookmark_option, back_option = subchapters_option(
            guide_chapter,
            chapter,
            chapter_bookmarked,
            *args
        )

        # Ask user to choose a subchapter in the selected chapter to read
        # or, read the whole chapter
        subchapter: str = common.questionary.select(
            message=f"Select a subchapter or read the whole of {chapter}",
            choices=common.add_options(
                subchapters,
                "Open text editor",
                bookmark_option,
                back_option
            ),
            qmark=common.QMARK,
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        read_another_chapter: bool = subchapter == "Read another chapter"
        go_back_bookmarks: bool = subchapter == common.GO_BACK_BOOKMARKS
        back_option_selected: bool = read_another_chapter or go_back_bookmarks
        read_whole_chapter: bool = subchapter == "Read the whole chapter"
        open_text_editor: bool = subchapter == "Open text editor"
        bookmark_chapter: bool = subchapter == bookmark_option

        if back_option_selected:
            break

        if read_whole_chapter:
            for key in guide_chapter['Subchapters']:
                print(
                    f"{'=' * len(key)}\n"
                    f"{key}\n{'=' * len(key)}\n"
                    f"{guide_chapter['Subchapters'][key]}\n"
                )
        elif open_text_editor:
            common.notes.launch_note_editor()
        elif bookmark_chapter:
            common.bookmarks.add_remove_bookmark(
                guide_db=guide_db,
                items=[chapter],
                bookmark_flags=[not chapter_bookmarked]
            )
        else:
            print(
                f"{'=' * len(subchapter)}\n"
                f"{subchapter}\n{'=' * len(subchapter)}\n"
                f"{guide_chapter['Subchapters'][subchapter]}\n"
            )


def query_chapters(guide_db: dict, select_guide: str):
    """
    Ask user to select the chapter he/she wants to read

    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    :param select_guide: The guide user wants to read
    :type select_guide: str
    """
    while True:
        # Select a chapter in the guide
        chapter: str = common.questionary.select(
            message="Select a chapter",
            choices=common.add_options(
                list(guide_db[select_guide].keys()),
                "Read something else"
            ),
            qmark=common.QMARK,
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        read_something_else = chapter == "Read something else"

        if read_something_else:
            break

        query_subchapters(guide_db, select_guide, chapter)


def query_guides(guide_db: dict):
    """
    Ask user to select a guide to read

    :param guide_db: guide_database.json stored as a dictionary
    :type guide_db: dict
    """
    while True:
        select_guide: str = common.questionary.select(
            message="What would you like to read today?",
            choices=common.add_options(
                list(guide_db.keys()),
                common.GO_BACK_MAIN_MENU
            ),
            qmark=common.QMARK,
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        go_back_main_menu_selected: bool = select_guide == common.GO_BACK_MAIN_MENU

        if go_back_main_menu_selected:
            break

        query_chapters(guide_db, select_guide)
