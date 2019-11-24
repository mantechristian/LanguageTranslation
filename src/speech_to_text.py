import json
import time
import os.path
import configparser
import constants as const
import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class SpeechToText:
    
    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configParser.read(const.CONFIG_FILE_NAME)
        self.API_KEY = self.configParser.get(const.CFG_SPEECH_TO_TEXT_SECTION, const.CFG_SPEECH_TO_TEXT_API_KEY)
        self.API_URL = self.configParser.get(const.CFG_SPEECH_TO_TEXT_SECTION, const.CFG_SPEECH_TO_TEXT_URL)
        self.audio_path = self.configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_PATH)
        self.audio_file_name = self.configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_FILE_NAME)
        self.audio_content_type = self.configParser.get(const.CFG_AUDIO_DIR, const.CFG_AUDIO_CONTENT_TYPE)
        self.speech_to_text_API = self.init_speech_to_text_API(self.API_KEY, self.API_URL)
    
    def init_speech_to_text_API(self, api_key, url):
        authenticator = IAMAuthenticator(api_key)
        speech_to_text = SpeechToTextV1(
            authenticator=authenticator
        )
        speech_to_text.set_service_url(url)
        return speech_to_text

    def start_speech_to_text(self):
        confidenceList = []
        transcriptList = []

        # Supported languages: Chinese, Japanese, Korean, English

        # # WATSON SPEECH TO TEXT API
        # start_time = time.time()
        # pathToSpeech = os.path.abspath(self.audio_path) + const.CHANGE_DIR + self.audio_file_name
        # for langModel in const.AUDIO_LANG_MODELS_LIST:
        #     with open(pathToSpeech, const.READ_BYTE) as audio_file:
        #         speech_recognition_results = self.speech_to_text_API.recognize(
        #             audio=audio_file,
        #             content_type=self.audio_content_type,
        #             word_alternatives_threshold=0.9,
        #             model = langModel,
        #         ).get_result()
        #         res = speech_recognition_results
        #         res = res.get(const.SPEECH_TO_TEXT_RESULTS)[const.ZERO]
        #         confidence = res.get(const.SPEECH_TO_TEXT_ALTERNATIVES)[const.ZERO].get(const.SPEECH_TO_TEXT_CONFIDENCE)
        #         transcript = res.get(const.SPEECH_TO_TEXT_ALTERNATIVES)[const.ZERO].get(const.SPEECH_TO_TEXT_TRANSCRIPT)
        #         confidenceList.append(confidence)
        #         transcriptList.append(transcript)

        # retrieve value for confidence
        # highest confidence is most likely the true base language

        # print(confidenceList)
        # langIdx = confidenceList.index(max(confidenceList))
        # baseLanguage = const.AUDIO_LANG_BASE_LANG_LIST[langIdx]
        # transcript = transcriptList[langIdx]
        # extracted_text = transcript
        # print("--- speech_to_text execution time: %s seconds ---" % (time.time() - start_time))
        # return extracted_text, baseLanguage

        # GOOGLE SPEECH API
        start_time = time.time()
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        res = {}
        audio_data = sr.AudioFile(os.path.abspath(self.audio_path) + const.CHANGE_DIR + self.audio_file_name)
        with audio_data as source:
            audio = recognizer.record(source)
            for langModel in const.AUDIO_LANG_BASE_LANG_LIST_GOOGLE:
                result = recognizer.recognize_google(audio, language = langModel, show_all=True)
                if not result:
                    confidence = const.ZERO
                    transcript = const.NONE
                else:
                    res = result.get(const.SPEECH_TO_TEXT_RESULTS_GOOGLE)[const.ZERO]
                    confidence = res.get(const.SPEECH_TO_TEXT_CONFIDENCE)
                    transcript = res.get(const.SPEECH_TO_TEXT_TRANSCRIPT)
                confidenceList.append(confidence)
                transcriptList.append(transcript)
        
        langIdx = confidenceList.index(max(confidenceList))
        baseLanguage = const.AUDIO_LANG_BASE_LANG_LIST[langIdx]
        transcript = transcriptList[langIdx]
        extracted_text = transcript
        print("--- speech_to_text execution time: %s seconds ---" % (time.time() - start_time))
        print(confidenceList)
        print(transcriptList)
        return extracted_text, baseLanguage
