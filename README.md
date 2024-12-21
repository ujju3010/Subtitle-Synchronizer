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
```

### Usage
1. Extract audio from your video using FFmpeg:
   ```bash
   ffmpeg -i input_video.mp4 -q:a 0 -map a audio.wav
   ```
2. Run the script to synchronize subtitles:
   ```bash
   python sync_subtitles.py --video input_video.mp4 --subtitle input_subs.srt --output output_subs.srt
   ```

### Project Structure
```
subtitle-synchronizer/
├── sync_subtitles.py          # Main script for subtitle synchronization
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── examples/                  # Example video and subtitle files
├── outputs/                   # Output subtitle files
└── LICENSE                    # License file
```

### How It Works
1. **Audio Extraction**: Extract audio from video using FFmpeg.
2. **Speech-to-Text Transcription**: Transcribe the audio to text using Google Speech-to-Text.
3. **Subtitle Parsing**: Parse SRT subtitle files to extract timestamps and text.
4. **Alignment**: Match subtitles with the transcribed audio to calculate offsets.
5. **Output**: Generate a new SRT file with corrected timestamps.

### Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

### License
This project is licensed under the MIT License.

### Contact
For questions or suggestions:
- **Email**: your-email@example.com
- **GitHub**: [your-username](https://github.com/your-username)
