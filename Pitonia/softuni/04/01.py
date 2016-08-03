import os
import sys

start_path = sys.argv[1]
file_name = sys.argv[2]

for dir_paths, dir_names, file_names in os.walk(start_path):
	if file_name in file_names:
		print(os.path.join(dir_paths, file_name))