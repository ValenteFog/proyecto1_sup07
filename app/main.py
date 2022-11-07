from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Cargamos el archivo csv, ingestándolo en dataframe, usando pandas
df = pd.read_csv('./csv/netflix.csv')

# Cambiamos el tipo de dato de la columna 'date_added' a datetime
df['date_added'] = df['date_added'].apply(pd.to_datetime)

# Ordenamos de más antiguo a más reciente, tomando la columna 'date_added'
df.sort_values(by=['date_added'], inplace=True)

# En la columna 'director' reemplazamos el valor 'Not Given' por None
df['director'].replace(to_replace='Not Given', value=None, inplace=True)

# Dividimos el dataframes en 3 años (2019, 2020, 2021) tomando 'release_year'
df_19 = df[df['release_year'] == 2019]
df_20 = df[df['release_year'] == 2020]
df_21 = df[df['release_year'] == 2021]

# Transformamos los 3 df en 3 dicc distintos usando: '.reset_index().to_dict(orient="index")'
dicc_19 = df_19.reset_index().to_dict(orient='index')
dicc_20 = df_20.reset_index().to_dict(orient='index')
dicc_21 = df_21.reset_index().to_dict(orient='index')


@app.get('/')
async def index():
    return {'Viendo que': 'Onda'}


@app.get('/2019')
async def cat_19():
    return {'2019': dicc_19}


@app.get('/2020')
async def cat_20():
    return {'2020': dicc_20}


@app.get('/2021')
async def cat_21():
    return {'2021': dicc_21}
