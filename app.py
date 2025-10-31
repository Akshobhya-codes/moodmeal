from flask import Flask, request, jsonify, send_from_directory
from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests, json, os, datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

# ---------- Web search recipe generator ----------
from anthropic import Anthropic

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    mood = data.get("mood", "")
    groceries = data.get("groceries", "")
    prompt = (
        f"You are FridgeChef, an expert home-cook AI. "
        f"Based on the user's mood and available groceries, "
        f"create a short comforting recipe with a title, ingredient list, "
        f"and numbered cooking steps.\n\n"
        f"Mood: {mood}\n"
        f"Ingredients: {groceries}"
    )

    try:
        # Read Anthropic API key from environment variable for safety.
        # Set ANTHROPIC_API_KEY in your environment instead of pasting keys in source.
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        msg = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}],
        )
        text = msg.content[0].text
        return jsonify({"output": text})
    except Exception as e:
        return jsonify({"output": f"Error generating recipe: {e}"})

# ---------- Add recipe reminder to Google Calendar ----------
@app.route("/add_to_calendar", methods=["POST"])
def add_to_calendar():
    data = request.json
    title = data.get("title", "Cook Recipe")
    start = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    end = start + datetime.timedelta(minutes=30)

    SCOPES = ["https://www.googleapis.com/auth/calendar.events"]
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)
    event = {
        "summary": title,
        "start": {"dateTime": start.isoformat() + "Z"},
        "end": {"dateTime": end.isoformat() + "Z"},
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    return jsonify({"result": f"Added to Calendar: {event.get('htmlLink')}"})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
