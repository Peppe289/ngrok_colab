import argparse
from time import sleep
from pyngrok import ngrok
import os

parser = argparse.ArgumentParser(description="Esegui ngrok con autenticazione.")
parser.add_argument("--token", required=True, help="Il token di autenticazione di ngrok")
args = parser.parse_args()

ngrok.set_auth_token(args.token)

url = ngrok.connect(8000)

file_path = "ngrok_url.txt"

if os.path.exists(file_path):
    os.remove(file_path)

with open(file_path, "w") as file:
    string = url.read().split()[1]
    string = string[1:len(string) - 1]
    file.write(str(string))

print("Public URL:", url)
while True:
    sleep(10000)
