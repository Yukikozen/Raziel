"""This module focuses on the tools feature of Raziel"""

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common

from tools_tutorial import print_how_to_use

#############
# CONSTANTS #
#############
SELECT_ANOTHER = "Select another tool"
SEARCH_SOMETHING_ELSE = "Search something else"
BOOKMARK = "Bookmark this tool"
REMOVE_BOOKMARK = "Remove bookmark for this tool"


#############
# FUNCTIONS #
#############
def result_tool(raziel_db: dict, results: dict, **kwargs: str):
    """
    Call a function that outputs the results based on what
    the user selected when asked what he/she would like to
    know about the selected tool

    :param raziel_db: tool_database.json stored as a dictionary
    :type raziel_db: dict
    :param results: A dictionary containing what user selected
    :type results: dict
    :param kwargs: For any additional keyword arguments
    :type kwargs: str
    """
    option_selected: str = results["want_to_know"]
    tool: str = results["tool"]
    db_tool: dict = raziel_db[tool]
    db_tool_interest: dict = db_tool[option_selected]

    # An empty dictionary returns False
    kwargs_not_empty: bool = bool(kwargs) is True

    # A dictionary that has what the user wants
    # to know as its keys and the function that
    # will display what the user wants to know
    # as its values
    output: dict = {
        common.WANT_TO_KNOW_CHOICES[0]: common.partial(
            common.print_about,
            db_tool,
            tool
        ),
        common.WANT_TO_KNOW_CHOICES[2]: common.partial(
            print_how_to_use,
            db_tool_interest,
            kwargs
        ),
        common.WANT_TO_KNOW_CHOICES[4]: common.partial(
            common.print_pros_cons,
            db_tool_interest,
            tool
        )
    }

    # Due to the use of next(iter(kwargs)),
    # for "How to install" & "Errors & fixes",
    # StopIteration will occur if kwargs is {}.
    # Thus to avoid the issue, a separate
    # dictionary is made for "How to install"
    # & "Errors & fixes" which will be merged
    # with the output dictionary if kwargs
    # is not {}
    if kwargs_not_empty:
        kwargs_first_key: str = kwargs[next(iter(kwargs))]

        to_add: dict = {
            common.WANT_TO_KNOW_CHOICES[1]: common.partial(
                print,
                db_tool_interest[kwargs_first_key]
            ),
            common.WANT_TO_KNOW_CHOICES[3]: common.partial(
                print,
                db_tool_interest[kwargs_first_key]
            )
        }

        output.update(to_add)

    output[option_selected]()


def more_queries(tool_db: dict, results: dict):
    """
    Some options user select might require user to
    answer additional questions to further filter down
    to what user wants to know

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param results: A dictionary containing what user selected
    :type results: dict
    """
    tool_selected: str = results["tool"]
    want_to_know: str = results["want_to_know"]

    learn_something_else: str = f"Learn something else about {tool_selected}"

    features_in_dict: bool = isinstance(
        tool_db[tool_selected][want_to_know],
        dict
    )

    # When there are more queries for a tool, the options for user to choose
    # from are dictionary keys. But if there aren't any more queries
    # (i.e. no dictionary), an error would occur. Thus, we need to check
    # that the extra queries are in a dictionary before proceeding
    if features_in_dict:
        more_queries_choices: list[str] = common.add_options(
            list(tool_db[tool_selected][want_to_know].keys()),
            learn_something_else
        )

        chainsaw_selected: bool = tool_selected == "Chainsaw"

        install_interest: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[1]
        use_interest: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[2]
        error_fixing_interest: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[3]

        # Ask user what platform user will be installing the tool on
        if install_interest:
            select_platform: str = common.questionary.select(
                message=f"What platform will you be installing {results['tool']} on?",
                qmark=common.QMARK,
                choices=more_queries_choices,
                use_shortcuts=True,
                show_selected=True,
                style=common.CUSTOM_STYLE
            ).ask()

            platform_selected: bool = select_platform != learn_something_else

            # Output result once a platform has been selected
            platform_selected and result_tool(
                tool_db,
                results,
                selected_platform=select_platform
            )

            return None

        # Ask user what's the error the tool is reporting
        if error_fixing_interest:
            select_error: str = common.questionary.select(
                message="What seems to be the problem?",
                qmark=common.QMARK,
                choices=more_queries_choices,
                use_jk_keys=True,
                show_selected=True,
                style=common.CUSTOM_STYLE
            ).ask()

            error_selected: bool = select_error != learn_something_else

            # Output result once an error has been selected
            error_selected and result_tool(
                tool_db,
                results,
                selected_error=select_error
            )

            return None

        # If selected tool is Chainsaw and user wants to know how to use the tool,
        # ask whether the user wants to know about Chainsaw's search feature or its
        # hunt feature
        if chainsaw_selected and use_interest:
            search_or_hunt: str = common.questionary.select(
                message="Would you like to know how to search or hunt?",
                qmark=common.QMARK,
                choices=more_queries_choices,
                use_shortcuts=True,
                show_selected=True,
                style=common.CUSTOM_STYLE
            ).ask()

            search_or_hunt_selected: bool = search_or_hunt != learn_something_else

            # Output result once search/hunt selected
            search_or_hunt_selected and result_tool(
                tool_db,
                results,
                search_or_hunt=search_or_hunt
            )

            return None

    # Print result based on user's choices
    result_tool(tool_db, results)


