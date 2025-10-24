from gtts import gTTS
import os

my_text = "Lorem ipsum dolor sit"
language = "en"
my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj.save("result.mp3")
os.system("result.mp3")