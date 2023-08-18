# Bancolombia-stats
In this project you can find the total value for a transaction in a Bancolombia statement .xlsx or .xls file (generated in the Sucursal Virtual Personas). This is useful to find the total sum of the specified transaction description through multiple files.

1. Insert the .xls or .xlsx (excel file) into files
2. Run the script ```python main.py "transaction description"```and add a partial description of the transaction to look up for it. For example ```python main.py "Empresas Publicas de"```
3. Check the output in the generated file logs.log


Output example for ```python main.py "Tarjeta Civica"```


``` 
*******************************************************
Procesando número de archivos: 4
* Obteniendo información del archivo: /Users/breynerrojas/Documents/Personal/tavet/bancolombia-stats/files/extracto_202209_cuenta_de_ahorros_4401.csv
* Obteniendo valores para la transacción: Recarga de Tarjeta C¡vica
   FECHA  VALOR
10/Julio -25000


* Obteniendo información del archivo: /Users/breynerrojas/Documents/Personal/tavet/bancolombia-stats/files/extracto_202206_cuenta_de_ahorros_4401.csv
* Obteniendo valores para la transacción: Recarga de Tarjeta C¡vica
   FECHA  VALOR
29/Junio -20000


* Obteniendo información del archivo: /Users/breynerrojas/Documents/Personal/tavet/bancolombia-stats/files/extracto_202203_cuenta_de_ahorros_4401.csv
Este archivo no tiene datos para la transacción indicada


* Obteniendo información del archivo: /Users/breynerrojas/Documents/Personal/tavet/bancolombia-stats/files/extracto_202212_cuenta_de_ahorros_4401.csv
* Obteniendo valores para la transacción: Recarga de Tarjeta C¡vica
      FECHA  VALOR
9/Noviembre -20000
9/Noviembre  -1000


TOTAL: 66000
```