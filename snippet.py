import requests

API_KEY = "your_api_key_here"  # Replace with your NewsAPI key
url = (
    "https://newsapi.org/v2/top-headlines?"
    "country=us&"
    f"apiKey={API_KEY}"
)

new testasdfasd
asdfasdfasd
response = requests.get(url)
data = response.json()

if data["status"] == "ok":
    print("Top headlines:\n")
    for idx, article in enumerate(data["articles"], start=1):
        print(f"{idx}. {article['title']}")
        print(f"   {article['url']}\n")
else:
    print("Failed to fetch news:", data.get("message"))
