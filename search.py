"""
This module allows users to quickly search for
information like how to perform a particular task.
It even allows user to run shell commands without
the need to remember the syntax
"""
############################
# STANDARD LIBRARY IMPORTS #
############################
import copy
import platform
import shlex
import subprocess

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common


#############
# FUNCTIONS #
#############
def run_cmd(search_result: dict):
    """
    Run a shell command

    :param search_result: A dictionary whose name is the same as
    what user selected in the search autocomplete box
    :type search_result: dict
    """
    # Get the user's OS so that when executing a
    # platform-specific command, Raziel will use the
    # command for that platform
    user_os: str = platform.system().capitalize()

    platform_specific_cmd: bool = user_os in search_result

    find_at: str = search_result[user_os]["value"] \
        if platform_specific_cmd \
        else search_result["value"]

    # Look for possible parameters (denoted as: <parameter>)
    # which would require user input
    args: list[str] = common.re.findall(
        r"<\w*>",
        find_at
    )

    # If parameters are found, loop through args, asking
    # user for input and subbing the parameter with what
    # user entered
    if args:
        for arg in args:
            if search_result[arg]["asking_for_path"]:
                user_input: str = common.questionary.path(
                    message=search_result[arg]["message"],
                    qmark=common.QMARK
                ).ask()
            else:
                user_input: str = common.questionary.text(
                    message=search_result[arg]["message"],
                    qmark=common.QMARK
                ).ask()

            find_at: str = common.re.sub(
                arg,
                user_input,
                find_at
            )

        to_run: list = shlex.split(find_at)
    else:
        to_run: str = find_at

    # Execute the command
    subprocess.run(
        to_run,
        shell=False,
        check=True
    )


def query_search(search_db: dict, tool_db: dict):
    """
    Allow user to quickly search for information
    he/she might need

    :param search_db: search_database.json stored as a dictionary
    :type search_db: dict
    :param tool_db: tool_database.json stored as a dictionary
    :type tool_db: dict
    :return:
    """
    while True:
        # Get user input
        query: str = common.questionary.autocomplete(
            message="Search (Enter exit/back to get out):\n",
            qmark=common.QMARK,
            choices=list(search_db.keys()),
            ignore_case=True,
            match_middle=True,
            style=common.CUSTOM_STYLE
        ).ask()

        # Duplicate search_db but with its keys lowered
        # This will be used to check against query.lower()
        golden_lowercase_search_db: dict = {
            key.lower(): value
            for key, value in search_db.items()
        }

        # Create a deep copy of golden_lowercase_search_db which will be
        # used if what user search for is a shell command. This is done
        # so that whatever changes happen to silver_lowercase_search_db
        # will not affect the golden_lowercase_search_db
        silver_lowercase_search_db: dict = copy.deepcopy(
            golden_lowercase_search_db
        )

        exit_search_entered: bool = query.lower() in ("back", "exit")
        query_found: bool = query.lower() in golden_lowercase_search_db.keys()
        info_category: bool = query_found and golden_lowercase_search_db[
            query.lower()
        ]["category"] == "info"
        cmd_category: bool = query_found and golden_lowercase_search_db[
            query.lower()
        ]["category"] == "command"
        tool_category: bool = query_found and golden_lowercase_search_db[
            query.lower()
        ]["category"] == "tools"

        if exit_search_entered:
            break

        if info_category:
            print(f"\n{golden_lowercase_search_db[query.lower()]['value']}\n")
        elif cmd_category:
            run_cmd(silver_lowercase_search_db[query.lower()])
        elif tool_category:
            common.tools.query_interest(
                tool_db,
                golden_lowercase_search_db[query.lower()]["value"],
                "from search"
            )
        else:
            print(f"\nSorry, but I can't find anything on \"{query}\"\n")
