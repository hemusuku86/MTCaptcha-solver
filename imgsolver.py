import requests

def solve(imgbase64):
  r = requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyDxJGnccDS1cbYIWQiD4ml8Ait3KASwoVA", json={"contents": [{"parts": [{"text": "what text in this image?"}, {"inline_data": {"mime_type": "image/jpeg", "data": imgbase64}}]}]}) # omg i leaked gemini apikey wtf
  resp = r.json()["candidates"][0]["content"]["parts"][0]["text"]
  if '"' in resp:
    return resp.split('"')[1]
  elif "'" in resp:
    return resp.split("'")[1]
  elif "is" in resp:
    return resp.split("is ")[1].split(".")[0]
  else:
    return resp
