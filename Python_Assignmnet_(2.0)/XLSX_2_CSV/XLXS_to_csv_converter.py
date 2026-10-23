
import pandas as pd
file_path=r"C:\Users\Admin\Desktop\Practice&assignmnet foler\Assignmnet_questions_solution\Python_assignmnets\Python_Assignmnet_(2.0)\XLSX_2_CSV\test.xlsx"
sheets_df=pd.read_excel(file_path,sheet_name=None)
for sheet,df in sheets_df.items():
    df.to_csv(f"CSV_files/{sheet}.csv",index=False)
    print(f"{sheet} cretaed")