def back_option(
        came_from_bookmarks: bool,
        came_from_search: bool,
        last_option_is_select_another: bool,
        last_option_is_go_back_bookmarks: bool,
        last_option_is_search_something_else: bool
) -> common.Optional[str]:
    """
    Add an option in the menu to go back

    :param came_from_bookmarks:
    :param came_from_search:
    :param last_option_is_select_another:
    :param last_option_is_go_back_bookmarks:
    :param last_option_is_search_something_else:
    :return: A string that will be used for the back option
    if there's no back option already, else None
    :rtype: common.Optional[str]
    """
    back: str = ""

    # If user came from Bookmarks, check if the last option is SELECT_ANOTHER
    # or SEARCH_SOMETHING_ELSE.
    # If it is, change that option to common.GO_BACK_BOOKMARKS. Else, assign
    # common.GO_BACK_BOOKMARKS to the variable back which will will be used in
    # add_options. Same thing for when user came from Tools or Search
    if came_from_bookmarks:
        if last_option_is_select_another or last_option_is_search_something_else:
            common.WANT_TO_KNOW_CHOICES[-1] = common.GO_BACK_BOOKMARKS
        else:
            back: str = common.GO_BACK_BOOKMARKS
    elif came_from_search:
        if last_option_is_select_another or last_option_is_go_back_bookmarks:
            common.WANT_TO_KNOW_CHOICES[-1] = SEARCH_SOMETHING_ELSE
        else:
            back: str = SEARCH_SOMETHING_ELSE
    else:
        if last_option_is_go_back_bookmarks or last_option_is_search_something_else:
            common.WANT_TO_KNOW_CHOICES[-1] = SELECT_ANOTHER
        else:
            back: str = SELECT_ANOTHER

    return back


