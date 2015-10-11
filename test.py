import os, sys
import argparse
from pyPdf import PdfFileReader
import utils
#from utils import retriveMeta
import magic

#make path
#path = "/home/kat/Downloads/test"
#os.mkdir(path,0755);
#print "Path Created"

#parse disk_image from prompt
def main():
	parser = argparse.ArgumentParser(description = 'Extractor')
	parser.add_argument('-i','--disk_image', help = 'Specify image')
	args = parser.parse_args()
	print (args.disk_image)

#tsk_recover to extract files
	tsk_command = "tsk_recover -e" " "+args.disk_image+" "+path
	os.system(tsk_command)

for dirpath, dirname, files in os.walk("/home/kat/Downloads/test"):
	for name in files:
		fn = os.path.join(dirpath,name)
		

pdf_meta_data = utils.retriveMeta(fn)
if pdf_meta_data!={}:
	print "##############"
	print name 
	print pdf_meta_data
	print "#############"




path = "/home/kat/Downloads/test"
dirs = os.listdir( path )

for file in dirs:
	print file



if __name__ == '__main__':
	main()



#pdf_meta = PdfFileReader(open("/home/kat/Downloads/test/02 Bike Helmet Use.pdf","rb"))
#pdf_info = pdf_meta.getDocumentInfo()
#print pdf_info

#m = magic.Magic(mime = True)
#m.from_file("/home/kat/Downloads/test/02 Bike Helmet Use.pdf")
#print m