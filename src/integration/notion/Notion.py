# Initialisation
import requests, json
import os
from dotenv import load_dotenv

load_dotenv()

class Notion:
    def __init__(self):
        self.token = os.getenv('NOTION_TOKEN')
        self.databaseID = os.getenv('NOTION_DATABASE_ID')
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def database_status(self):
        try:
            readUrl=f"https://api.notion.com/v1/databases/{self.databaseID}"
            res=requests.request("GET", readUrl, headers=self.headers)

            print(res.status_code)
        except Exception as e:
            print(e)
    
    def database_retrieve(self):
        try:
            readUrl=f"https://api.notion.com/v1/databases/{self.databaseID}"
            res=requests.request("GET",readUrl,headers=self.headers)
        
            return res.json()
        except Exception as e:
            return None
        
    def database_query(self):
        pass

    def database_insert_page(self, data):
        try:
            createUrl = f"https://api.notion.com/v1/pages"

            res=requests.request("POST",createUrl,headers=self.headers,data=json.dumps(data))
            
            return res.json()
        except Exception as e:
            return None

    def database_update(self):
        pass

notion = Notion().database_insert_page()
print(notion)