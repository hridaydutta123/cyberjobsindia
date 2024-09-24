import os
import pickle
from bs4 import BeautifulSoup
import html

inputDirName = 'jobs'
outputDirName = 'jobs_md'

for files in os.listdir(inputDirName):
	with open(os.path.join(inputDirName, files), 'rb') as handle:
		print('Working file:', files)
		data = pickle.load(handle)
		with open(os.path.join(outputDirName, files[:-7] + '.md'), 'w') as f:
			f.write('---\n')
			f.write('title: ' + data.title + '\n')
			f.write('linkedin_url: ' + data.link + '\n')
			f.write('company: ' + data.company + '\n')
			f.write('location: ' + data.place + '\n')
			f.write('posted_date: ' + data.date + '\n')
			f.write('---\n')
			f.write('\n')
			soup = BeautifulSoup(data.description_html, 'html.parser')
			for button in soup.find_all('button'):
				button.decompose()
			f.write(str(soup))