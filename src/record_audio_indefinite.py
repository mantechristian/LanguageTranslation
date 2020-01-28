import argparse
import tempfile
import queue
import sys
import os

import sounddevice as sd
import soundfile as sf
import constants as const
import configparser
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

class RecordAudioIndefinite:
    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configParser.read(const.CONFIG_FILE_NAME)
        self.samplingFreq = self.configParser.getint(const.CFG_AUDIO_REC, const.CFG_REC_FREQ)
        self.recordingDuration = self.configParser.getint(const.CFG_AUDIO_REC, const.CFG_REC_DURATION)
        self.audio_path = self.configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_PATH)
        self.audio_file_name = self.configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_FILE_NAME)
        self.audio_file_path = os.path.join(self.audio_path, self.audio_file_name)
        self.channels = 2
        self.subtype = "PCM_24"
        self.tempFileName = 'temp.wav'
        self.tempFilePath = os.path.join(self.audio_path, self.tempFileName)
        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.q.put(indata.copy())
    
    def start(self):
        print("Start Recording (press ctrl + C to exit) ...")
        try:
            if self.samplingFreq is None:
                device_info = sd.query_devices('input')
                # soundfile expects an int, sounddevice provides a float:
                self.samplingFreq = int(device_info['default_samplerate'])
            if self.audio_file_path is None:
                self.audio_file_path = tempfile.mktemp(prefix='temp',
                                                suffix='.wav', dir='../audio')

            # Delete temp file if it exits
            if os.path.exists(self.tempFilePath): os.remove(self.tempFilePath)

            # Make sure the file is opened before recording anything:
            with sf.SoundFile(self.tempFilePath, mode='x', samplerate=self.samplingFreq,
                            channels=self.channels, subtype=self.subtype) as file:
                with sd.InputStream(samplerate=self.samplingFreq,
                                    channels=self.channels, callback=self.callback):
                    while True:
                        file.write(self.q.get())
        except KeyboardInterrupt:
            print('\nRecording finished: ' + repr(self.audio_file_path))
            os.rename(self.tempFilePath, self.audio_file_path)
        except Exception as e:
            print (e)
            print("An error ocurred while recording the audio.")

if __name__ == "__main__":
    recorder = RecordAudioIndefinite()
    recorder.start()