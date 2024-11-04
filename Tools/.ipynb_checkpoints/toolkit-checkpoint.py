import pandas as pd

def procesar_datos_avocado(filepath, opcion='A'):
    # Cargar el archivo
    data_avo = pd.read_csv(filepath)
    
    # Eliminar la primera columna si es un índice exportado
    data_avo = data.drop(columns=['Unnamed: 0'])

    # Definir regiones y áreas específicas
    areas_metro_regionesgeogra = [
        "BaltimoreWashington", "BuffaloRochester", "CincinnatiDayton", "DallasFtWorth", "GreatLakes",
        "HarrisburgScranton", "HartfordSpringfield", "MiamiFtLauderdale", "Midsouth", "NewOrleansMobile",
        "Northeast", "NorthernNewEngland", "PhoenixTucson", "Plains", "RaleighGreensboro", 
        "RichmondNorfolk", "SouthCentral", "Southeast", "West", "WestTexNewMexico"
    ]

    regiones_geograficas = ["California", "GreatLakes", "Midsouth", "Northeast", "Plains", "SouthCentral", "Southeast", "West"]

    # Filtrar los datos según la opción seleccionada
    if opcion.upper() == 'A':
        filtro = data_avo['region'].isin([
            "TotalUS", "GreatLakes", "Midsouth", "Northeast", "NorthernNewEngland",
            "Plains", "SouthCentral", "Southeast", "West", "WestTexNewMexico"
        ])
        data_avo = data_avo[~filtro]
    elif opcion.upper() == 'B':
        data_avo = data_avo[data_avo['region'].isin(regiones_geograficas)]
    else:
        raise ValueError("Opción no válida. Por favor, elige 'A' o 'B'.")

    return data_avo
