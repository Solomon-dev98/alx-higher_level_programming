#!/usr/bin/python3
"""Implementation of a script that adds item to a list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


command_line_args = sys.argv[1:]

try:
    args = load_from_json_file("add_item.json")
    for i in command_line_args:
        args.append(i)
    save_to_json_file(args, "add_item.json")
except FileNotFoundError:
    save_to_json_file(command_line_args, "add_item.json")
