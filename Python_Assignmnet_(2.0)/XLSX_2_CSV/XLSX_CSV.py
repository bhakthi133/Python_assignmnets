import pandas as pd
excel_url = f"https://docs.google.com/spreadsheets/d/1RVJ4qI90FGvuwkknh3LCEc5gAPXaacaJm_iuetYPeBg/export?format=xlsx"
sheets_df = pd.read_excel(excel_url, sheet_name=None)
for sheet, df in sheets_df.items():
    df.to_csv(f"CSV_files/{sheet}1.csv", index=False)
    print(f"{sheet} created")