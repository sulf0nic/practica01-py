import pandas as pd

excelData = pd.read_excel("\Users\ricardo-arenas\Documents\ebc-python\practica01-py\sample-xls-file-for-testing.xls")
dataFrame = pd.DataFrame(excelData)
print(dataFrame.head())