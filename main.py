import argparse
from time import sleep
from pyngrok import ngrok
import os

# Configura argparse per ottenere il token dalla riga di comando
parser = argparse.ArgumentParser(description="Esegui ngrok con autenticazione.")
parser.add_argument("--token", required=True, help="Il token di autenticazione di ngrok")
args = parser.parse_args()

# Imposta il token di autenticazione
ngrok.set_auth_token(args.token)

# Connetti ngrok al tuo server locale
url = ngrok.connect(8000)

# Percorso del file dove salvare l'URL
file_path = "ngrok_url.txt"

# Elimina il file se esiste, quindi crea un nuovo file con il valore di `url`
if os.path.exists(file_path):
    os.remove(file_path)

with open(file_path, "w") as file:
    file.write(str(url))

print("Public URL:", url)

# Loop infinito per mantenere attiva la connessione
while True:
    sleep(50)
