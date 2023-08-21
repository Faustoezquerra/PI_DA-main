import requests
import csv

# URL de la API de CoinGecko para obtener datos de criptomonedas
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parámetros de la solicitud
params = {
    "vs_currency": "usd",   # Moneda con la que se comparan los precios
    "order": "market_cap_desc",  # Orden de clasificación por capitalización de mercado
    "per_page": 10,  # Número de resultados por página
    "page": 1        # Página de resultados
}

# Realizar la solicitud GET a la API
response = requests.get(url, params=params)
data = response.json()

# Nombre del archivo CSV en el que se guardarán los datos
csv_filename = "coin_data.csv"

# Abrir el archivo CSV en modo de escritura
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    # Crear un objeto CSV writer
    csv_writer = csv.writer(csv_file)

    # Escribir encabezados
    csv_writer.writerow(["Nombre", "Símbolo", "Precio", "Capitalización de mercado", "Volumen"])

    # Escribir datos de cada criptomoneda en filas
    for coin in data:
        name = coin["name"]
        symbol = coin["symbol"]
        price = coin["current_price"]
        market_cap = coin["market_cap"]
        volume = coin["total_volume"]
        csv_writer.writerow([name, symbol, price, market_cap, volume])

print("Datos extraídos y guardados en", csv_filename)
