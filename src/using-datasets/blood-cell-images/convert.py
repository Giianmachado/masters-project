import xmltodict
import json
import os

# declare path to xml files
path = os.path.abspath('dataset/annotations')


# read file contents
def file_get_contents(filename):
    with open(filename) as f:
        return f.read()


# read files
def read_files_and_convert():
    # declare obj
    items = {}
    for filename in os.listdir(path):
        # get file content
        content = file_get_contents(os.path.join(path, filename))
        # convert content
        result = xmltodict.parse(content)
        # set value with key
        items[filename] = result
    # result items
    return items


# read files and convert
json_content = read_files_and_convert()
# format json
formatted_json = json.dumps(json_content, indent=2, sort_keys=True)
# create file
f = open("annotations.json", "w")
# write file
f.write(formatted_json)
# close file
f.close()
