from googletrans import Translator

translator = Translator()

b = input("Do you want to make a translation from Turkish to English? (Y/N)\n")
if b=="Y" or b == "y":
    word_in_tr = input("Please, enter a Turkish word or sentence for me to translate:\n")
    translation_tr_en = translator.translate(word_in_tr, src="tr", dest="en")
    print(f"{translation_tr_en.origin} => {translation_tr_en.text}")
else:
    c = input("Do you want to make a translation from English to Turkish (Y/N)\n")
    if c == "Y" or c == "y":
        word_in_en = input("Please, enter an English word or sentence for me to translate:\n")
        translation_en_tr = translator.translate(word_in_en,src="en",dest="tr")
        print(f"{translation_en_tr.origin} => {translation_en_tr.text}")
    else:
        print("Sorry, this program is only for translations between the languages Turkish and English.")
