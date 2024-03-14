from voice_to_text import voice_to_text
from text_to_voice import text_to_speech
from model import englishteacher

while True:
    text = voice_to_text()
    if text == "stop":
       break  # Exit the loop if the user says "stop"
# implement chatgpt
    response = englishteacher(text)

    text_to_speech(response)
    # time.sleep(1)
else:
    print("loop ended because user said stop" )








