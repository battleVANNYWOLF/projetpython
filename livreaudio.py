import pyttsx3
import PyPDF2
import speech_recognition as sr
import pyaudio

# rec_vocale = sr.Recognizer()
# mic = sr.Microphone()
# with mic as src:
#     audio = rec_vocale.listen(src)
#     texte = rec_vocale.recognize_google(audio, language="fr-FR")
#     print(texte)

engine = pyttsx3.init()
engine.say('Bonjour momsieur le programmeur,je suis un droid de la 3eme generation et je me nome  alexia')
engine.say('Maintenant,tu peux te relaxer et ecouter tranquillement')
engine.say('mamane le pote comment tu va?')
livre =  open('scrumagiles.pdf','rb')
lecture = PyPDF2.PdfFileReader(livre)
pages = lecture.numPages
print(pages)

debutlecture = lecture.getPage(3)
texte = debutlecture.extractText()
engine.say(texte)

engine.runAndWait()