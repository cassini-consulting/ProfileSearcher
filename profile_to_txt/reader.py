import xml.etree.ElementTree as ET
import numpy as np
import zipfile

def extract_text(root):
    if root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t':
        txt = root.text
    elif root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br': 
        txt = ' '
    elif root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tab': 
        txt = ' '
    elif root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p':
        txt = '. '
    else:
        txt = ''

    if txt is None:
        txt = ''

    for sub in root:
        txt += extract_text(sub)

    return txt

def read_docx(path):
    docx = zipfile.ZipFile(path)
    root = ET.fromstring(docx.read('word/document.xml'))

    txt = ' '.join(extract_text(root).split())
    return txt

if __name__ == '__main__':
    print(read_docx('../agd_profil.docx'))
