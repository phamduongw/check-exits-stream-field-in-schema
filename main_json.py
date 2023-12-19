import json
from utils import check_stream_field_in_schema

with open("schema.json", "r") as file:
    check_stream_field_in_schema([field["name"] for field in json.load(file)["fields"]])
