# YT_DLIB - YouTube Downloader Library

A Python library for downloading audio from YouTube videos using `yt-dlp`. This tool supports downloading from text files, lists of links, and CSV files.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Download from a Text File](#download-from-a-text-file)
   - [Download from a List of Links](#download-from-a-list-of-links)
   - [Download from a CSV File](#download-from-a-csv-file)
3. [Folder Structure](#folder-structure)
4. [Examples](#examples)
5. [Dependencies](#dependencies)

---

## Installation

Before using the library, ensure all required dependencies are installed. Run the following command:

```bash
pip install -r requirements.txt
```

The requirements.txt file includes:
```
yt-dlp==2025.3.31
tqdm==4.66.1
ffmpeg-python==0.2.0
```

Usage
Download from a Text File

You can download videos by providing a text file containing one video URL per line.

Example Code:
```
from downloader import YouTubeDownloader

downloader = YouTubeDownloader()
downloader.download_from_file('examples/videos.txt')
```

Example Input (videos.txt):
```
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2
```

Download from a List of Links

You can also pass a Python list of video URLs directly to the downloader.

Example Code:
```
from downloader import YouTubeDownloader

links = [
    "https://www.youtube.com/watch?v=example1",
    "https://www.youtube.com/watch?v=example2"
]

downloader = YouTubeDownloader()
downloader.download_from_list(links)
```


Download from a CSV File

If you have a CSV file with a column containing video URLs, you can specify the column name to extract the links.

Example Code:
```
from downloader import YouTubeDownloader

downloader = YouTubeDownloader()
downloader.download_from_csv('examples/videos.csv', column_name='url')
```

Example Input (videos.csv):
```
url
https://www.youtube.com/watch?v=example1
https://www.youtube.com/watch?v=example2
```

Folder Structure

After running the script, the downloaded files will be saved in the following folders:

In Google Colab:
```
/content/
└── YouTube_Downloaded/
    ├── example1.mp3
    └── example2.mp3
```

Locally:
```
.
└── YouTube_Downloaded/
    ├── example1.mp3
    └── example2.mp3
```

Dependencies 

Ensure the following dependencies are installed: 

    yt-dlp : A powerful YouTube downloader.
    tqdm : For progress bars during downloads.
    ffmpeg-python : For audio extraction and processing.
     

Install them using the requirements.txt file: 
```
pip install -r requirements.txt
```
