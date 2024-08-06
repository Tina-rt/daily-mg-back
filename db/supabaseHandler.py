import os
from supabase import create_client, client
from datetime import datetime
url:str = os.environ.get("SUPABASE_URL")
key:str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

def insertHeadlines(data):
    response = (supabase.table("Headlines").upsert(data, on_conflict="link").execute())
    
    return response

def getHeadlines(category=None, limit=20):
    if category:
        response = (supabase.table("Headlines").select("*, publisher(id,name)").eq("category", category).order("created_at", desc=True).limit(limit).execute())
    else:
        response = (supabase.table("Headlines").select("*, publisher(id,name)").execute())
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
    response = (supabase.table("Headlines").select("*, publisher(id,name)").eq("id", id).execute())
    return response.data