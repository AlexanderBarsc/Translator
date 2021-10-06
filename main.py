from re import search
from googletrans import Translator
from languages_list import thisdict
import speech_recognition as sr
import inquirer
import os

# Programek pro prelozeni reci 

dir_path = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(dir_path)

# Ziskame vsechny soubory s priponou wav
subs = 'wav'
res = [i for i in files if subs in i]


found_files = [
  inquirer.List('Jazyk',
                message="Jaký chcete zvolit soubor?",
                choices=res,
            )
]

selected_file = inquirer.prompt(found_files)
sel = list(selected_file.values())


#Nacitame rec
r = sr.Recognizer()
filename = dir_path + '\\' + sel[0]
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    speech = r.recognize_google(audio_data, language= "cs-CZ")
    print("Nactena rec")
    print(speech)

#Pretocime dictionary jazyku, protoze jsem moc liny to prepisovat
inv_map = {v: k for k, v in thisdict.items()}


#Zvolime vystupni jazyk
questions = [
  inquirer.List('Jazyk',
                message="Do jakeho jazyka chcete přeložit?",
                choices=list(inv_map.keys()),
            )
]
answers = inquirer.prompt(questions)

search = list(answers.values())

#Najdeme jazyk v dictionary
lang = inv_map.get(search[0])

translator = Translator()

#Prelozime
out = translator.translate(speech,lang)

print(out.text)

input()
