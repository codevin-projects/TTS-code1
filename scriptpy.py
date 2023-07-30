import pyttsx3
def voiceChangeFemale():
    eng = pyttsx3.init()
    voice = eng.getProperty('voices') 
    eng.setProperty('voice', voice[1].id)
    cmd = input("Enter text here: ")
    eng.say(cmd)
    eng.runAndWait()

def voiceChangeMale():
    tesp = pyttsx3.init()
    res = input("Enter text here: ")
    tesp.say(res)
    tesp.runAndWait()

if __name__ == "__main__":
    voiceChangeFemale()
    voiceChangeMale()
