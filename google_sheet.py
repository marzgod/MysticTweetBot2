import gspread, json, os
from google.oauth2.service_account import Credentials
SCOPES=["https://www.googleapis.com/auth/spreadsheets"]
creds=Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT"]),scopes=SCOPES)
gc=gspread.authorize(creds)
ws=gc.open(os.environ["SPREADSHEET_NAME"]).worksheet(os.environ.get("WORKSHEET","Tweets"))
def next_tweet():
    rows=ws.get_all_records()
    for i,r in enumerate(rows,start=2):
        if not str(r.get("Posted","")).strip():
            return i,r["Tweet"]
    return None,None
def mark_posted(row):
    ws.update(f"C{row}","tweet posted")
