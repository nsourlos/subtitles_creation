# Video Subtitle Creation using OpenAI Whisper Library

![Alt text](./subtitle-creation.svg)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)]( https://github.com/nsourlos/subtitle_creation)


> This tool can be used to generate subtitles from any video file. Preferred language is English but trancription can be done from any other language as well. For non-English languages please use the `large` whisper model. The code for the transcription can be found [here](./subtitle_creation.py). The whisper models can be found in [this discussion](https://github.com/openai/whisper/discussions/63).

**Caution!** The original [whisper repository](https://github.com/openai/whisper) should also be downloaded and added in the folder of this repository.


## Documentation (by *Chat GPT*)

The documentation below was created by using the prompt 
> Write documentation for the following code

**Overview**

This code is used for extracting subtitles from a video file using the OpenAI Whisper library. OpenAI Whisper is a deep learning-based API that can transcribe audio in any language or even translate to English. It takes an audio file as input and returns a set of segments with their corresponding start and end times and the transcribed text.

*Requirements*

The following libraries are used in this code:

- OpenAI Whisper
- moviepy
- tkinter

**Usage**

The code prompts the user to select a video file for subtitle extraction and a Whisper model. The user is recommended to select an `.en.pt` model for better performance with English language videos. The video file is then converted to audio, and the selected Whisper model is used to transcribe the audio into text segments.

**Output**

The code outputs the transcribed text in the WebVTT format and saves it in a `.srt` file with the name `video_file_transcribed_en.srt`, where `video_file` is the name of the selected video file.

**Limitations**

According to Reddit users, Whisper does not perform speaker diarization.
The code only supports extracting subtitles in English language. To extract subtitles in other languages, the `large` model should be used, and the language should be specified in the `transcribe` method. However, using the `large` model requires a GPU with 10GB VRAM, which can only be done in Colab.
The code sometimes returns censored data (e.g., "fucking as f**king") due to the inconsistency of censored data in the training data used by Whisper.

The performance of the Whisper model varies depending on the size of the model and the processing power of the GPU. On a laptop with NVIDIA GeForce GTX 1660 Ti with 6GB VRAM, it takes approximately 35 minutes to transcribe a 1-hour video (2.5 minutes for the `tiny` model). The performance difference between the different models becomes less significant for the `small` and `medium` models.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

 
## License
[MIT License](LICENSE)
