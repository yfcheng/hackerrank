#this utility is for downloading mp3 files from tamilbeat.com

import sys,urllib2,re

def downloadfile(url):
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,
	f.close()
	
def main():
	page = sys.argv[1]
	print "Downloading song from " + page
	response = urllib2.urlopen(page)
	html = response.read()
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+mp3', html) 
	print "Downloading song from " + urls
	for url in urls:
		downloadfile(url)
	print "Download completed"
if __name__ == "__main__":
	main()
