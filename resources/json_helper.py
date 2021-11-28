"""Helper to generate lists from Json."""
import json


def convert_list_to_dict(assets, key, value_key):
    """Break down into dictionary."""
    result = {}
    for asset in assets:
        codes = asset[key].split("-")
        for code in codes:
            result[code] = asset[value_key]
    return result


# with open("etfs.json", "r") as json_file:
#     result = convert_list_to_dict(json.load(json_file), "Codigo", "Cnpj")
#     print(result)

# with open("fiis.json", "r") as json_file:
#     result = convert_list_to_dict(json.load(json_file), "codigo", "cnpj")
#     print(result)

# with open("empresas.json", "r") as json_file:
#     result = convert_list_to_dict(json.load(json_file), "codigo", "cnpj")
#     print(result)

with open("corretoras.json") as json_file:
    result = convert_list_to_dict(json.load(json_file), "CodB3", "Cnpj")
    print(len(result))
    print(result)
