"""This module prints information about the chosen tool"""

############################
# STANDARD LIBRARY IMPORTS #
############################
from datetime import datetime
from typing import Iterator, Union

###############################
# RELATED THIRD PARTY IMPORTS #
###############################
from dateutil.tz import tzutc
from lastversion import latest
from lastversion.Version import Version
from lastversion.utils import BadProjectError

##############################################
# LOCAL APPLICATION/LIBRARY SPECIFIC IMPORTS #
##############################################
import common


#############
# FUNCTIONS #
#############
def update_latest_stable_release(
        lsr_info: dict,
        latest_version: Version,
        latest_release_date: datetime
) -> common.Optional[str]:
    """
    Update the latest version and/or latest release date in tool_db
    (tool_database.json) if run_lastversion() managed to get the latest
    version and/or release date and the version/date found is not
    the same as the one in tool_db

    :param lsr_info: A dictionary (from tool_database.json)
    containing the currently, possibly outdated,
    latest version and latest release date of the
    specified tool
    :type lsr_info: dict
    :param latest_version: The latest version found by lastversion
    :type latest_version: Version
    :param latest_release_date: The latest release date found by
    lastversion
    :type latest_release_date: datetime
    :return: The latest release date as a string in the format
    "%d %b %Y
    """
    have_version: bool = latest_version is not None
    have_release_date: bool = latest_release_date is not None

    different_version: bool = latest_version != lsr_info["version"]

    # Update the latest version in tool_db (tool_database.json) if
    # lastversion managed to get the latest version and it's
    # different from the one we currently have in tool_database.json
    if have_version and different_version:
        lsr_info["version"]: str = latest_version

    # Check if lastversion managed to get the latest release date
    # before proceeding
    if have_release_date:
        db_have_release_date: bool = lsr_info["release_date"] is not None

        newer: bool = False

        # We need to ensure the date we get is not before the date
        # we currently have, so before proceeding, we first check
        # to see if tool_database.json has "release_date" set
        # (i.e. not None)
        if db_have_release_date:
            # If there is a date set, convert it from a str to
            # a datetime so that it can be compared
            db_release_date: datetime = datetime.strptime(
                lsr_info["release_date"], "%d %b %Y"
            ).replace(tzinfo=tzutc())

            # Check that the latest release date lastversion got
            # is after the one in tool_database.json
            newer: bool = latest_release_date > db_release_date

        # If the lastversion's date is newer or release_date is
        # None, convert lastversion's date to the format
        # "%d %b %Y" and update release_date with that value
        if newer or not db_have_release_date:
            # Convert latest_release_date to a more readable
            # format
            latest_release_date: str = datetime.strftime(
                latest_release_date,
                "%d %b %Y"
            )

            lsr_info["release_date"]: str = latest_release_date

        return latest_release_date

    return None


def run_lastversion(lsr_info: dict, site: str) -> Union[
    tuple[None, None],
    tuple[Version, str],
    tuple[Version, None],
    tuple[None, str],
]:
    """
    Run the 3rd party library lastversion to possibly get
    info about the latest stable release of a tool

    :param lsr_info: A dictionary (from tool_database.json)
    containing the currently, possibly outdated,
    latest version and latest release date of the
    specified tool
    :type lsr_info: dict
    :param site: The repository/official site of the tool
    you are trying to get info about
    :type site: str
    :return: The latest version and/or latest release date
    found by lastversion, else None for whichever it
    couldn't get
    :rtype: Union[
                tuple[None, None],
                tuple[Version, str],
                tuple[Version, None],
                tuple[None, str]
            ]
    """
    # Try to run lastversion to get a dictionary containing info
    # related to the latest stable release of a tool
    try:
        latest_release: Version = latest(
            repo=site,
            output_format="dict",
            pre_ok=False
        )

    # Some sites might cause lastversion to throw an error
    # So to avoid this, we just return None, None
    except (BadProjectError, common.json.JSONDecodeError):
        return None, None

    # If no errors thrown, we first make sure that
    # latest_release is not None. If it's not, we
    # assign latest_version to the latest version
    # found by lastversion, and latest_release_date
    # to the latest release date found by lastversion
    else:
        have_release: bool = latest_release is not None

        if have_release:
            has_version_key: bool = "version" in latest_release
            has_tag_date_key: bool = "tag_date" in latest_release

            latest_version: Version = latest_release["version"] if has_version_key else None
            latest_release_date: datetime = latest_release["tag_date"] if has_tag_date_key else None

            # Update the latest stable release info in
            # tool_db (tool_database.json) which will be used in
            # print_about()
            latest_release_date: str = update_latest_stable_release(
                lsr_info,
                latest_version,
                latest_release_date
            )

            return latest_version, latest_release_date

        return None, None


