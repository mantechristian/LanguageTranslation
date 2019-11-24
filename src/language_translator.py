import json
import configparser
import constants as const
from googletrans import Translator
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class LanguageTranslation:
    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configParser.read(const.CONFIG_FILE_NAME)
        self.API_KEY = self.configParser.get(const.CFG_LANG_TRANSLATION_SECTION, const.CFG_LANG_TRANSLATION_API_KEY)
        self.API_URL = self.configParser.get(const.CFG_LANG_TRANSLATION_SECTION, const.CFG_LANG_TRANSLATION_URL)
        self.lang_translation_API = self.init_lang_translation_API(self.API_KEY, self.API_URL)
    
    def init_lang_translation_API(self, api_key, url):
        authenticator = IAMAuthenticator(api_key)
        language_translator = LanguageTranslatorV3(
            version=const.LANG_TRANSLATION_API_VER,
            authenticator=authenticator
        )
        language_translator.set_service_url(url)
        return language_translator

    def start_translation(self, text, baseLanguage):
        print(const.LANG_IDENTIFIED_MSG.format(baseLanguage))
        # lang_model = baseLanguage + const.LANG_MODEL_TO_EN
        # res = None

        # if lang_model == const.LANG_EN_TO_EN:
        #     # print(const.LANG_MSG_ALREADY_IN_EN)
        #     print(const.LANG_MSG_TRANSLATION.format(text))
        #     return text
        # else:
        #     translation = self.lang_translation_API.translate(
        #         text=text,
        #         model_id=lang_model).get_result()
        #     res = translation.get(const.LANG_TRANSLATION_LIST)[const.ZERO]
        #     res = res.get(const.LANG_TRANSLATION)
        #     print(const.LANG_MSG_TRANSLATION.format(res))
        # return res
        translator = Translator()
        res = translator.translate(text, dest=const.LANG_EN).text
        return res

