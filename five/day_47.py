#!/usr/bin/env python3
#
# Day 47: Save a JSON
import json

def save_json(names: dict):
    with open('names.json', 'w') as f:
        json.dump(names, f, indent=4)
    return "Names saved to 'names.json'"


def read_json():
    with open('names.json', 'r') as f:
        data = json.loads(f.read())
    return data