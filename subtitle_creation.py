# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:30:13 2022

@author: soyrl
"""
    
# This code is used for extracting subtitles from a video file using the OpenAI whisper library.

# https://openai.com/blog/whisper/
# Models in https://github.com/openai/whisper/discussions/63

import whisper
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# For English-only applications, the .en models tend to perform better, especially for the tiny.en 
# and base.en models. We observed that the difference becomes less significant for the small.en and 
# medium.en models. Other models also perform language identification. Default selection is 'small' model
# In my laptop NVIDIA GeForce GTX 1660 Ti with 6BG VRAM it takes ~35min for an 1hour audio file (2.5mins for tiny).
# To use the 'large' model for other languages only option for now is Colab (10GB VRAM needed). 

# According to Reddit users whisper does not perform speaker diarization. 
# Also, sometimes we get censored data (fucking as f**king) most likely because some of the training data
# has it censored and some doesn't and it just picks semi-randomly
# https://www.reddit.com/r/MachineLearning/comments/xl7mfy/d_some_openai_whisper_benchmarks_for_runtime_and/

# The user is prompted to select a video file for extracting subtitles.
print("Please select video file to extract subtitles from: ")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
video_file = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# The user is prompted to select a whisper model. The '.en.pt' models tend to perform better for English.
print("Please select model - '.en.pt' models tend to perform better for English: ")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
model_path = askopenfilename()

# The video file is converted to audio.
#https://stackoverflow.com/questions/33448759/python-converting-video-to-audio
import moviepy.editor as mp
clip = mp.VideoFileClip(video_file)
clip.audio.write_audiofile("audio.mp3")

#Whisper to transcribe audio of any language (or even translate to English)
model = whisper.load_model(model_path) 
result = model.transcribe("audio.mp3", language='en') #If language not English we should specify it if model!=large. We should also add 'task='translate''.
print("Transcription has finished")

#Code below copied from the following:
#https://www.codingforentrepreneurs.com/blog/getting-started-with-openai-whisper/

import datetime

# A function is defined to convert datetime.timedelta to match the format of vtt timecodes.
def timedelta_to_videotime(delta):
    """
    Here's a janky way to format a
    datetime.timedelta to match
    the format of vtt timecodes.
    """
    parts = delta.split(":")
    if len(parts[0]) == 1:
        parts[0] = f"0{parts[0]}"
        new_data = ":".join(parts)
        parts2 = new_data.split(".")
    if len(parts2) == 1:
        parts2.append("000")
    elif len(parts2) == 2:
        parts2[1] = parts2[1][:2]
    final_data = ".".join(parts2)
    return final_data

# A function is defined to format whisper segments into WebVTT format.
def whisper_segments_to_vtt_data(result_segments):
    """
    This function iterates through all whisper
    segements to format them into WebVTT.
    """
    data = "" #"WEBVTT\n\n"
    for idx, segment in enumerate(result_segments):
        num = idx + 1
        data+= f"{num}\n"
        start_ = datetime.timedelta(seconds=segment.get('start'))
        start_ = timedelta_to_videotime(str(start_))
        end_ = datetime.timedelta(seconds=segment.get('end'))
        end_ = timedelta_to_videotime(str(end_))
        data += f"{start_} --> {end_}\n"
        text = segment.get('text').strip()
        data += f"{text}\n\n"
    return data

#Text transcribed from audio in srt format
caption_data = whisper_segments_to_vtt_data(result['segments'])

#Write that in srt file
with open("/".join(video_file.split('.')[:-1])+'_transcribed_en'+".srt", "w",encoding='utf-8') as text_file:
    text_file.write(caption_data)
    
#For a per word translation look at https://github.com/johnafish/whisperer    
#which was found in discussion in https://github.com/openai/whisper/discussions/3