import os
import re
from dotenv import load_dotenv

load_dotenv()

PATTERN = re.compile(r".+XMLRECORD\['(.+)'\].*\s(\w+),?")


def print_result(match):
    group1, group2 = match.group(1), match.group(2)
    print(f"DATA.XMLRECORD[{group1}] {group2}")
    print(f"XMLRECORD['{group1}'] = {group1 in FIELD_NAMES}")
    print(f"FIELD['{group2}'] = {group2 in FIELD_NAMES}\n")


def apply_regex(input_string):
    matches = PATTERN.match(input_string)
    if matches:
        print_result(matches)
    else:
        print("Match failed.\n")


def check_stream_field_in_schema(field_names):
    global FIELD_NAMES
    FIELD_NAMES = field_names

    with open(os.getenv("STREAM_FIELDS_FILE_PATH"), "r") as file:
        STREAM_FIELDS = [
            item.split("--")[0].strip() for item in file.read().split("\n")
        ]

    for stream_fields in STREAM_FIELDS:
        apply_regex(stream_fields)
