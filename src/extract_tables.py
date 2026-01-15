from typing import List, Dict

def extract_tables(model: Dict) -> List[Dict]:
    result = []
    for t in model["model"]["tables"]:
        result.append({
            "table_name": t["name"],
            "columns": len(t.get("columns", [])),
            "measures": len(t.get("measures", [])),
            "partitions": len(t.get("partitions", []))
        })
    return result
