import speech_recognition as sr
import pyttsx3

class Mini():
    __name = ""

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate+15)
        self.engine.runAndWait()

        # Set the name if none given
        if name is not None:
            self.__name = name

        print("Listening")

        # Initialise recorder and microphone
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def say_name(self, nametag):
        name_introduction = "Hello my name is " + self.__name
        self.__name = nametag
        self.engine.say(name_introduction)
        self.engine.runAndWait()
        return name_introduction

    def speak(self, text):
        # print('text: ', text)
        self.engine.say(text, 'response')
        self.engine.runAndWait()
        return text

    def listen(self):
        # Open microphone and start recording
        with self.m as source:
            print('Say something')
            audio = self.r.listen(source)

        # Use google's speech recognition
        voice_data = ''
        try:
            voice_data = self.r.recognize_google(audio, show_all = False, language="en_US")
            print('You: ' + voice_data)
            self.engine.say(voice_data)
            self.engine.runAndWait()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Request results from Google Speech Recognition service error')
        return voice_data

# Run mini
command = ""
mini = Mini()
while True and command != "goodbye":
    command = mini.listen()

mini.speak("Goodbye")


