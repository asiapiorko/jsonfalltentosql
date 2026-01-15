from typing import List, Dict

def extract_sources(model: Dict) -> List[Dict]:
    rows = []
    for t in model["model"]["tables"]:
        for p in t.get("partitions", []):
            src = p.get("source", {})
            rows.append({
                "table": t["name"],
                "partition": p.get("name"),
                "source_type": src.get("type"),
                "expression": " | ".join(src.get("expression", []))
            })
    return rows
