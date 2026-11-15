import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / '.env')

api_token = os.getenv('HF_API_TOKEN')
API_URL = "https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": f"Bearer {api_token}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

text1 = """Президент РФ Владимир Путин подписал указ «О призыве в апреле – июле 2025 г. граждан Российской Федерации на военную службу и об увольнении с военной службы граждан, проходящих военную службу по призыву»."""
text2 = """Путин заявил о невозможности выхода в запас военнослужащих, проходящих военную службу по контракту и при этом необходимости проведения дополнительного набора в рамках весеннего призыва в апреле - июле 2025 г."""
text3 = """Глава Российской Федерации Владимир Путин издал распоряжение, в котором говорится о проведении призыва на военную службу в период с апреля по июль 2025 года. Также в документе содержится информация об увольнении с военной службы граждан, которые проходят её по призыву."""
text4 = """Президент РФ Владимир Путин подписал указ «О призыве в апреле – июле 2026 г. граждан Российской Федерации на военную службу и об увольнении с военной службы граждан, проходящих военную службу по призыву»."""

data = query(
    {
        "inputs": {
            "source_sentence": text1,
            "sentences":[text4, text3]
        }
    })

print(data)

# [0.605, 0.894]
