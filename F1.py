# %%
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
import requests
from io import StringIO
from datetime import datetime

# %%

headers = {"User-Agent": "Mozilla/5.0"}
base_url = "https://www.formula1.com/en/results/{}/races"

now = datetime.now()
last_year = now.year if now.month >= 3 else now.year - 1

dfs = []

for year in range(1950, last_year + 1):
    url = base_url.format(year)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        continue
    try:
        df = pd.read_html(StringIO(r.text))[0]
        df["Year"] = year
        df["Grand Prix"] = df["Grand Prix"].str.replace(r"Flag of .*?", "", regex=True)
        dfs.append(df)
    except ValueError:
        continue

f1_races = pd.concat(dfs, ignore_index=True)


# Guardar en Excel con hoja llamada 'Teams'
with pd.ExcelWriter("F1.xlsx") as writer:
    f1_races.to_excel(writer, sheet_name="Racers", index=False)


# print
f1_races



# %%
def limpiar_gp(nombre):
    nombre = str(nombre).strip()
    
    # 1. Caso: texto duplicado exacto (Great BritainGreat Britain)
    mitad = len(nombre) // 2
    if nombre[:mitad] == nombre[mitad:]:
        return nombre[:mitad].strip()
    
    # 2. Caso: algo pegado al final sin espacio (AmericaIndianapolis)
    # buscamos el último punto donde empieza una mayúscula SIN espacio antes
    corte = None
    for i in range(1, len(nombre)):
        if nombre[i].isupper() and nombre[i-1] != ' ':
            corte = i
    
    if corte is not None:
        return nombre[:corte].strip()
    
    # 3. Si no cumple nada de lo anterior, lo dejamos tal cual
    return nombre


f1_races['Grand Prix'] = f1_races['Grand Prix'].apply(limpiar_gp)
f1_races


# %%

headers = {"User-Agent": "Mozilla/5.0"}
base_url = "https://www.formula1.com/en/results/{}/drivers"

# fecha actual para determinar el último año
now = datetime.now()
last_year = now.year if now.month >= 3 else now.year - 1

dfs = []

for year in range(1950, last_year + 1):
    url = base_url.format(year)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        continue

    try:
        df = pd.read_html(StringIO(r.text))[0]
        df["Year"] = year
        # Normalizar nombres de columna según el formato de drivers
        df.rename(columns=lambda x: x.strip(), inplace=True)
        if "Driver" in df.columns:
            df["Driver"] = df["Driver"].str.strip()
        if "Team" in df.columns:
            df["Team"] = df["Team"].str.strip()
        dfs.append(df)
    except ValueError:
        pass

# unir todos los años
f1_drivers = pd.concat(dfs, ignore_index=True)

# Extraer el código FIA (3 letras mayúsculas al final)
f1_drivers['DriverCode'] = f1_drivers['Driver'].str.extract(r'([A-Z]{3})$')

# Limpiar el nombre quitando las 3 letras finales
f1_drivers['Driver'] = f1_drivers['Driver'].str.replace(r'[A-Z]{3}$', '', regex=True).str.strip()
#f1_drivers

cols = list(f1_drivers.columns)

# Sacar DriverCode de donde esté
cols.remove('DriverCode')

# Insertarla justo después de Driver
driver_index = cols.index('Driver') + 1
cols.insert(driver_index, 'DriverCode')

# Reordenar el dataframe
f1_drivers = f1_drivers[cols]


# Guardar en Excel con hoja llamada 'Teams'
with pd.ExcelWriter("F1.xlsx") as writer:
    f1_drivers.to_excel(writer, sheet_name="Drivers", index=False)


# ver primeras filas
f1_drivers



# %%


# %%

headers = {"User-Agent": "Mozilla/5.0"}
base_url = "https://www.formula1.com/en/results/{}/team"

now = datetime.now()
last_year = now.year if now.month >= 3 else now.year - 1

dfs = []

for year in range(1950, last_year + 1):
    url = base_url.format(year)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        continue
    try:
        df = pd.read_html(StringIO(r.text))[0]
        df["Year"] = year
        # Limpiar nombres de equipos si existe la columna Team
        if "Team" in df.columns:
            df["Team"] = df["Team"].str.strip()
        dfs.append(df)
    except ValueError:
        continue

f1_teams = pd.concat(dfs, ignore_index=True)

# Guardar en Excel con hoja llamada 'Teams'
with pd.ExcelWriter("F1.xlsx") as writer:
    f1_teams.to_excel(writer, sheet_name="Teams", index=False)


# print
f1_teams


# %%
with pd.ExcelWriter("F1.xlsx") as writer:
    if not f1_races.empty:
        f1_races.to_excel(writer, sheet_name="Racers", index=False)
    if not f1_drivers.empty:
        f1_drivers.to_excel(writer, sheet_name="Drivers", index=False)
    if not f1_teams.empty:
        f1_teams.to_excel(writer, sheet_name="Teams", index=False)

print("Excel generado con éxito: F1.xlsx")

# %% [markdown]
# ### Leer los datos del excel

# %%


# %%
#Capturar archivo de datos
path = r'C:\turutadecarpetas\'
filef1 = 'F1.xlsx'

#Path
ruta_f1 = os.path.join(path, filef1)

df1_F1 = pd.read_excel(ruta_f1, sheet_name='Racers')
df1_F1
#df.count()


# %%
df2_F1 = pd.read_excel(ruta_f1, sheet_name='Drivers')
df2_F1
#df2_F1.count()

# %%
df3_F1 = pd.read_excel(ruta_f1, sheet_name='Teams')
df3_F1
#df3_F1.count()

# %%


# %%
df_merged = pd.merge(
    df1_F1,
    df2_F1,
    left_on=['Winner', 'Year'],
    right_on=['Driver', 'Year'],
    how='left'
)

df_merged


# %%
df_full = pd.merge(
    df2_F1,
    df1_F1,
    left_on='Year',
    right_on='Year',
    how='outer'
)
df_full

# %%


# %%



