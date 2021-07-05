#!/bin/python

import sys
import os
from textblob import TextBlob
import subprocess

header = sys.stdin.buffer.read(78)
counter=4
while(1):
    if counter%2==0:
        #data = sys.stdin.buffer.read(882000) #5 sec
        data = sys.stdin.buffer.read(3528000) #20 sec
        f = open("/tmp/inter.wav", "wb")
        f.write(header)
        f.write(data)
        f.close()
        os.system("ffmpeg -y -i /tmp/inter.wav -f wav /tmp/inter_f.wav 2> /dev/null")

        File="/tmp/inter_f.wav"

        os.system("deepspeech --model deepspeech-0.9.3-models.pbmm --scorer deepspeech-0.9.3-models.scorer --audio "+File+" > buffText.txt")
        f = open("buffText.txt")
        deta = f.readlines()[0].strip()
        f.close()
        analysis = TextBlob(deta)
        if analysis.detect_language() != 'en':
            print("Translating to English!")
            output = subprocess.check_output(['trans', '-b', deta])
            deta = output.decode('utf-8').strip()
            analysis = TextBlob(deta)

        f = open("deepText.txt","a")
        f.write(deta+","+str(analysis.sentiment.polarity)+"\n")
        f.close()

    else:
        data = sys.stdin.buffer.read(176400)
        f = open("/tmp/inter.wav", "wb")
        f.write(header)
        f.write(data)
        f.close()
        os.system("ffmpeg -y -i /tmp/inter.wav -f wav /tmp/inter_f.wav 2> /dev/null")
    counter+=1
