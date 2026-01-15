from typing import Any, Dict

def flatten_json(data: Dict[str, Any], parent_key="", sep=".") -> Dict[str, Any]:
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, (dict, list)):
                    items.update(flatten_json(item, f"{new_key}[{i}]", sep))
                else:
                    items[f"{new_key}[{i}]"] = item
        else:
            items[new_key] = v
    return items
