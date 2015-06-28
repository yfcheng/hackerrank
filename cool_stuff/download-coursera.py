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
	html = open('coursera.html','r')
	content = html.readlines()
	html_content = ""
	for line in content:
                html_content += line
                html_content += "\n"
	print html_content
	#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+mp4+?', html_content)
	urls = re.findall(r'href=[\'"]?([^\'" >]+)', html_content)
	urls = ["https://class.coursera.org/algs4partI-2012-001/lecture/download.mp4?lecture_id=45"]
	for url in urls:
                print url
		downloadfile(url)
	print "Download completed"
if __name__ == "__main__":
	main()