def tool_add_options(tool_bookmarked: bool, args: tuple[str]):
    """
    Add the following options to common.WANT_TO_KNOW_CHOICES:
    - An option to quickly launch the text editor for note creation
    - An option for bookmarking a tool or removing it from the bookmarks
    - An option to go back to the previous question

    :param tool_bookmarked: A boolean that determines if a tool has been
    bookmarked or not
    :type tool_bookmarked: bool
    :param args: A single string in a tuple that indicates whether
    or not user came from Bookmarks
    :type args: tuple[str]
    """
    want_to_know = common.WANT_TO_KNOW_CHOICES

    came_from_bookmarks: bool = bool(
        args) is True and args[0] == "from bookmarks"
    came_from_search: bool = bool(
        args) is True and args[0] == "from search"
    last_option_is_select_another: bool = want_to_know[-1] == SELECT_ANOTHER
    last_option_is_go_back_bookmarks: bool = want_to_know[-1] == common.GO_BACK_BOOKMARKS
    last_option_is_search_something_else: bool = want_to_know[-1] == SEARCH_SOMETHING_ELSE
    select_another_not_in_choices: bool = SELECT_ANOTHER not in want_to_know
    go_back_bookmarks_not_in_choices: bool = common.GO_BACK_BOOKMARKS not in want_to_know
    search_something_else_not_in_choices: bool = SEARCH_SOMETHING_ELSE not in want_to_know

    back: str = back_option(
        came_from_bookmarks,
        came_from_search,
        last_option_is_select_another,
        last_option_is_go_back_bookmarks,
        last_option_is_search_something_else
    )

    # Check if the tool is already bookmarked
    if tool_bookmarked:
        bookmark_or_remove: str = REMOVE_BOOKMARK
    else:
        bookmark_or_remove: str = BOOKMARK

    remove_bookmark_in_choices: bool = REMOVE_BOOKMARK in want_to_know
    bookmark_in_choices: bool = BOOKMARK in want_to_know

    # Change the text between "Remove bookmark for this tool"
    # and "Bookmark this tool" whenever user chooses that
    # option
    if remove_bookmark_in_choices or bookmark_in_choices:
        want_to_know[-2] = bookmark_or_remove

    # If neither SELECT_ANOTHER nor common.GO_BACK_BOOKMARKS are in the choices,
    # call add_options to add either one (depending on the value of
    # came_from_bookmarks), along with the option to bookmark a tool or
    # remove it (depending on the value of tool_bookmarked) and an option
    # for the user to quickly create notes
    if select_another_not_in_choices \
            and go_back_bookmarks_not_in_choices \
            and search_something_else_not_in_choices:
        common.add_options(
            want_to_know,
            "Open text editor",
            bookmark_or_remove,
            back
        )


def query_interest(tool_db: dict, tool: str, *args: str):
    """
    Ask user what he/she would like to know about the
    tool selected

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :param tool: The tool user selected
    :type tool: str
    :param args: A string indicating who called the function
    :type args: tuple[str]
    """
    # The loop is to ensure that after more_queries() is done,
    # Raziel will again ask the user what he/she would like to
    # learn about the tool, rather than asking user to select
    # another tool
    while True:
        tool_bookmarked: bool = tool_db[tool]["Bookmarked"]

        tool_add_options(tool_bookmarked, args)

        # Ask user what he/she would like to learn about the tool
        want_to_know: str = common.questionary.select(
            message=f"What would you like to know about {tool}?",
            qmark=common.QMARK,
            choices=common.WANT_TO_KNOW_CHOICES,
            use_shortcuts=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        select_another_tool: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[-1]
        bookmark: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[-2]
        open_editor: bool = want_to_know == common.WANT_TO_KNOW_CHOICES[-3]

        # Break the while loop if user selects SELECT_ANOTHER
        # and go back to query_tools() where Raziel will ask the user
        # to select a tool
        # Else move on to the next question
        if select_another_tool:
            break

        if bookmark:
            common.bookmarks.add_remove_bookmark(
                tool_db=tool_db,
                items=[tool],
                bookmark_flags=[not tool_bookmarked]
            )
        elif open_editor:
            common.notes.launch_note_editor()
        else:
            # Store user's choices in a dictionary called results
            results: dict = {
                "tool": tool,
                "want_to_know": want_to_know
            }

            # Check if the tool user selected has questions specifically
            # for that tool
            more_queries(tool_db, results)


def query_tools(tool_db: dict):
    """
    Show user a list of tools to choose from

    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    """
    # The loop is to ensure that after query_interest() is done,
    # Raziel will again ask the user to select a tool that he/she
    # might want to know, rather than taking the user back to the
    # main menu
    while True:
        # Ask user to choose a tool he/she wants to learn about
        tool: str = common.questionary.select(
            message="Please select a tool",
            qmark=common.QMARK,
            choices=common.add_options(
                list(tool_db.keys()),
                common.GO_BACK_MAIN_MENU
            ),
            use_jk_keys=True,
            show_selected=True,
            style=common.CUSTOM_STYLE
        ).ask()

        tool_chosen: bool = (tool != common.GO_BACK_MAIN_MENU) and (tool is not None)

        # Proceed to the next question only if 1st question answered
        if tool_chosen:
            query_interest(tool_db, tool)
        else:
            # Break the outer while loop if user decides to go back to main menu
            break
