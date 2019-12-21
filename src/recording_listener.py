import os
import sys
import time
import main
import logging
import configparser
import constants as const
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

configParser = configparser.ConfigParser()
configParser.read(const.CONFIG_FILE_NAME)
audio_path = configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_PATH)
audio_file_name = configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_FILE_NAME)

class Event(LoggingEventHandler):
    def on_created(self, event):
        print("Triggering speech to text ...")
        time.sleep(1)
        main.start()
        print("Deleting the recording file ...")
        audio_file_path = os.path.join(audio_path, audio_file_name)
        os.remove(audio_file_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = audio_path
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()