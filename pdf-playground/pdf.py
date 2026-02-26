#import pypdf
# 
#template = pypdf.PdfReader(open('superduper.pdf', 'rb'))
#watermark = pypdf.PdfReader(open('water.pdf', 'rb'))
#output = pypdf.PdfWriter()
# 
#for i in range(len(template.pages)):
#    page = template.pages[i]
#    page.merge_page(watermark.pages[0])
#    output.add_page(page)
# 
#with open('watermaked_output.pdf', 'wb') as outputFile:
#    output.write(outputFile)

import pypdf
import sys
#with open('dummy.pdf', 'rb') as file:
#    reader = pypdf.PdfReader(file)
#    print(reader.get_page(0).rotate(180)) 
#    writer = pypdf.PdfWriter()
#    writer.add_page(reader.get_page(0).rotate(90))
#    with open('tilt.pdf', 'wb') as new_file:
#        writer.write(new_file)


inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = pypdf.PdfWriter()
    merger.wat
    for pdf in pdf_list:        
        merger.append(pdf)
    merger.write("super.pdf")

pdf_combiner(inputs)