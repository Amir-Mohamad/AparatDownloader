# The Main Script
from AparatDownloader.app import Scraper
import requests



class Main:
	def __init__(self, url, quality):
		self.url = url
		self.quality = quality
		self.scraper = Scraper(url, quality)

	def downloadVideo(self):
        # get video url
		videoUrl = str(self.scraper.get_link())
		videoName = videoUrl.split('/')
		with open(videoName[4], 'wb') as f:

			print('video is downloading..')
			result = requests.get(videoUrl, stream=True)

			totalLength = result.headers.get('content-length')
			if totalLength is None:
				f.write(result.content)
			else:
				downloadVideo = 0
				totalLength = int(totalLength)
				for data in result.iter_content(chunk_size=4096):
					downloadVideo += len(data)
					f.write(data)
					done = int(50*downloadVideo / totalLength)
					print("\r[%s%s]" % ('=' * done, ' ' * (50-done)), end=''

		print('\nVideo downloaded !!!\n Enjoy :)')