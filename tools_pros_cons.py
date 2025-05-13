"""This module prints the pros and/or cons of the tool chosen"""


def print_pros_cons(tool_db_pros_cons: dict, tool: str, pros_or_cons: str = "Both"):
    """
    Print the pros and/or cons of the tool selected

    :param tool_db_pros_cons: tool_db[tool]["Pros & Cons"]
    Stores the pros and cons of the specified tool in a dictionary
    taken from tool_database.json
    :type tool_db_pros_cons: dict
    :param tool: The tool selected
    :type tool: str
    :param pros_or_cons: Whether user wants to see the tool's
    pros and/or cons, defaults to "Both"
    :type pros_or_cons: str
    """
    if pros_or_cons == "Both":
        pros_or_cons: tuple = ("Pros", "Cons")

    # Print the pros and/or cons of the tool
    [
        print(
            "{0} of {1}:\n\u2022 {2}\n".format(
                key,
                tool,
                "\n\u2022 ".join(
                    tool_db_pros_cons[key]
                )
            )
        ) for key in tool_db_pros_cons.keys()
        if key in pros_or_cons
    ]
