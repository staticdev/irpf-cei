"""Helper to generate lists from Json."""
import json


def convert_list_to_dict(assets, key):
    """Break down into dictionary."""
    result = {}
    for asset in assets:
        codes = asset[key].split("-")
        # delete key from value
        del asset[key]
        for code in codes:
            result[code] = asset
    return result


# with open("etfs.json", "r") as json_file:
#     result = convert_list_to_dict(json.load(json_file), "Codigo")
#     print(result)

# with open("fiis.json", "r") as json_file:
#     result = convert_list_to_dict(json.load(json_file), "codigo")
#     print(result)

with open("empresas.json", "r") as json_file:
    result = convert_list_to_dict(json.load(json_file), "codigo")
    print(result)
