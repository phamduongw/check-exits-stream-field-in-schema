from utils import check_stream_field_in_schema

with open("standard_selection_manual_column_table.txt", "r") as file:
    check_stream_field_in_schema(file.read().replace(".", "_").split("\n"))
