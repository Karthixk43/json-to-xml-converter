import json
import xmltodict

def convert_bools(obj):
    if isinstance(obj, dict):
        return {k: convert_bools(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_bools(i) for i in obj]
    elif isinstance(obj, bool):
        return str(obj).lower()
    else:
        return obj

def flatten_single_dict_lists(obj):
    if isinstance(obj, dict):
        return {k: flatten_single_dict_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # If the list contains only one dict, replace the list with the dict
        if len(obj) == 1 and isinstance(obj[0], dict):
            return flatten_single_dict_lists(obj[0])
        else:
            return [flatten_single_dict_lists(i) for i in obj]
    else:
        return obj

try:
    print("Reading JSON file...")
    with open("example_input.json") as f:
        json_data = json.load(f)
    print("JSON loaded successfully.")

    # Convert booleans to lowercase strings for XML compatibility
    json_data = convert_bools(json_data)
    # Flatten single-dict lists for better XML output
    json_data = flatten_single_dict_lists(json_data)

    print("Converting to XML...")
    xml_str = xmltodict.unparse({"root": json_data}, pretty=True)
    print("Conversion successful.")

    print("Writing to output.xml...")
    with open("output.xml", "w") as f:
        f.write(xml_str)
    print("Conversion complete! Check output.xml")
except Exception as e:
    print(f"Error: {e}")