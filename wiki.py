# Credit: https://gitHub.com/DhairyaShah-Programmer

import pyttsx3 as tts
import wikipedia as wiki

# Search Logic
searchOpt = str(input("What do you want to search: "))
summary = wiki.summary(searchOpt, sentences=7)
print( "\n" + summary)
page = wiki.page(searchOpt)

# TTS Logic
engine = tts.init()
engine.say(summary)
engine.runAndWait()

print("Goodbye! Have a good day")
