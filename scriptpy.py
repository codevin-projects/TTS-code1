import pyttsx3
def voiceChange():
    eng = pyttsx3.init()
    voice = eng.getProperty('voices') 
    eng.setProperty('voice', voice[1].id)
    cmd = "This is a demonstration of how to convert index of voice using pyttsx3 library in python."
    eng.say(cmd)
    eng.runAndWait()

if __name__ == "__main__":
    voiceChange()