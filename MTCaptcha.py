import curl_cffi
import ua_generator
from ua_generator.options import Options
from ua_generator.data.version import VersionRange
import imgsolver
import secrets
import hashlib
import random
import time
import uuid
import math

def transactionSignature(_0x4990fd, _0x4cd178):
  return "TH[" + hashlib.md5((_0x4cd178 + _0x4990fd).encode()).hexdigest() + "]"

def int32(n):
  n = n & 0xFFFFFFFF
  if n >= 0x80000000:
    n -= 0x100000000
  return n

class FoldChlg:
  def __init__(self):
    pass
  def URLSafeBase64CharToInt(self, _0x5db43a):
    URLSafeBase64CharCode2IntMap = [
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            0x3e,
            -0x1,
            -0x1,
            0x0,
            0x1,
            0x2,
            0x3,
            0x4,
            0x5,
            0x6,
            0x7,
            0x8,
            0x9,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            0xa,
            0xb,
            0xc,
            0xd,
            0xe,
            0xf,
            0x10,
            0x11,
            0x12,
            0x13,
            0x14,
            0x15,
            0x16,
            0x17,
            0x18,
            0x19,
            0x1a,
            0x1b,
            0x1c,
            0x1d,
            0x1e,
            0x1f,
            0x20,
            0x21,
            0x22,
            0x23,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            0x3f,
            -0x1,
            0x24,
            0x25,
            0x26,
            0x27,
            0x28,
            0x29,
            0x2a,
            0x2b,
            0x2c,
            0x2d,
            0x2e,
            0x2f,
            0x30,
            0x31,
            0x32,
            0x33,
            0x34,
            0x35,
            0x36,
            0x37,
            0x38,
            0x39,
            0x3a,
            0x3b,
            0x3c,
            0x3d,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1,
            -0x1
    ]
    _0x5db43a = ord(_0x5db43a[0])
    _0x2699c1 = URLSafeBase64CharCode2IntMap[_0x5db43a % 0x100]
    return _0x2699c1
  def URLSafeBase64IntToChar(self, _0x26f8c7):
    URLSafeBase64Int2CharMap = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'J',
            'K',
            'L',
            'M',
            'N',
            'O',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'U',
            'V',
            'W',
            'X',
            'Y',
            'Z',
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z',
            '-',
            '_'
        ]
    return URLSafeBase64Int2CharMap[_0x26f8c7 % 0x40]
  def URLSafeBase4096IntToChar(self, _0x101738):
    return "" + self.URLSafeBase64IntToChar(_0x101738 >> 0x6) + self.URLSafeBase64IntToChar(_0x101738 & 0x3f)
  def URLSafeBase64Str2IntArray(self, _0x42402c):
    _0x379e1d = []
    for _0x411f36 in range(len(_0x42402c)):
      _0x379e1d.append(self.URLSafeBase64CharToInt(_0x42402c[_0x411f36]))
    return _0x379e1d
  def hashIntAry(self, _0x2c7601):
    _0x4bb62d = 0x0
    for _0x504548 in range(len(_0x2c7601)):
      _0x4bb62d = int32(_0x4bb62d << 0x5) - _0x4bb62d + _0x2c7601[_0x504548]
      _0x4bb62d = int32(_0x4bb62d & _0x4bb62d)
    if _0x4bb62d < 0x0:
      _0x4bb62d *= -0x1
    return _0x4bb62d
  def solve(self, _0x158a06, _0x4c6381, _0x43e330):
    _0x311562 = []
    _0x3d9dd9 = self.URLSafeBase64Str2IntArray(_0x158a06)
    for _0x26938f in range(_0x4c6381):
      _0x3d9dd9 = self.foldBase64IntArray(_0x3d9dd9, 0x1f)
      _0x23dab8 = self.hashIntAry(self.foldBase64IntArray(_0x3d9dd9, _0x43e330))
      _0x311562.append(self.URLSafeBase4096IntToChar(_0x23dab8 % 0x1000))
    return "".join(_0x311562)
  def foldBase64IntArray(self, a1, foldCount):
    a2 = [a for a in a1][::-1]
    a3 = [a for a in a1]
    offset = x = y = z = i = 0
    for i in range(foldCount):
      offset += 1
      for x in range(len(a1)):
        a3[x] = (math.floor((a3[x] + a2[(x + offset) % len(a2)]) * 73 / 8) + y + z) % 64
        z = math.floor(y / 2)
        y = math.floor(a3[x] / 2)
    return a3

