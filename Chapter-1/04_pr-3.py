#3.	Install an external module and use it to perform an operation of your interest.
# text to speech python
import pyttsx3
engine = pyttsx3.init()
engine.say("Hey, Naima. I am a python module. Welcome to the world of python")
engine.runAndWait()