import yt_dlp
from tqdm.notebook import tqdm
import datetime
import os
import csv

class YouTubeDownloader:
    def __init__(self, save_folder=None):
        self.save_folder = save_folder or self._create_save_folder()
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.save_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    def _is_colab(self):
        try:
            import google.colab
            return True
        except ImportError:
            return False

    def _create_save_folder(self):
        if self._is_colab():
            folder_path = '/content/YouTube_Downloaded'
        else:
            folder_path = './YouTube_Downloaded'
        
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    def download_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                links = [line.strip() for line in f if line.strip()]
            self._download(links)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def download_from_list(self, links):
        if not links:
            print("The list of links is empty.")
            return
        self._download(links)

    def download_from_csv(self, csv_path, column_name='url'):
        try:
            links = []
            with open(csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                if column_name not in reader.fieldnames:
                    print(f"Column '{column_name}' not found in the CSV file.")
                    return
                for row in reader:
                    link = row[column_name].strip()
                    if link:
                        links.append(link)
            self._download(links)
        except FileNotFoundError:
            print(f"File {csv_path} not found.")
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")

    def _download(self, links):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            for url in tqdm(links, desc="Downloading videos"):
                try:
                    ydl.download([url])
                except Exception as e:
                    print(f"Failed to download video from link {url}. Error: {e}")
