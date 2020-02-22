#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

KEY_FILE = './watson/python/visual_recognition/mykey.json'
VERSION = '2018-03-19'

IMAGE_PATH = './datasets/imagens/'
OUT_GENERAL_DATA = './watson/python/visual_recognition/out/{0}_general.json'
OUT_EXPLICIT_DATA = './watson/python/visual_recognition/out/{0}_explicit.json'

with open(KEY_FILE) as json_file:
    mykey = json.load(json_file)

authenticator = IAMAuthenticator(mykey["key"])
visual_recognition = VisualRecognitionV3(version=VERSION, authenticator=authenticator)
visual_recognition.set_service_url(mykey["url"])
#visual_recognition.disable_SSL_verification()

pathlist = Path(IMAGE_PATH).glob('**/*.jpg')
for path in pathlist:
    image_file = str(path)

    image_name = image_file.split('\\')[-1].split('.')[0]

    with open(image_file, 'rb') as image:
        general_data = visual_recognition.classify(images_file=image, threshold=0.6, classifier_ids='default').get_result()

    with open(OUT_GENERAL_DATA.format(image_name), 'w') as out_file:
        out_file.write(json.dumps(general_data, indent=2))

    with open(image_file, 'rb') as image:
        explicit_data = visual_recognition.classify(images_file=image, threshold=0.75, classifier_ids='explicit').get_result()

    with open(OUT_EXPLICIT_DATA.format(image_name), 'w') as out_file:
        out_file.write(json.dumps(explicit_data, indent=2))

    explicit_classes = explicit_data['images'][0]['classifiers'][0]['classes']
    if any(x['class'] == "explicit" for x in explicit_classes):
        print(f'A imagem {image_name} é inapropriada.')
