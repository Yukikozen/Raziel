"""
The main script. This module calls other modules,
depending on what user selected/specified
"""

############################
# STANDARD LIBRARY IMPORTS #
############################
import sys

from getpass import getuser

###############################
# RELATED THIRD PARTY IMPORTS #
###############################
import argparse

from typing import TextIO
from art import tprint

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common
import search

from tools_about import get_latest_release

#############
# CONSTANTS #
#############
MAIN_MENU: tuple = (
    "Search",
    "Tools",
    "Guides",
    "Notes",
    "Bookmarks",
    common.questionary.Separator(line="-" * 13),
    "Never mind"
)


#############
# FUNCTIONS #
#############
def exit_raziel():
    """
    Prints a goodbye message when user is done using Raziel

    :raises SystemExit: End Raziel and exit with code 0 (no error)
    """
    print(f"Goodbye {getuser()}! Thanks for stopping by!")

    # Exit Raziel
    raise SystemExit


def open_database() -> tuple[dict, dict, dict]:
    """
    Open tool_database.json which contains info on every tool
    for Raziel to get info from

    :return: A dictionary containing the keys and values in
    search_database.json called search_database, another
    dictionary containing the keys and values in
    tool_database.json called tool_database and a third
    dictionary containing the keys and values in
    guide_database.json
    :rtype: tuple[dict, dict, dict]
    """
    search_json_file: TextIO
    tool_json_file: TextIO
    guide_json_file: TextIO
    with open("search_database.json") as search_json_file, \
            open("tool_database.json") as tool_json_file, \
            open("guide_database.json") as guide_json_file:
        search_database: dict = common.json.load(search_json_file)
        tool_database: dict = common.json.load(tool_json_file)
        guide_database: dict = common.json.load(guide_json_file)

    return search_database, tool_database, guide_database


