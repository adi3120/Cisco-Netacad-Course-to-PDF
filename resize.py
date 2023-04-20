from PIL import Image
import os
from PyPDF2 import PdfMerger

PAGE_WIDTH = 794
PAGE_HEIGHT = 1123
nums=0
for i in range(0,145):

	img = Image.open('./CyberOPS/'+str(i)+'.png')

	img_width, img_height = img.size
	aspect_ratio = img_height / img_width
	new_width = PAGE_WIDTH
	new_height = int(new_width * aspect_ratio)
	resized_img = img.resize((new_width, new_height))


	num_pages = int(new_height / PAGE_HEIGHT) + 1

	for j in range(num_pages):
		y1 = j * PAGE_HEIGHT
		y2 = (j+1) * PAGE_HEIGHT
		if y2 > new_height:
			y2 = new_height
		cropped_img = resized_img.crop((0, y1, new_width, y2))

		page_img = Image.new('RGB', (PAGE_WIDTH, PAGE_HEIGHT), color='white')
		page_img.paste(cropped_img, (0, 0))

		filename = f'page_{j+1}.pdf'
		page_img.save(filename, 'PDF')

	pdf_merger = PdfMerger()
	for j in range(num_pages):
		filename = f'page_{j+1}.pdf'
		pdf_merger.append(open(filename, 'rb'))

	pdf_merger.write(str(i)+'_output.pdf')
	nums+=1
	pdf_merger.close()

	for j in range(num_pages):
		filename = f'page_{j+1}.pdf'
		os.remove(filename)

pdf_merger = PdfMerger()
for i in range(nums):
	filename = f'{i}_output.pdf'
	pdf_merger.append(open(filename, 'rb'))
pdf_merger.write('output.pdf')
pdf_merger.close()

for i in range(nums):
	filename = f'{i}_output.pdf'
	os.remove(filename)