def get_latest_release_from_repository_sites(about_tool: dict) -> Union[
    tuple[None, None],
    tuple[Version, str],
    tuple[Version, None],
    tuple[None, str]
]:
    """
    Get the latest version and release date of a tool from
    repository sites

    :param about_tool: A dictionary containing all the
    info about tool_selected
    :type about_tool: dict
    :return: The latest version and/or latest release date
    found by lastversion, else None for whichever it
    couldn't get
    :rtype: Union[
        tuple[None, None],
        tuple[Version, str],
        tuple[Version, None],
        tuple[None, str]
    ]
    """
    # An iterator with repository sites supported by lastversion
    # We need to use an iterator due to next()
    repository_sites: Iterator[str] = iter(
        (
            "Github",
            "SourceForge",
            "Gitlab",
            "BitBucket",
            "PyPI"
        )
    )

    # Find the first site in repository_sites that matches
    # a key in the about_tool dictionary
    first_site_matched: common.Optional[str] = next(
        (
            site for site in repository_sites
            if site in about_tool.keys()
        ), None
    )

    have_match: bool = first_site_matched is not None

    # Run lastversion if a repository site was matched
    # to get the latest version and the latest release
    # date of the tool
    if have_match:
        latest_version: Version
        latest_release_date: str
        latest_version, latest_release_date = run_lastversion(
            about_tool[common.LATEST_STABLE_RELEASE],
            about_tool[first_site_matched]
        )

        return latest_version, latest_release_date

    return None, None


def get_latest_release(about_tool: dict):
    """
    Get the latest version and/or latest release date of a tool.
    By default, the latest version and its release date should be
    in tool_database.json already, but there's a possibility that those
    values may be outdated, so we need to get the latest values
    online.
    We first try to get the values from the following repository
    sites:
    - Github
    - SourceForge
    - Gitlab
    - BitBucket
    - PyPI
    If we can't get the values (i.e. None returned), we then try
    to get the values from the tool's official website.
    Finally, if that doesn't work as well, we'll just go with
    whatever values are in tool_database.json.

    :param about_tool: A dictionary containing all the info
    about tool_selected
    :type about_tool: dict
    """
    # Try and get the latest version & release date of a tool
    # from the following repository sites:
    # - Github
    # - SourceForge
    # - Gitlab
    # - BitBucket
    # - PyPI
    latest_version: Version
    latest_release_date: str
    latest_version, latest_release_date = get_latest_release_from_repository_sites(
        about_tool
    )

    no_version: bool = latest_version is None
    no_release_date: bool = latest_release_date is None

    # If latest_version/latest_release_date is None, try getting the
    # latest version and/or release date from the tool's official site instead
    if no_version or no_release_date:
        run_lastversion(
            about_tool[common.LATEST_STABLE_RELEASE],
            about_tool["Official site"]
        )


def print_about(raziel_db_tool: dict, tool_selected: str):
    """
    Print every info about a tool

    :param raziel_db_tool: A dictionary containing the keys
    and values of tool_selected in tool_database.json
    :type raziel_db_tool: dict
    :param tool_selected: The tool user selected
    :type tool_selected: str
    """
    about_tool: dict = raziel_db_tool["About"]
    supported_platforms: dict = raziel_db_tool["How to install"].keys()

    # Get a tool's latest version & release date
    get_latest_release(about_tool)

    lsr_info: dict = about_tool[common.LATEST_STABLE_RELEASE]
    latest_version: str = lsr_info["version"]
    latest_release_date: str = lsr_info["release_date"]

    no_version: bool = latest_version is None
    no_latest_release_date: bool = latest_release_date is None
    only_have_latest_release_date: bool = no_version and not no_latest_release_date

    if no_version:
        latest_version: str = "Version not found"

    if no_latest_release_date:
        latest_release_date: str = "Release date not found"

    # Print tool's name
    print(f"Name:\n{tool_selected}\n")

    # Print every value in about_tool
    key: str
    for key in about_tool.keys():
        if key == common.LATEST_STABLE_RELEASE:
            print(
                f"Supported platform(s):\n{', '.join(supported_platforms)}\n"
            )

            if only_have_latest_release_date:
                print(
                    f"Latest release date:\n{latest_release_date}\n"
                )
            else:
                print(
                    f"{key}:\n{latest_version} ({latest_release_date})\n"
                )
        elif key == "Useful for":
            print(
                "{0}:\n\u2022 {1}\n".format(
                    key, "\n\u2022 ".join(about_tool[key])
                )
            )
        else:
            print(f"{key}:\n{about_tool[key]}\n")
