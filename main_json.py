import os
import json
from dotenv import load_dotenv
from utils import check_stream_field_in_schema

load_dotenv()

with open(os.getenv("SCHEMA_FILE_PATH"), "r") as file:
    check_stream_field_in_schema([field["name"] for field in json.load(file)["fields"]])
