# utils
ZERO = 0
READ_BYTE = "rb"
CONFIG_FILE_NAME = "config.ini"
CFG_SPEECH_TO_TEXT_SECTION = "speechToText"
CFG_SPEECH_TO_TEXT_API_KEY = "api_key"
CFG_SPEECH_TO_TEXT_URL = "url"
CFG_LANG_TRANSLATION_SECTION = "languageTranslation"
CFG_LANG_TRANSLATION_API_KEY = "api_key"
CFG_LANG_TRANSLATION_URL = "url"
CFG_AUDIO_DIR = "audioDir"
CFG_AUDIO_PATH = "path"
CFG_AUDIO_FILE_NAME = "file_name"
CFG_AUDIO_CONTENT_TYPE = "content_type"
ENCODING_UTF8 = 'utf8'
CHANGE_DIR = '\\'
NONE = 'none'

# audio
AUDIO_LANG_MODEL_JP = "ja-JP_BroadbandModel"
AUDIO_LANG_MODEL_ZH = "zh-CN_BroadbandModel"
AUDIO_LANG_MODEL_EN = "en-US_BroadbandModel"
AUDIO_LANG_MODEL_KR = "ko-KR_BroadbandModel"
AUDIO_LANG_MODELS_LIST = ["ja-JP_BroadbandModel", "zh-CN_BroadbandModel", "en-US_BroadbandModel", "ko-KR_BroadbandModel"]
AUDIO_LANG_BASE_LANG_LIST = ["ja", "zh", "en", "ko"] 	
AUDIO_CONTENT_MSG = "The audio says ' {} ' ."

# supported languages
LANG_EN = 'en'
LANG_ZH = 'zh'
LANG_JP = 'ja'
LANG_KR = 'ko'
AUDIO_LANG_BASE_LANG_LIST_GOOGLE = ["ja", "zh", "en", "ko"]

# speech to text API
SPEECH_TO_TEXT_RESULTS = "results"
SPEECH_TO_TEXT_ALTERNATIVES = "alternatives"
SPEECH_TO_TEXT_TRANSCRIPT = "transcript"
SPEECH_TO_TEXT_CONFIDENCE = "confidence"
SPEECH_TO_TEXT_RESULTS_GOOGLE = "alternative"

# language translation API
LANG_TRANSLATION_API_VER = "2018-05-01"
LANG_LIST = "languages"
LANG_IDENTIFIED = "language"
LANG_IDENTIFIED_MSG = "Identified language of recording is ' {} '."
LANG_EN_TO_EN = "en-en"
LANG_MODEL_TO_EN = "-en"
LANG_MSG_ALREADY_IN_EN = "The audio is already in english."
LANG_TRANSLATION_LIST = "translations"
LANG_TRANSLATION = "translation"
LANG_MSG_TRANSLATION = "The translation is ' {} ' ." 