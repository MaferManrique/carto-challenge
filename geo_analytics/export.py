import pandas as pd

def generate_map_csv(df: pd.DataFrame, output_path: str):
    """
    Export DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame to export.
        output_path (str): The path to save the CSV file.
        delimiter (str, optional): The delimiter to use (default is ',').

    Raises:
        ValueError: If the DataFrame is empty or output_path is invalid.
    """
    if df.empty:
        raise ValueError("DataFrame is empty.")
    
    if not output_path:
        raise ValueError("Invalid output path.")

    df[['poi_id', 'lon', 'lat', 'cluster_id']].to_csv(output_path, index=False)