import feedparser
import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'us-en')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None
    return query            

query = takecommand()
    
if  'news' in query.lower():
    d=feedparser.parse('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    for post in d.entries:
    # if you want news with link then print this line(post.title+ ":"+post.link+"\n").
    # or if you want only post title then use below command.
        print(post.title+ ":")
        speak(post.title+ ":")