def solve(sitekey, url, proxy=None, log=False):
  chrome_v = 120
  ua_options = Options()
  ua_options.version_ranges = {
    'chrome': VersionRange(chrome_v, chrome_v)
  }
  s = curl_cffi.Session(impersonate="chrome131")
  ua = ua_generator.generate(browser='chrome', platform="ios", options=ua_options)
  s.headers = {"User-Agent": ua.text, "referer":"https://service.mtcaptcha.com/"}
  if proxy != None:
    s.proxies.update({"https": proxy})
  domain = url.split("/")[2]
  ss = f"S1{str(uuid.uuid4())}"
  s.get("https://service.mtcaptcha.com/mtcv1/client.iframe.html", params={
  "action": "",
  "autoFadeOuterText": "false",
  "challengeType": "standard",
  "custom": "false",
  "enableMouseFlow": "false",
  "host": f"https://{domain}",
  "hostname": domain,
  "iframeId": "mtcaptcha-iframe-1",
  "lang": "en",
  "lowFrictionInvisible": "",
  "serviceDomain": "service.mtcaptcha.com",
  "sitekey": sitekey,
  "textLength": "0",
  "theme": "basic",
  "v": "2024-11-14.21.53.06",
  "widgetInstance": "mtcaptcha",
  "widgetSize": "standard"
  })
  r = s.get("https://service.mtcaptcha.com/mtcv1/api/getchallenge.json", params={
    "sk": sitekey,
    "bd": domain,
    "rt": str(round(time.time()/1000)),
    "act": "$",
    "lf": "1",
    "tl": "$",
    "lg": "en",
    "tp": "s",
    "ss": ss,
    "tsh": transactionSignature(sitekey, "mtcap@mtcaptcha.com")
  })
  ct = None
  if "result" in r.json():
    if "challenge" in r.json()["result"]:
      ct = r.json()["result"]["challenge"]["ct"]
      foldChlg = r.json()["result"]["challenge"]["foldChlg"]
      if log == True:
        print(f"(MTCaptcha Solver log) Got Challenge -> {ct}")
        if foldChlg["fdepth"] > 2000:
          print(f"(MTCaptcha Solver log) huge foldChlg, it means your proxy is flagged and it causes solving to take a long time -> {foldChlg}")
  if ct == None:
    if log == True:
      print(f"(MTCaptcha Solver log) Failed to get challenge | {r.text}")
    return "Failed"
  if foldChlg["preRes"] == True:
    foldChlg["fa"] = FoldChlg().solve(foldChlg["fseed"], foldChlg["fslots"], foldChlg["fdepth"])
  r = s.get("https://service.mtcaptcha.com/mtcv1/api/getimage.json", params={
    "sk": sitekey,
    "ct": ct,
    "fa": foldChlg["fa"] if "fa" in foldChlg else "$",
    "ss": ss
  })
  imgbase64 = None
  if "result" in r.json():
    if "img" in r.json()["result"]:
      imgbase64 = r.json()["result"]["img"]["image64"]
      if log == True:
        print(f"(MTCaptcha Solver log) Got Image -> {imgbase64[:40]}...")
  if imgbase64 == None:
    if log == True:
      print(f"(MTCaptcha Solver log) Failed to get image | {r.text}")
    return "Failed"
  s.get("https://service.mtcaptcha.com/mtcv1/api/getaudio.json", params={
    "sk": sitekey,
    "ct": ct,
    "fa": foldChlg["fa"] if "fa" in foldChlg else "$",
    "ss": ss
  })
  cap_text = imgsolver.solve(imgbase64)
  if log == True:
    print(f"(MTCaptcha Solver log) Image solved -> {cap_text}")
  r = s.get("https://service.mtcaptcha.com/mtcv1/api/solvechallenge.json", params={
    "sk": sitekey,
    "ct": ct,
    "st": cap_text,
    "lf": "1",
    "bd": domain,
    "rt": str(round(time.time()/1000)),
    "tsh": transactionSignature(sitekey, "mtcap@mtcaptcha.com"),
    "fa": foldChlg["fa"] if "fa" in foldChlg else FoldChlg().solve(foldChlg["fseed"], foldChlg["fslots"], foldChlg["fdepth"]),
    "qh": "$",
    "act": "$",
    "ss": ss,
    "tl": "$",
    "lg": "en",
    "tp": "s",
    "kt": "AAA",
    "fs": foldChlg["fseed"]
  })
  token = None
  if "result" in r.json():
    if "verifyResult" in r.json()["result"]:
      if "verifiedToken" in r.json()["result"]["verifyResult"]:
        if "vt" in r.json()["result"]["verifyResult"]["verifiedToken"]:
          token = r.json()["result"]["verifyResult"]["verifiedToken"]["vt"]
          if log == True:
            print(f"(MTCaptcha Solver log) MTCaptcha Solved -> {token[:60]}...")
          return token
  if token == None:
    if log == True:
      print(f"(MTCaptcha Solver log) Failed to submit answer | {r.text}")
    return "Failed"
