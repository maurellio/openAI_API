import openai
import deepl

auth_key = ""
openai.api_key = ""

def get_description(length, text_request):
    response = openai.Completion.create(model="text-davinci-003", prompt=text_request, temperature=0, \
                                        max_tokens=length)
    return response.get('choices')[0]['text']


def get_translation(s, target):
    translator = deepl.Translator(auth_key)
    return translator.translate_text(s, target_lang=target).text
