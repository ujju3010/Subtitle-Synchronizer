# Subtitle Synchronizer

An automated tool to fix subtitle timing issues and ensure perfect synchronization with video files. This project processes a video file and an out-of-sync subtitle file, generating a corrected subtitle file as output.

## Features
- Automatically aligns subtitles with video dialogue.
- Supports common video formats like MP4 and MKV.
- Processes subtitles in SRT format.
- Uses speech-to-text transcription for precise synchronization.

## Demo
![Demo](link_to_demo_gif_or_image)

## Getting Started

### Prerequisites
1. **Python 3.7+**: Install Python from [python.org](https://www.python.org/).
2. **FFmpeg**: Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/).
3. **Google Speech-to-Text API**: Set up your API credentials:
   - Create a Google Cloud account.
   - Enable the Speech-to-Text API.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable with the path to your service account key.

### Installation
Clone this repository and install the required dependencies:
```bash
git clone https://github.com/your-username/subtitle-synchronizer.git
cd subtitle-synchronizer
pip install -r requirements.txt
