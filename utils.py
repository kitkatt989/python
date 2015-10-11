import types
import pyPdf
import os

def retriveMeta(fn):
	pdf = pyPdf.PdfFileReader(file(fn, 'rb'))
	info = pdf.getDocumentInfo()
	print '[*] PDF Metadata: {0}'.format(fn)
	print pdf.resolvedObjects
	for item, dat in info.items():
		try:
			print '[+] {0}: {1}'.format(item, pdf.resolvedObjects[0][1][item])
		except:
			print '[+] {0}: {1}'.format(item, dat)