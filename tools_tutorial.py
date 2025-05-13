"""
This module prints out how to use a particular feature of
the tool user selected/specified or the overall tool itself
"""


def print_how_to_use(how_to_use: dict, *args: tuple):
    """
    Print how to use a particular feature of
    the selected tool or the tool in general

    :param how_to_use: A dictionary containing
    the keys & values in the "How to use" dictionary
    in tool_db (tool_database.json)
    :type how_to_use: dict
    :param args: A tuple containing a dictionary
    of the feature the user would like to learn
    :type args: tuple
    """
    dict_not_empty: bool = bool(args[0]) is True

    # Check that the dictionary in args isn't empty
    # so it doesn't get StopIteration thrown due to
    # next(iter(args[0]))
    if dict_not_empty:
        feature: str = args[0][next(iter(args[0]))]
        how_to_use_feature: dict = how_to_use[feature]

        have_info: bool = "extra_info" in how_to_use_feature \
                          and how_to_use_feature["extra_info"] is not None

        have_example: bool = "examples" in how_to_use_feature \
                             and how_to_use_feature["examples"] is not None

        # Print how to use the feature of the tool
        print(f"{how_to_use_feature['help']}\n")

        # Print the examples for that feature if have_example is True
        if have_example:
            print(f"{'=' * 8}\nEXAMPLES\n{'=' * 8}")
            [
                print(f"{key}:\n{value}\n")
                for key, value in how_to_use_feature['examples'].items()
            ]

        # If have_info is True, print the extra info
        have_info and print(f"{how_to_use_feature['extra_info']}\n")
    else:
        # Print how to use the tool if args[0] is {}
        print(how_to_use)
