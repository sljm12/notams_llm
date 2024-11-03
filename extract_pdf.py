from pypdf import PdfReader
from notam import extract_notam

reader = PdfReader("singapore-notam-list-oct-2024.pdf")
page = reader.pages[7]
#print(page.extract_text())

notams = extract_notam(page.extract_text())

for i, n in enumerate(notams):
    print(str(i)+":")
    print('\n'.join(n))
    print()