import os
from supabase import create_client, client
from datetime import datetime
url:str = os.environ.get("SUPABASE_URL")
key:str = os.environ.get("SUPABASE_KEY")
print(key)
supabase = create_client(url, key)

def insertHeadlines(data):
    response = (supabase.table("Headlines").upsert(data, on_conflict="link").execute())
    
    return response

def getHeadlines(category=None):
    if category:
        response = (supabase.table("Headlines").select("*").eq("category", category).execute())
    else:
        response = (supabase.table("Headlines").select("*").execute())
    return response


def getStatus():
    response = (supabase.table("Status").select("*").execute())
    return response

def updateStatus():
    current_status = getStatus()
    print(current_status.data)
    if len(current_status.data) == 0:
        res = supabase.table("Status").insert({"last_update": str(datetime.now())}).execute()
        return res
    return

def getDetails(id):
    response = (supabase.table("Headlines").select("*").eq("id", id).execute())
    return response.data