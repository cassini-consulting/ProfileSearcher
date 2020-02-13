from reader import *
from split_text import *
import requests
import json

# headers for text analytics
headers = {"Ocp-Apim-Subscription-Key": "dcb0d307225f4a70a5bc77be156bc529",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "cache-control": "no-cache",
    "Postman-Token": "45a3c16d-12a7-445c-8ace-545d219cbff7"
    }


def analyse_json_list(json_list):
#   with open("input.json", "r") as f:
#       data = json.loads(f.read())

    data = json_list

    url = "https://profilekeywords.cognitiveservices.azure.com/text/analytics/v2.1/keyPhrases"

    eq = requests.Request('POST', url, headers = headers, json = data)
    prepared = eq.prepare()

#    def pretty_print_POST(req):
#        """
#        At this point it is completely built and ready
#        to be fired; it is "prepared".
#    
#        However pay attention at the formatting used in
#        this function because it is programmed to be pretty
#        printed and may differ from the actual request.
#        """
#        print('{}\n{}\r\n{}\r\n\r\n{}'.format(
#            '-----------START-----------',
#            req.method + ' ' + req.url,
#            '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
#            req.body,
#        ))
#
#    pretty_print_POST(prepared)

    r = requests.post(url, headers=headers, json = data)
#    print(r.status_code, r.reason)
    return r.content.decode('utf8')


def generate_json_list(path_list):
    out_list = [create_inp_json(read_docx(p)) for p in path_list]
    return join_inp_json(out_list)


if __name__ == '__main__':
    profiles = [
            '../agd_profil.docx',
            '/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/A/Achterberg, Manuel/Manuel_Achterberg_Langprofil.docx',
            '/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/K/Kalisch, Dominik/Kalisch_Dominik_Profil_lang.docx'
            ]
    json_list = generate_json_list(profiles)
    print(analyse_json_list(json_list))

