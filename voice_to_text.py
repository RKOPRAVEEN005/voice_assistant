
import speech_recognition as sr


def voice_to_text():
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("AI Teacher is listening.....")
        audio = recognizer.listen(source)

    # Use Google Web Speech API to convert audio to text
    try:
        text = recognizer.recognize_google(audio)
        print("Student: ", text)
        return text
    except sr.UnknownValueError:
        print("No audio is received....")
    except sr.RequestError as e:
        print("Error with the request: {0}".format(e))



if __name__ == '__main__':
    voice_to_text()
