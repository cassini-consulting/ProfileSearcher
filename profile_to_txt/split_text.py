# TODO:
#   - split at spaces, where possible, otherwise just split.
def split_text(txt, length):
    inp = txt
    out = []

    while len(inp)>length:
        out.append(inp[:length])
        inp = inp[length:]

    if len(inp)>0:
        out.append(inp)

    return out


def create_inp_json(text, ata_max_len = 5120, language='de'):
    text_list = split_text(text, ata_max_len)
#    print(text_list)
    docs = [
            {'language': language, 'id': i+1, 'text': t}
            for (i,t) in enumerate(text_list)
            ]
    return {'documents': docs }


def join_inp_json(json_list):
    ''' Join input jsons, using the language of the first document. '''
    i = 0 # counter for the documents
    docs_out = []
    language = json_list[0]['documents'][0]['language']
    for j in json_list:
        docs = j['documents']
        for d in docs:
            i = i + 1
            docs_out.append({'language': language, 'id': i, 'text': d['text']})
    return {'documents': docs_out}


if __name__ == '__main__':
    print(split_text('This is my text.', 5))
    print(create_inp_json('This is my text.', 5))
    l = [create_inp_json('This is my first text.', 5), create_inp_json('This is my second text.', 5)]
    print(join_inp_json(l))
