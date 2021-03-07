from googletrans import Translator

translator = Translator()

metin = open("metin.txt","r",encoding="utf-8")
myText= metin.read()

translation = translator.translate(myText, dest='en')
print(translation.text)

trs = open("ceviri.txt", "w")
trs.write(str(translation.text))

metin.close()
trs.close()

print(translation.text)
