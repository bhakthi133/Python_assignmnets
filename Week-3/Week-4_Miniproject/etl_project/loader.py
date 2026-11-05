
import os
import pandas as pd


def save_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")

    except PermissionError:
        print("Error: Permission denied while saving the file.")

    except Exception as e:
        print(f"Unexpected error: {e}")
