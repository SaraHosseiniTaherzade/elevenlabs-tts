import requests

API_KEY = "sk_de4e53f175e1dc88e2e9866ce95f59168f7f013b243b5e4b"  

voice_id = "EXAVITQu4vr4xnSDxMaL"

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": "Hi I'm Sara and this is my first script in elevenlabs",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

print("🔄 در حال ارسال به ElevenLabs...")

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("✅ فایل صوتی ذخیره شد! output.mp3")
    print("🎵 از پنل سمت چپ دانلودش کن و گوش بده.")
    
else:
    print(f"❌ خطا: {response.status_code}")
    print(response.text)