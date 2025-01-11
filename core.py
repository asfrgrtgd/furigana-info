import requests
import urllib.parse
from bs4 import BeautifulSoup
from .exceptions import FuriganaInfoError
from .utils import clean_text

BASE_URL = "https://furigana.info/w/"

def build_url(word: str) -> str:
    """指定した語を URL エンコードして furigana.info の検索 URL を組み立てる."""
    encoded_word = urllib.parse.quote(word, safe="")
    return BASE_URL + encoded_word

def fetch_page(url: str, timeout=10) -> str:
    """指定 URL から HTML を取得する."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; FuriganaInfoBot/1.0; +https://github.com/yourname/furigana_info)"
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text

def parse_furigana(html: str):
    """HTML をパースして読み仮名や例文などを抽出する."""
    soup = BeautifulSoup(html, "html.parser")
    readings = []
    examples = []
    
    sum_table = soup.select_one(".sum_table")
    if sum_table:
        rows = sum_table.select("tr")[1:]
        for row in rows:
            cols = row.select("td")
            if len(cols) == 2:
                yomi = clean_text(cols[0].get_text())
                percentage = clean_text(cols[1].get_text())
                readings.append((yomi, percentage))
    yomi_blocks = soup.select(".yomi_wrapper")
    for block in yomi_blocks:
        yomi_div = block.select_one(".yomi a")
        if yomi_div:
            reading_text = clean_text(yomi_div.get_text())
        else:
            reading_text = ""
        snip_div = block.select_one(".examples .snip")
        if snip_div:
            snippet_text = clean_text(snip_div.get_text())
        else:
            snippet_text = ""
        
        examples.append({
            "reading": reading_text,
            "text": snippet_text
        })
    
    return readings, examples

def get_furigana(word: str):
    """
    単語の読み仮名や例文をまとめて取得し、辞書形式で返す。
    例:
        {
          "word": "濃黒",
          "readings": [
            {"yomi": "どすぐろ", "percentage": "50.0%"},
            {"yomi": "まつくろ", "percentage": "50.0%"}
          ],
          "examples": [
            {"reading": "どすぐろ", "text": "..."},
            {"reading": "まつくろ", "text": "..."}
          ]
        }
    """
    url = build_url(word)
    try:
        html = fetch_page(url)
    except requests.RequestException as e:
        raise FuriganaInfoError(f"HTTP request failed: {e}")
    
    readings, examples = parse_furigana(html)
    return {
        "word": word,
        "readings": [
            {"yomi": r[0], "percentage": r[1]} for r in readings
        ],
        "examples": examples
    }