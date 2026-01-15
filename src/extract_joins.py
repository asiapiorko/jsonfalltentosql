from typing import List, Dict

def extract_joins(sources: List[Dict]) -> List[Dict]:
    joins = []
    for s in sources:
        expr = s["expression"]
        if "Table.NestedJoin" in expr or "LOOKUPVALUE" in expr:
            joins.append({
                "table": s["table"],
                "join_type": (
                    "M_JOIN" if "Table.NestedJoin" in expr else "DAX_LOOKUP"
                ),
                "expression": expr
            })
    return joins
