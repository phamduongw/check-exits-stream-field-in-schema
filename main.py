import os
import re
import json
from dotenv import load_dotenv

load_dotenv()

STREAM_FIELDS_FILE_PATH = os.getenv("STREAM_FIELDS_FILE_PATH")
SCHEMA_FILE_PATH = os.getenv("SCHEMA_FILE_PATH")
PATTERN = re.compile(r".+XMLRECORD\['(.+)'\].*\s(\w+),?")


with open(STREAM_FIELDS_FILE_PATH, "r") as file:
    STREAM_FIELDS = [item.split("--")[0].strip() for item in file.read().split("\n")]

with open(SCHEMA_FILE_PATH, "r") as file:
    FIELD_NAMES = [field["name"] for field in json.load(file)["fields"]]


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


for stream_fields in STREAM_FIELDS:
    apply_regex(stream_fields)
