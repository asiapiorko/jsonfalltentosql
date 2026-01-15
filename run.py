import pandas as pd
from src.load_json import load_json
from src.flatten_json import flatten_json
from src.extract_tables import extract_tables
from src.extract_sources import extract_sources
from src.extract_joins import extract_joins
from src.lineage_builder import build_lineage

model = load_json("data/model.bim")

tables = extract_tables(model)
sources = extract_sources(model)
joins = extract_joins(sources)

lineage = build_lineage(tables, sources, joins)

pd.DataFrame(tables).to_csv("outputs/tables.csv", index=False)
pd.DataFrame(sources).to_csv("outputs/sources.csv", index=False)
pd.DataFrame(joins).to_csv("outputs/joins.csv", index=False)
lineage.to_csv("outputs/lineage.csv", index=False)

print("Lineage extraction completed.")
