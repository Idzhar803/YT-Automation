# auth_helper.py
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os, pickle

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def login_and_save_token(token_path, client_secret="client_secrets.json"):
    flow = InstalledAppFlow.from_client_secrets_file(client_secret, SCOPES)
    creds = flow.run_console()

    with open(token_path, 'wb') as token_file:
        pickle.dump(creds, token_file)
    print(f"Token disimpan di: {token_path}")

def load_token(token_path):
    if not os.path.exists(token_path):
        raise Exception("Token belum dibuat. Jalankan login_and_save_token() dulu.")
    with open(token_path, 'rb') as token_file:
        return pickle.load(token_file)
