import pandas as pd

spanish_months = {
    1: 'Enero',
    2: 'Febrero',
    3: 'Marzo',
    4: 'Abril',
    5: 'Mayo',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'Noviembre',
    12: 'Diciembre',
}

def map_date_to_spanish_month(date_str):
    day, month = map(int, date_str.split('/'))
    return f"{day}/{spanish_months[month]}"

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