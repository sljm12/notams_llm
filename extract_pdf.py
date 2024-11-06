from pypdf import PdfReader
from notam import extract_notam
from argparse import ArgumentParser
from pprint import pprint
import json

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-o","--output", help="Output JSON Filename")
    parser.add_argument("-p","--page",help="Page number to extract")
    args = parser.parse_args()
    print(args)
    
    reader = PdfReader(args.filename)
    page = reader.pages[int(args.page)-1]
    #print(page.extract_text())

    notams = extract_notam(page.extract_text())
    if args.output is None:
        for i, n in enumerate(notams):
            print(str(i)+":")
            print('\n'.join(n))
            print()
    else:
        with open(args.output,'w') as f:
            notams_strings = ['\n'.join(i) for i in notams]
            json.dump(notams_strings, f, indent=4)

