# 🏎️ Formula 1 Historical Data Pipeline & Power BI Dashboard -WIP-

Proyecto de extracción, limpieza y análisis de datos históricos de la Fórmula 1 (1950 - actualidad), obtenidos directamente de formula1.com, con un dashboard interactivo construido en Power BI.

## 📋 Descripción

Este proyecto realiza web scraping de los resultados oficiales de Fórmula 1 (carreras, pilotos y equipos) desde la web oficial, limpia y normaliza los datos con pandas, los exporta a un archivo Excel (F1.xlsx) con varias hojas, y finalmente los consume desde un dashboard de Power BI (Formula1.pbix) para su visualización y análisis.

## 🚧 Estado del proyecto

- ✅ Componente EstadoScraping de carreras, pilotos y equipos (F1.py / F1.ipynb)
- ✅ Limpieza y normalización de datos
- ✅ Exportación a Excel (F1.xlsx)
- ✅ Automatización (F1.bat)
- 🚧 Dashboard de Power BI (Formula1.pbix)  WIP (Work in Progress) 

El dashboard de Power BI todavía está en construcción: las consultas e importación del dataset ya están conectadas, pero faltan terminar visualizaciones, medidas (DAX) y el diseño final de las páginas del reporte.



## 📂 Estructura del repositorio

Archivo F1.py Script principal en Python. Hace el scraping, limpieza y exportación de datos a F1.ipynb Notebook de Jupyter con el mismo proceso, pensado para exploración y desarrollo paso a paso.F1.batScript de Windows para ejecutar F1.py con un doble clic F1.bat Archivo de salida con los datos ya procesados, organizado en 3 hojas: Racers, Drivers y Formula1.pbix Dashboard de Power BI construido a partir de F1.xlsx.

## ⚙️ ¿Qué hace el script?


Scraping de carreras (Racers): recorre los resultados de cada Gran Premio desde 1950 hasta el año en curso, obteniendo Gran Premio, fecha, ganador, equipo, vueltas y tiempo.
Scraping de pilotos (Drivers): obtiene la clasificación de pilotos por temporada, separando el código FIA de 3 letras (ej. VER, HAM, LEC) del nombre del piloto.
Scraping de equipos (Teams): obtiene la clasificación de constructores/equipos por temporada.
Limpieza de datos:

Corrige nombres de Gran Premio duplicados o mal formateados (p. ej. "Great BritainGreat Britain" → "Great Britain").
Extrae y separa los códigos de piloto (FIA) del nombre completo.
Normaliza espacios y formatos de texto.

Exportación: guarda todo en F1.xlsx, con una hoja por entidad (Racers, Drivers, Teams).
Análisis exploratorio: combina (merge) los datos de carreras y pilotos para relacionar ganadores de cada GP con sus estadísticas de temporada.


## 🛠️ Tecnologías utilizadas

- pandas
- Power BI
- Python 3.12
- manipulación y limpieza de datos
- requests - peticiones HTTP para el scraping
- numpy / matplotlib - soporte numérico y gráfico
- Automatización para Windows .bat

## 🚀 Cómo ejecutarlo

Requisitos

bashpip install pandas numpy matplotlib requests openpyxl lxml

Ejecución

bashpython F1.py

O en Windows, simplemente haciendo doble clic en:

F1.bat

Esto generará/actualizará el archivo F1.xlsx en el mismo directorio.



## ⚠️ Nota: el script depende de la estructura HTML de formula1.com en el momento de la ejecución. Si la web cambia su estructura, el scraping (pd.read_html) puede dejar de funcionar y requerirá ajustes.



## 📊 Datos disponibles

Columnas principales RacersGrand Prix, Date, Winner, WinnerCode, Team, Laps, Time, YearDriversPos., Driver, DriverCode, Nationality, Team, Pts., YearTeamsPos., Team, Pts., Year



## 📌 Notas

Los datos cubren temporadas desde 1950 hasta la temporada actual (se actualiza dinámicamente según la fecha del sistema).
Las rutas de archivo en F1.py y F1.bat están configuradas para un entorno local específico (C:\Users\xxaby\Desktop\master\Formula1); deberás ajustarlas a tu propia ruta si clonas el repositorio.



## 📄 Licencia

Este proyecto se distribuye con fines educativos y de análisis de datos. Los datos provienen de la web oficial de Fórmula 1 y son propiedad de sus respectivos titulares.
