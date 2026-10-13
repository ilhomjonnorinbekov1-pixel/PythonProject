def chegirma(narx, foiz):
    if not 0 <= foiz <= 100:
        raise ValueError("Foiz 0..100")
    return narx - narx * foiz / 100

import time, threading

def yukla(nom):
    print(f"⬇️ {nom} yuklanmoqda...")
    time.sleep(1)                        # internetni kutish (requests.get kabi)
    print(f"✅ {nom} tayyor")

fayllar = ["rasm.png", "video.mp4", "musiqa.mp3"]

# --- Ketma-ket ---
t = time.time()
for f in fayllar:
    yukla(f)
print(f"⏱ {time.time() - t:.1f} s")

# --- threading ---
t = time.time()
oqimlar = [threading.Thread(target=yukla, args=(f,)) for f in fayllar]
for o in oqimlar:
    o.start()                            # ishga tushir — kutmasdan keyingisiga
for o in oqimlar:
    o.join()                             # hammasi tugashini kut
print(f"⏱ {time.time() - t:.1f} s")