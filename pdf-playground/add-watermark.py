import pypdf
import sys

stamp = pypdf.PdfReader("wtr.pdf").pages[0]
writer = pypdf.PdfWriter(clone_from="super.pdf")

for page in writer.pages:
    page.merge_page(stamp, over=False)

writer.write("super-watermark.pdf")