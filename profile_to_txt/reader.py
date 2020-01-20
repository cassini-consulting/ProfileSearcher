import xml.etree.ElementTree as ET
import numpy as np
import zipfile

def extract_text(root):
    txt = root.text
    if txt is None:
        txt = ''
    else:
        txt = ' '.join(txt.split())

    if root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br':
        txt = ' '
    elif root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr':
        txt = ' '

    for sub in root:
        txt += extract_text(sub)

    if root.tag=='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p':
        txt = ' ' + txt + ' '

    return txt

def read_docx(path):
    docx = zipfile.ZipFile(path)
    root = ET.fromstring(docx.read('word/document.xml'))

    txt = ' '.join(extract_text(root).split())
    return txt
