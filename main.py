import logging
import os
import transformer
import statement
import sys

mydir = (os.getcwd()).replace('\\','/') + '/files'

logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_file_list():
    filelist=[]
    for path, _, files in os.walk(mydir):
        for file in files:
            if (file.endswith('.xlsx') or file.endswith('.xls') or file.endswith('.XLS')):
                filelist.append(os.path.join(path, file))
    number_of_files=len(filelist)
    logger.info("*******************************************************")
    logger.info("Procesando número de archivos: " + str(number_of_files))
    
    for file in filelist:
        transformer.transform_xlsx_to_csv(file)
        
    return list(map(lambda file: transformer.replace_extension(file), filelist))


def main():
    fileList = get_file_list()
    total = 0
    argument_string = sys.argv[1]
    print("Procesando datos para: " + argument_string)
    for file in fileList:
        info_cliente, info_general, resumen, movimientos = statement.read(file)
        logger.info("* Obteniendo información del archivo: " + file)
        total += abs(get_total_for(movimientos, argument_string))
        
    logger.info("TOTAL: " + str(total) + "\n\n\n")
    

# Gets the total sum for a given description that matches the movements
def get_total_for(movimientos, descripcion):
    movimientos = movimientos.copy()
    movimientos = movimientos[movimientos['DESCRIPCIÓN'].str.contains(descripcion) == True]
    
    movimientos['VALOR'] = movimientos['VALOR'].str.replace(',', '').astype(float).astype(int)
    if not movimientos.empty:
        movimientos['FECHA'] = movimientos['FECHA'].apply(transformer.map_date_to_spanish_month)
        logger.info("* Obteniendo valores para la transacción: " + str((movimientos['DESCRIPCIÓN'].unique())[0]))
        logger.info(str(movimientos[['FECHA', 'VALOR']].to_string(index=False)))
    else:
        logger.error("Este archivo no tiene datos para la transacción indicada")
        
    logger.info("\n")
    return movimientos['VALOR'].sum()

    

if __name__ == "__main__":
    main()
