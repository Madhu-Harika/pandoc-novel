#!/usr/bin/python

# Usage: replace-placeholders.py TEXT_FILE JSON_FILE [EXTRA_JSON_STRING]

# Takes an input TEXT_FILE and a variables (simple list of key-value pairs) JSON_FILE.
# Additional JSON key-value pairs can optionally be specified in EXTRA_JSON_STRING.
# Replaces all occurrences of variables' placeholders with their values in TEXT_FILE.

# The placeholders have the form "%key%".
# For example, given the JSON pair:	"name": "Bob",
# all occurrences of "%name%" are replaced with "Bob".

# Note: this UPDATES/OVERWRITES the input TEXT_FILE without warning!

import sys
import argparse
import json

valid_modes = ["basic", "templite", "jinja2"]

parser=argparse.ArgumentParser()
parser.add_argument('--input', '-i', help="Input text file", type= str, required=True)
parser.add_argument('--json-file', '-j', help="JSON file with placeholders and values", type= str, required=True)
parser.add_argument('--json-values', '-v', help="[optional] JSON string of additonal placeholders", type= str, default= "")
parser.add_argument('--replacement-mode', '-m', help=f"[optional] Replacement system to use: {', '.join(valid_modes)} or none (default is basic)", type= str, default= "basic")
args=parser.parse_args()

text_file_path = args.input
json_file_path = args.json_file
extra_json_string = args.json_values
placeholder_mode = args.replacement_mode

if placeholder_mode not in valid_modes:
	sys.exit(f"Invalid placeholder mode ({placeholder_mode}); should be {', '.join(valid_modes)} or none.")
elif placeholder_mode == "none":
	sys.exit(0)

try:
	# Read the text file.
	text_file = open(text_file_path, 'r')
	text_contents = text_file.read()
	text_file.close()
	
	try:
		# Read the JSON file.
		json_file = open(json_file_path, 'r')
		json_contents = json.load(json_file)
		json_file.close()
		
		# Check for extra JSON variables.
		if extra_json_string and extra_json_string != "":
			try:
				extra_json = json.loads(extra_json_string)
				json_contents.update(extra_json)
			except ValueError as e:
				print("An error occurred: %s" % e)
		
		if placeholder_mode == "basic":
			# Replace all occurrences of key placeholders in text_contents.
			for key, value in json_contents.items():
				#print(f"{key}: {value} [{type(value)}]")
				text_contents = text_contents.replace(f"%{key}%", str(value))
		
		elif placeholder_mode == "templite":
			try:
				from templite import Templite
				#t = Templite(text_contents, delimiters=["{%", "%}"])
				t = Templite(text_contents)
				text_contents = t.render(**json_contents)
			except ImportError as e:
				print("Couldn't find templite module: ", e)
				
		elif placeholder_mode == "jinja2":
			try:
				from jinja2 import Template
				template = Template(text_contents)
				text_contents = template.render(json_contents)
			except ImportError as e:
				print("Couldn't find jinja2 for python3: ", e)
		
		# Save text_file.
		try:
			text_file = open(text_file_path, 'w')
			text_file.write(text_contents)
			text_file.close()
		except IOError as e:
			print("An IOError occurred: %s" % e)
			
	except IOError:
		print("Couldn't read JSON file: " + json_file_path)
	
except IOError:
	print("Couldn't read text file: " + text_file_path)
