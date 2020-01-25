import time
from speech_to_text import SpeechToText
from language_translator import LanguageTranslation

def start():
    start_time = time.time()
    extracted_speech, baseLanguage = SpeechToText().start_speech_to_text()
    translated_text = LanguageTranslation().start_translation(extracted_speech, baseLanguage)
    print(translated_text)
    print("--- TOTAL execution time: %s seconds ---" % (time.time() - start_time))

if __name__=="__main__":
    start()