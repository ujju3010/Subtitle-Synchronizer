import os
import pysrt
import argparse
from google.cloud import speech
import ffmpeg

def extract_audio(video_path, audio_path):
    ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)

def transcribe_audio(audio_path):
    client = speech.SpeechClient()
    with open(audio_path, 'rb') as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code='en-US',
        enable_automatic_punctuation=True
    )
    response = client.recognize(config=config, audio=audio)
    transcript = []
    for result in response.results:
        transcript.append(result.alternatives[0].transcript)
    return ' '.join(transcript)

def adjust_subtitles(subtitle_path, transcript):
    subs = pysrt.open(subtitle_path)
    for sub in subs:
        sub.text = transcript
    return subs

def save_corrected_subtitles(subs, output_path):
    subs.save(output_path, encoding='utf-8')

def main(video, subtitle, output):
    audio_path = 'audio.wav'
    extract_audio(video, audio_path)
    transcript = transcribe_audio(audio_path)
    adjusted_subs = adjust_subtitles(subtitle, transcript)
    save_corrected_subtitles(adjusted_subs, output)
    os.remove(audio_path)
    print(f'Corrected subtitles saved to {output}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Synchronize subtitles with video.')
    parser.add_argument('--video', required=True, help='Path to the input video file.')
    parser.add_argument('--subtitle', required=True, help='Path to the input subtitle file.')
    parser.add_argument('--output', required=True, help='Path to the output corrected subtitle file.')
    args = parser.parse_args()

    main(args.video, args.subtitle, args.output)
