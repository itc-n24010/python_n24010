import re

a = 'かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoeing787で高松空港まで行き、帰りはN700系で岡山から戻りました。'
print(re.findall(r'[a-zA-Z-]+\d+', a))
