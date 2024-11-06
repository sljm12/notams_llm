'''
Tested with LM Studio lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf

'''
from pypdf import PdfReader
import codecs
from glob import glob
from pathlib import Path
from openai_llm import create_openai_llm
from prompts import prompt_template1 as prompt_template
#from openai_llm import call_llm
#from googleai import call_llm

import json

llm_model = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF"

def read_file(filename):
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    results = ""
    for p in range(number_of_pages):
        page = reader.pages[p]
        text = page.extract_text()
        results = results + text
    
    return results

call_llm = create_openai_llm(prompt_template, llm_model)

def process_file(filename):
    '''
    Process file in the following order
    1. Read the pdf file and extract the text
    2. call the llm and get back the json
    3. loads the json from the llm to ensure that it is a valid json
    4. Writes the Json out
    '''
    text = read_file(filename)
    j = call_llm(text)
    print(j)
    json_obj= json.loads(j)
    j_str = json.dumps(json_obj)
    print(j_str)

    output_name = filename.replace(".pdf",".txt")
    with codecs.open(output_name,"w","UTF8") as f:
        f.write(j_str)

def extract_notam(text:str):
    '''
    Extracts NOTAM from a block of text
    '''
    lines = text.split("\n")
    temp = []
    results = []
    start = False
    for l in lines:
        if l.startswith("+"):            
            temp = [l]
            start=True
            continue
        if l.startswith("From: "):
            start = False
            temp.append(l)
            results.append(temp)
            temp = []
            continue
        if start:
            temp.append(l)
    
    return results


if __name__ == "__main__":
    files = glob("./mistral_0.2_7B/*.pdf")
    for i, f in enumerate(files):
        output_name = f.replace(".pdf",".txt")
        
            
        print(str(i) +"/" + str(len(files)) +" "+ f)
        print(output_name)
        if Path(output_name).exists():
            print("Skipping")
        else:
            process_file(f)