import os
from dotenv import load_dotenv
from utils import check_stream_field_in_schema

load_dotenv()

with open(os.getenv("STANDARD_SELECTION_MANUAL_COLUMN_TABLE"), "r") as file:
    check_stream_field_in_schema(file.read().replace(".", "_").split("\n"))
