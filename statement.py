import pandas as pd
import io


def read(file_path):
    # Read all lines to get the sections
    with open(file_path, 'r') as file:
        lines = file.readlines()

    tables = {
        'Información Cliente': [],
        'Información General': [],
        'Resumen': [],
        'Movimientos': []
    }
    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith('Información Cliente'):
            current_section = 'Información Cliente'
        elif line.startswith('Información General'):
            current_section = 'Información General'
        elif line.startswith('Resumen'):
            current_section = 'Resumen'
        elif line.startswith('Movimientos'):
            current_section = 'Movimientos'
        elif current_section:
            tables[current_section].append(line)

    # Convert each section back to a CSV-like string and read it into a DataFrame
    info_cliente = pd.read_csv(io.StringIO('\n'.join(tables['Información Cliente'][1:])))
    info_general = pd.read_csv(io.StringIO('\n'.join(tables['Información General'][1:])))
    resumen = pd.read_csv(io.StringIO('\n'.join(tables['Resumen'][1:])))
    movimientos = pd.read_csv(io.StringIO('\n'.join(tables['Movimientos'][1:])))

    return info_cliente, info_general, resumen, movimientos