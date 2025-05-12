# YT_DLP - YouTube Downloader Library

A Python library for downloading audio or video from YouTube using `yt-dlp`. This tool supports downloading from text files, lists of links, and CSV files.

## Table of Contents
1. [Installation](#installation)
2. [Features](#features)
3. [Usage](#usage)
   - [Basic Initialization](#basic-initialization)
   - [Download from a Text File](#download-from-a-text-file)
   - [Download from a List of Links](#download-from-a-list-of-links)
   - [Download from a CSV File](#download-from-a-csv-file)
4. [Configuration Options](#configuration-options)
5. [Folder Structure](#folder-structure)
6. [Examples](#examples)
7. [Dependencies](#dependencies)

---

## Installation

Install the required dependencies:

```bash
pip install yt-dlp tqdm ffmpeg-python
```

Or using requirements.txt:
```
yt-dlp>=2023.11.16
tqdm>=4.66.1
ffmpeg-python>=0.2.0
```

## Features

- Download YouTube videos as MP4 files
- Extract audio as MP3 files
- Support for multiple input sources:
  - Text files (.txt)
  - CSV files
  - Direct URL lists
- Progress tracking with tqdm
- Automatic folder creation
- Google Colab compatible

## Usage

### Basic Initialization

```python
from yt_dlp_wrapper import YouTubeDownloader

# For audio downloads (default)
downloader = YouTubeDownloader(download_type='audio')

# For video downloads
downloader = YouTubeDownloader(download_type='video')

# Custom save location
downloader = YouTubeDownloader(save_folder='/path/to/custom/folder')
```

### Download from a Text File

```python
downloader.download_from_file('videos.txt')
```

Example input file (videos.txt):
```
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2
```

### Download from a List of Links

```python
links = [
    "https://www.youtube.com/watch?v=example1",
    "https://www.youtube.com/watch?v=example2"
]
downloader.download_from_list(links)
```

### Download from a CSV File

```python
downloader.download_from_csv('videos.csv', column_name='url')
```

Example CSV file:
```csv
id,title,url
1,Video 1,https://www.youtube.com/watch?v=example1
2,Video 2,https://www.youtube.com/watch?v=example2
```

## Configuration Options

| Parameter       | Default Value | Description |
|----------------|---------------|-------------|
| `download_type` | 'audio'       | 'audio' for MP3, 'video' for MP4 |
| `save_folder`   | None          | Custom save location (auto-created if not exists) |
| `audio_quality` | '192'         | Audio bitrate when downloading audio |
| `video_quality` | 'best'        | Video quality preference |

Example with custom quality:
```python
downloader = YouTubeDownloader(
    download_type='audio',
    audio_quality='320'  # Higher quality MP3
)
```

## Folder Structure

Downloads are saved in the following structure:

Google Colab:
```
/content/
└── YouTube_Downloaded/
    ├── video1.mp3 (or .mp4)
    └── video2.mp3 (or .mp4)
```

Local Environment:
```
./YouTube_Downloaded/
    ├── video1.mp3 (or .mp4)
    └── video2.mp3 (or .mp4)
```

## Examples

### 1. Download High Quality Audio

```python
from yt_dlp_wrapper import YouTubeDownloader

downloader = YouTubeDownloader(
    download_type='audio',
    audio_quality='320'
)

links = [
    "https://www.youtube.com/watch?v=7Gzdo107SmE",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
]

downloader.download_from_list(links)
```

### 2. Download HD Videos

```python
from yt_dlp_wrapper import YouTubeDownloader

downloader = YouTubeDownloader(
    download_type='video',
    save_folder='./HD_Videos'
)

downloader.download_from_file('hd_videos.txt')
```

## Dependencies

- `yt-dlp`: YouTube content downloader (actively maintained fork of youtube-dl)
- `tqdm`: Progress bar visualization
- `ffmpeg-python`: Audio/video processing

For full functionality, ensure FFmpeg is installed on your system:
- Linux: `sudo apt install ffmpeg`
- Windows: Download from [FFmpeg official site](https://ffmpeg.org/)
- Mac: `brew install ffmpeg`

## Troubleshooting

1. **FFmpeg not found**:
   - Install FFmpeg system-wide
   - Or specify path in options: `'ffmpeg_location': '/path/to/ffmpeg'`

2. **Download errors**:
   - Check URL availability
   - Try different quality settings
   - Update yt-dlp: `pip install --upgrade yt-dlp`

3. **Permission issues**:
   - Ensure write permissions for save folder
   - Try different save location
