from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
txt = engine.image_to_string(Image.open('test1.png'), lang="eng")
print(txt) # 「Test Message」が出力される
