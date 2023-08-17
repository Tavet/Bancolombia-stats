import pandas as pd

def transform_xlsx_to_csv(file_path):
    read_file = pd.read_excel(file_path)
    read_file.to_csv (replace_extension(file_path), 
                  index = None,
                  header=True)
    
    
def replace_extension(file_path):
    if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return file_path.rsplit('.', 1)[0] + '.csv'
    else:
        return file_path