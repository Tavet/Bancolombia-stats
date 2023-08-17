import logging
import os
import transform_to_csv
import statement


mydir = (os.getcwd()).replace('\\','/') + '/files'

def get_file_list():
    filelist=[]
    for path, _, files in os.walk(mydir):
        for file in files:
            if (file.endswith('.xlsx') or file.endswith('.xls') or file.endswith('.XLS')):
                filelist.append(os.path.join(path, file))
    number_of_files=len(filelist)
    
    logging.info("Procesando número de archivos: " + str(number_of_files))
    
    for file in filelist:
        transform_to_csv.transform_xlsx_to_csv(file)
        
    return list(map(lambda file: transform_to_csv.replace_extension(file), filelist))


def main():
    fileList = get_file_list()
    
    for file in fileList:
        info_cliente, info_general, resumen, movimientos = statement.read(file)
        #print(info_cliente)
        #print(info_general)
        #print(resumen)
        print(movimientos[2:3])


if __name__ == "__main__":
    main()

