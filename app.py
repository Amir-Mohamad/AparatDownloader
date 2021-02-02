import requests
from bs4 import BeautifulSoup
import re
from AparatDownloader.exceptions import QualityError

qualities = {
	'144': 0,
	'240': 1,
	'360': 2,
	'480': 3,
	'720': 4,
	'1080': 5
}



class Scraper:
    def __init__(self, url, quality):
        self.url = url
        self.quality = quality

    def all_links(self):
        page = requests.get(self.url)
        content = BeautifulSoup(page.text, 'html.parser')
        videoLinks = content.findAll('a', href=re.compile('.mp4'))
        links = [links['href'] for link in videoLinks]
        return links

    def get_video_link(self):
        """
            This will get the given video link in mian.py
        """
        links = self.all_links()
        all_qualities = self.get_video_qualities()
        if self.quality not in availble_video_qualities:
			raise QualityError(f'This quality is not avalable \n available qualities are {availble_video_qualities}')
		else:
			link = links[qualities[self.quality]]
			return link
    
    def get_video_qualities(self):
        """
            this funciton will get the given video qualities
        """
        links = self.all_links()
		qualities = list(qualities.keys())
        availble_video_qualities = []
		for i in range(len(links)):
			availble_video_qualities.append(qualities[i])
		return availble_video_qualities

