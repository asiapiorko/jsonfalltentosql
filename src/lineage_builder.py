import pandas as pd

def build_lineage(tables, sources, joins):
    df_tables = pd.DataFrame(tables)
    df_sources = pd.DataFrame(sources)
    df_joins = pd.DataFrame(joins)

    lineage = df_sources.merge(df_tables, on="table", how="left")
    return lineage
