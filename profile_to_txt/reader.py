import xml.etree.ElementTree as ET
import numpy as np
import zipfile
import re

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

def clean_text(text):
    res = text

    url = re.compile('https?://[^ \t\n\r\f\v]*[^.]')
    dot_spaces = re.compile('(\\. )+')
    komma_spaces = re.compile('(, )+')
    space_dot = re.compile(' \\.')
    space_komma = re.compile(' ,')
    komma_dot = re.compile(',\\.')
    number = re.compile('[(]?(?<=[ .,])[0-9()+\\-/]*(?=[ .,])')
    symbol = re.compile('(?<= )[()/?+\\-=](?= )')
    spaces = re.compile(' +')
    letter = re.compile(' [a-zA-Z] ')
    colon_dot = re.compile(':\\.')
    dots = re.compile('\\.\\.+')
    email = re.compile('[^ ]*@[^ ]*')
    brackets = re.compile('[\\[\\]()]')

    res = re.sub(url, '', res)
    res = re.sub(email, ' ', res)
    res = re.sub(number, '', res)
    res = re.sub(symbol, '', res)
    res = re.sub(letter, '', res)
    res = re.sub(spaces, ' ', res)
    res = re.sub(dot_spaces, '. ', res)
    res = re.sub(komma_spaces, ', ', res)
    res = re.sub(space_dot, '.', res)
    res = re.sub(space_komma, ',', res)
    res = re.sub(colon_dot, ':', res)
    res = re.sub(dots, '.', res)
    res = re.sub(komma_dot, '.', res)
    res = re.sub(spaces, ' ', res)
    return res

def read_docx(path):
    docx = zipfile.ZipFile(path)
    root = ET.fromstring(docx.read('word/document.xml'))

    txt = ' '.join(extract_text(root).split())
    return clean_text(txt)

if __name__ == '__main__':
    print(read_docx('../agd_profil.docx'))
    print(clean_text('Bla https://my.web.site/pusteblume. . . and so on 0049 (0)211 123-456 on 10 / 1894, , '))
