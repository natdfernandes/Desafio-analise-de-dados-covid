from supabase import create_client, Client
from streamlit import secrets

url: str = secrets.supabase_url
key: str = secrets.supabase_key
supabase: Client = create_client(url, key)


def get_history():
    return supabase.table("history").select("*").execute()


def insert_history(page: str, filter: str):
    supabase.table("history").insert({"page": page, "filter": filter}).execute()