def main(search_database: dict, tool_database: dict, guide_database: dict):
    """
    Ask user what he/she would like to use Raziel for

    :param search_database: search_database.json stored as a dictionary
    :type search_database: dict
    :param tool_database: tool_database.json stored as a dictionary
    :type tool_database: dict
    :param guide_database: guide_database.json stored as a dictionary
    :type guide_database: dict
    """
    while True:
        options: str = common.questionary.select(
            "What can I do for you today?",
            choices=MAIN_MENU,
            qmark=common.QMARK,
            use_shortcuts=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        # Execute the function whose key matches options
        main_menu: dict = {
            MAIN_MENU[0]: common.partial(
                search.query_search,
                search_database,
                tool_database
            ),
            MAIN_MENU[1]: common.partial(
                common.tools.query_tools,
                tool_database
            ),
            MAIN_MENU[2]: common.partial(
                common.guides.query_guides,
                guide_database
            ),
            MAIN_MENU[3]: common.notes.query_notes,
            MAIN_MENU[4]: common.partial(
                common.bookmarks.query_bookmarks,
                tool_database,
                guide_database
            ),
            MAIN_MENU[-1]: exit_raziel
        }

        main_menu[options]()


if __name__ == '__main__':
    # Print an ASCII logo of the word "Raziel"
    tprint("Raziel", font="roman")

    # Store search_database.json into a dictionary called search_db
    # and tool_database.json into a dictionary called tool_db
    search_db: dict
    tool_db: dict
    search_db, tool_db, guide_db = open_database()

    # If user only entered "python raziel.py", start Raziel
    # from the start
    # Else, start Raziel depending on the arguments given
    if len(sys.argv) == 1:
        # Ask user what he/she wants to do
        main(search_db, tool_db, guide_db)
    else:
        parser: argparse.ArgumentParser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers()

        search_parser: argparse.ArgumentParser = subparsers.add_parser(
            "search",
            help="Access Raziel's search feature"
        )

        tools_parser: argparse.ArgumentParser = subparsers.add_parser(
            "tools",
            help="Enter --help / -h to see more commands specific to tools"
        )

        tools_parser.add_argument(
            "--list",
            "-ls",
            action="store_true",
            dest="tools_list",
            help="Show all tools currently supported by Raziel"
        )

        tools_subparsers = tools_parser.add_subparsers()

        about_tool_parser: argparse.ArgumentParser = tools_subparsers.add_parser(
            "tool_name",
            help="Specify a tool after tool_name, followed by --help/-h "
                 "for more info"
        )

        about_tool_parser.add_argument(
            "tool_name",
            type=str,
            help="Enter the name of a tool (See all tools by running "
                 "\"python raziel_old.py tools --list\")"
        )

        about_tool_parser.add_argument(
            "--about",
            "-a",
            action="store_true",
            dest="tool_about",
            help="Print all info about the specified tool "
                 "(Description, latest stable release, "
                 "official site, repository, etc.)"
        )

        about_tool_parser.add_argument(
            "--description",
            "-d",
            action="store_true",
            dest="tool_description",
            help="Print the description of the specified tool"
        )

        about_tool_parser.add_argument(
            "--latest",
            "-lsr",
            action="store_true",
            dest="tool_lsr",
            help="Print the latest stable release of the specified tool"
        )

        about_tool_parser.add_argument(
            "--official_site",
            "-os",
            action="store_true",
            dest="tool_official_site",
            help="Print the official site for the specified tool"
        )

        about_tool_parser.add_argument(
            "--repository",
            "-r",
            action="store_true",
            dest="tool_repo",
            help="Print the specified tool's repository site(s)"
        )

        about_tool_parser.add_argument(
            "--bookmark",
            action=argparse.BooleanOptionalAction,
            dest="tool_bookmark",
            help="--bookmark: Bookmark the tool | --no-bookmark: Remove tool from bookmarks"
        )

        tool_subparsers = about_tool_parser.add_subparsers()

        install_tool_parser: argparse.ArgumentParser = tool_subparsers.add_parser(
            "install",
            help="Show how to install the selected tool "
                 "(Append --platform/-p after \"install\" for a specific platform)"
        )

        install_tool_parser.add_argument(
            "--platform",
            "-p",
            choices=[
                "Windows",
                "Linux",
                "Mac"
            ],
            type=str.capitalize,
            dest="tool_platform",
            help="Print the installation steps for the specified tool based on platform specified"
        )

        how_to_use_tool_parser: argparse.ArgumentParser = tool_subparsers.add_parser(
            "how_to_use",
            help="Show how to use the selected tool. "
                 "If the tool has more than 1 feature, "
                 "show the features to user where he/she can "
                 "select the tool he/she wants to know"
        )

        error_tool_parser: argparse.ArgumentParser = tool_subparsers.add_parser(
            "errors",
            help="List all known errors for the specified tool. "
                 "Selecting one with show you how to fix the issue"
        )

        pros_cons_tool_parser: argparse.ArgumentParser = tool_subparsers.add_parser(
            "pros_cons",
            help="Show the pros and/or cons of the specified tool"
        )

        pros_cons_tool_parser.add_argument(
            choices=[
                "Pros",
                "Cons",
                "Both"
            ],
            type=str.capitalize,
            default="Both",
            nargs="?",
            dest="tool_pros_cons",
            help="Show the pros and/or cons of the specified tool"
        )

        guides_parser: argparse.ArgumentParser = subparsers.add_parser(
            "guides",
            help="See all of Raziel's guides"
        )

        notes_parser: argparse.ArgumentParser = subparsers.add_parser(
            "notes",
            help="Enter --help / -h to see more commands specific to notes"
        )

        notes_parser.add_argument(
            "--new",
            "-n",
            action="store_true",
            dest="notes_new",
            help="Launch a text editor where you can create a new note"
        )

        notes_parser.add_argument(
            "--list",
            "-ls",
            action="store_true",
            dest="notes_list",
            help="Show all notes you've made"
        )

        bookmarks_parser: argparse.ArgumentParser = subparsers.add_parser(
            "bookmarks",
            help="Enter --help / -h to see more commands specific to bookmarks"
        )

        bookmarks_parser.add_argument(
            "--list",
            "-ls",
            action="store_true",
            dest="bookmarks_list",
            help="Show all tools & guides that have been bookmarked"
        )

        bookmarks_parser.add_argument(
            "--edit",
            "-e",
            action="store_true",
            dest="bookmarks_edit",
            help="Bookmark tools and/or guides or remove them from the list"
        )

        args: argparse.Namespace = parser.parse_args()

        search_specified = "search" in sys.argv and len(sys.argv) == 2

        # Start Raziel's search feature
        search_specified and search.query_search(search_db, tool_db)

        # If --list or -ls specified, show user every tool
        # Raziel supports
        if "tools_list" in vars(args):
            tools_list_flag_raised: bool = args.tools_list

            if tools_list_flag_raised:
                print("Here's a list of tools Raziel supports:")
                for key in sorted(tool_db.keys()):
                    print(f"\u2022 {key}")

        # If "tool_name" in Namespace
        if "tool_name" in vars(args):
            tool_name: str = args.tool_name
            only_tool_name: bool = tool_name is not None and len(sys.argv) == 4
            about_flag_raised: bool = args.tool_about
            description_flag_raised: bool = args.tool_description
            lsr_flag_raised: bool = args.tool_lsr
            official_site_flag_raised: bool = args.tool_official_site
            repo_flag_raised: bool = args.tool_repo
            bookmark: bool = args.tool_bookmark

            five_args: bool = len(sys.argv) == 5

            about_tool: dict = tool_db[tool_name]["About"]

            # If user entered:
            # "python raziel.py tools tool_name tool_name",
            # Ask user what he/she wants to know about the tool
            if only_tool_name:
                common.tools.query_interest(tool_db, tool_name)
                common.tools.query_tools(tool_db)
                main(search_db, tool_db, guide_db)

            # If --about or -a specified, show user info about
            # the specified tool
            if about_flag_raised:
                common.print_about(tool_db[tool_name], tool_name)
            else:
                # If --description or -d specified, show user
                # what the specified tool is about
                description_flag_raised and print(
                    f"{tool_name}:\n{about_tool['Description']}"
                )

                # If --latest or -lsr specified, show user the
                # latest version and/or latest release date of
                # the specified tool
                if lsr_flag_raised:
                    get_latest_release(about_tool)

                    lsr_info: dict = about_tool[common.LATEST_STABLE_RELEASE]
                    latest_version: str = lsr_info["version"]
                    latest_release_date: str = lsr_info["release_date"]

                    if latest_version is None:
                        latest_version: str = "Version not found"

                    if latest_release_date is None:
                        latest_release_date: str = "Release date not found"

                    if latest_version is None and latest_release_date is not None:
                        print(
                            f"Latest release date:\n{latest_release_date}\n"
                        )
                    else:
                        print(
                            f"{common.LATEST_STABLE_RELEASE}:\n"
                            f"{latest_version} ({latest_release_date})\n"
                        )

                # If --official_site or -os specified, show user the
                # official site of the specified tool
                official_site_flag_raised and print(
                    f"{tool_name}'s official site:\n{about_tool['Official site']}"
                )

                # If --repository or -r specified, show user every
                # repository site the specified tool is in
                repository_sites: tuple = (
                    "Github",
                    "SourceForge",
                    "Gitlab",
                    "BitBucket",
                    "PyPI"
                )

                if repo_flag_raised:
                    heading: str = f"{tool_name}'s repository site(s)"
                    print(f"{heading}\n{'-' * len(heading)}")
                    [
                        print(f"{site}:\n{about_tool[site]}\n")
                        for site in repository_sites
                        if site in tool_db[tool_name]["About"]
                    ]

                if "tool_bookmark" in vars(args):
                    diff_value = bookmark != tool_db[tool_name]["Bookmarked"]

                    if diff_value:
                        common.bookmarks.add_remove_bookmark(
                            tool_db=tool_db,
                            items=[tool_name],
                            bookmark_flags=[bookmark]
                        )

                # If user entered:
                # "python raziel.py tools tool_name tool_name install --platform PLATFORM",
                # Show user how to install the specified tool for the platform specified
                if "tool_platform" in vars(args):
                    platform: str = args.tool_platform
                    platform_not_none: bool = platform is not None

                    platform_not_none and print(
                        tool_db[tool_name][common.WANT_TO_KNOW_CHOICES[1]][platform]
                    )

                # If user entered:
                # "python raziel.py tools tool_name tool_name how_to_use",
                # show a list of features the specified tool has where
                # he/she can enter to see how to use that feature.
                # If the tool only has 1 feature, show how to use that
                # feature
                if "how_to_use" in sys.argv and five_args:
                    common.tools.more_queries(
                        tool_db, {
                            "tool": tool_name,
                            "want_to_know": common.WANT_TO_KNOW_CHOICES[2]
                        }
                    )
                    common.tools.query_interest(tool_db, tool_name)
                    common.tools.query_tools(tool_db)
                    main(search_db, tool_db, guide_db)

                # If user entered:
                # "python raziel.py tools tool_name tool_name errors",
                # show a list of errors the specified tool has where
                # he/she can enter to see how to solve the error
                if "errors" in sys.argv and five_args:
                    common.tools.more_queries(
                        tool_db, {
                            "tool": tool_name,
                            "want_to_know": common.WANT_TO_KNOW_CHOICES[3]
                        }
                    )
                    common.tools.query_interest(tool_db, tool_name)
                    common.tools.query_tools(tool_db)
                    main(search_db, tool_db, guide_db)

                # If "tool_pros_cons" in Namespace print the
                # pros and/or cons of the specified tool (tool_name)
                if "tool_pros_cons" in vars(args):
                    pros_cons: str = args.tool_pros_cons
                    pros_cons_flag_raised: bool = pros_cons is not None

                    pros_cons_flag_raised and common.print_pros_cons(
                        tool_db[tool_name]["Pros & Cons"],
                        tool_name,
                        pros_cons
                    )

        guides_specified = "guides" in sys.argv and len(sys.argv) == 2

        # Ask user which guide he/she wants to read
        guides_specified and common.guides.query_guides(guide_db)

        # List all notes user made
        if "notes_list" in vars(args):
            notes_list_flag_raised: bool = args.notes_list
            notes_list_flag_raised and common.notes.read_notes()

        # Launch text editor for user to create a new note
        if "notes_new" in vars(args):
            notes_new_flag_raised: bool = args.notes_new
            notes_new_flag_raised and common.notes.launch_note_editor()

        if "bookmarks_list" in vars(args):
            bookmarks_list_flag_raised: bool = args.bookmarks_list
            edit_bookmarks_flag_raised: bool = args.bookmarks_edit

            # If --list or -ls specified, show user every tool
            # user has bookmarked. Else if --edit or -e
            # specified, show user every tool where user can
            # select which to bookmark or remove
            if bookmarks_list_flag_raised:
                common.bookmarks.see_bookmarks(tool_db, guide_db)
            elif edit_bookmarks_flag_raised:
                common.bookmarks.edit_bookmarks(tool_db, guide_db)
