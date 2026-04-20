from deep_translator import GoogleTranslator

cache = {}

def translate(text):
    if text in cache:
        return cache[text]

    translated = GoogleTranslator(
        source='auto',
        target='en'
    ).translate(text)

    cache[text] = translated
    return translated