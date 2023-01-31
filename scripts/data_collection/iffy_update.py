"""
Purpose:
    Update the existing Iffy news list of low-credibility domains with the latest.
    Iffy News Ref: https://iffy.news/
    File Ref: https://iffynews.page.link/sheet

Inputs:
    Full path to the existing iffy news file. See argparse function below.

Outputs:
    Overwrites the previous iffy news file.

Authors: Nick Liu & Matthew DeVerna
"""
import argparse
import os
import sys

import pandas as pd
from urllib import request

from top_fibers_pkg.utils import get_logger

REPO_ROOT = "/home/data/apps/topfibers/repo"
LOG_DIR = "./logs"
LOG_FNAME = "iffy_update.log"
SCRIPT_PURPOSE = "Update the Iffy News list of low-credibility domains."


def parse_cl_args(script_purpose="", logger=None):
    """
    Read command line arguments listed below.

    Parameters:
    --------------
    - script_purpose (str) : Purpose of the script being utilized. When printing
        script help message via `python script.py -h`, this will represent the
        script's description. Default = "" (an empty string)
    - logger : logging object

    Returns
    --------------
    None

    Exceptions
    --------------
    None
    """
    logger.info("Parsing command line arguments...")

    # Initiate the parser
    parser = argparse.ArgumentParser(description=script_purpose)

    # Add long and short argument
    parser.add_argument(
        "-f",
        "--file",
        metavar="Iffy File",
        help="Full path to the iffy news file",
        required=True,
    )

    # Read parsed arguments from the command line into "args"
    args = parser.parse_args()

    return args


def get_iffy():
    """grab the latest version of iffy list and save to local"""
    url = "https://iffynews.page.link/sheet"
    sheet_name = "Iffy-news"
    try:
        response = request.urlopen(url)
        new_url = response.geturl()
        sheet_id = new_url.split("/")[-2]
        google_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df = pd.read_csv(google_url)
        list_of_url = [f"{url}*\n" for url in df.URL.tolist()]
    except Exception as e:
        logger.exception(f"Problem getting the new iffy list!\n\n{e}")
    return list_of_url


if __name__ == "__main__":
    if not (os.getcwd() == REPO_ROOT):
        sys.exit(
            "ALL SCRIPTS MUST BE RUN FROM THE REPO ROOT!!\n"
            f"\tCurrent directory: {os.getcwd()}\n"
            f"\tRepo root        : {REPO_ROOT}\n"
        )
    script_name = os.path.basename(__file__)
    logger = get_logger(LOG_DIR, LOG_FNAME, script_name=script_name, also_print=True)
    logger.info("-" * 50)
    logger.info(f"Begin script: {__file__}")

    # Parse input flags
    args = parse_cl_args(SCRIPT_PURPOSE, logger)
    iffy_file = args.file

    new_iffy = get_iffy()
    with open(iffy_file, "w+") as outfile:
        outfile.writelines(new_iffy)
