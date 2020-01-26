import os
import sys
import time
import logging
import configparser
import constants as const
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from speech_to_text import SpeechToText
from language_translator import LanguageTranslation

configParser = configparser.ConfigParser()
configParser.read(const.CONFIG_FILE_NAME)
audio_path = configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_PATH)
audio_file_name = configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_FILE_NAME)

class Event(LoggingEventHandler):
    def on_created(self, event):
        audio_file_path = os.path.join(audio_path, audio_file_name)
        try:
            print("Triggering speech to text ...")
            time.sleep(1)
            start_time = time.time()
            extracted_speech, baseLanguage = SpeechToText().start_speech_to_text()
            if baseLanguage == "none":
                print("Invalid Language")
                return
            else:
                translated_text = LanguageTranslation().start_translation(extracted_speech, baseLanguage)
                print(translated_text)
                print("--- TOTAL execution time: %s seconds ---" % (time.time() - start_time))
                print("Deleting the recording file ...")
                os.remove(audio_file_path)
        except Exception as e:
            print(e)
            print("An error ocurred while translating speech to text.")
        finally:
            if os.path.isfile(audio_file_path):
                os.remove(audio_file_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = audio_path
    event_handler = Event()
    observer = Observer()
    print("Listening ...")
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()