# Remove first docstring in all the .py files
# This leading docstring is huge and not usefull in a bundled package
import os

root_dir = 'zuora_client'  # Calling directory
for dir_name, sub_dir_list, file_list in os.walk(root_dir):
    for file_name in file_list:
        if not file_name.endswith('.py'):
            # Only consider python files
            continue

        print(f'{dir_name} - {file_name}')
        data = open(os.path.join(dir_name, file_name), 'r').read()
        if data.count('\n"""') < 2:
            # Not enough instances of docstring quotes
            continue
        start_index = data.find('\n"""')
        end_index = data.find('\n"""', start_index+1)
        with open(os.path.join(dir_name, file_name), 'w') as fh:
            fh.write(data[:start_index])
            fh.write('\n')
            fh.write(data[end_index+4:])
