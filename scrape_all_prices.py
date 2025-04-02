
import os
import time
import json
import requests

games = {
    "rust": 252490,
    "dota": 570
}

CURRENCY = 1  # USD
SLEEP_INTERVAL = 13  # seconds
ITEMS_PER_PAGE = 100
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_market_items(appid, start):
    url = f"https://steamcommunity.com/market/search/render/"
    params = {
        "appid": appid,
        "norender": 1,
        "start": start,
        "count": ITEMS_PER_PAGE,
        "currency": CURRENCY
    }
    try:
        res = requests.get(url, params=params, headers=HEADERS, timeout=15)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"❌ Request failed for start={start}: {e}")
        return None

def scrape_game(game_name, appid):
    print(f"🚀 Starting scrape for {game_name.upper()} (AppID: {appid})")
    start = 0
    total_items = {}
    
    while True:
        print(f"📦 Fetching items {start}–{start + ITEMS_PER_PAGE}...")
        data = fetch_market_items(appid, start)
        if not data or 'results' not in data or not data['results']:
            print(f"✅ Finished {game_name.upper()} — Total items: {len(total_items)}\n")
            break

        for item in data['results']:
            name = item['hash_name']
            price = item.get('sell_price', 0) / 100
            total_items[name] = round(price, 2)

        start += ITEMS_PER_PAGE
        time.sleep(SLEEP_INTERVAL)

    # Save to JSON
    os.makedirs("prices", exist_ok=True)
    output_path = f"prices/{game_name}-prices.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(total_items, f, indent=2)
    print(f"💾 Saved to {output_path}\n")

if __name__ == "__main__":
    for game_name, appid in games.items():
        scrape_game(game_name, appid)
