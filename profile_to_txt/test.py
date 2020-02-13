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
    translator = [p for (p, j) in zip(path_list,out_list) for d in j['documents'] ]
    return join_inp_json(out_list), translator


if __name__ == '__main__':
    profiles = [
             '/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/A/Achterberg, Manuel/Manuel_Achterberg_Langprofil.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/A/Ahmadi, Tareq/Ahmadi_Tareq_Profil_lang.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/A/Aschoff, Franz/Aschoff_Franz_FRA_Lang_April2018_Projektmanagement.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bellavin, Artjom/Archiv/Bellavin_Artjom_Profil_lang_Juli 2014.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bellavin, Artjom/Archiv/Bellavin_Artjom_Profil_lang_Juli 2015.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bellavin, Artjom/Bellavin_Artjom_Profil_lang_März 2016.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Berghaus, Miriam/Langprofil_Berghaus_Miriam.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Biesinger, Suzanne/Suzanne_Biesinger_Profil_lang.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Boetzel, Sascha/Bötzel_Sascha_Profil_lang_neues Template.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Boetzel, Sascha/Profil_Sascha_Bötzel_lang für BD2.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Borchart, Frank/Langprofil_Frank Borchart.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Borchart, Frank/Langprofil_Frank Borchart_neu.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bornefeld, Michael/Cassini_Bornefeld_Michael_Profil_lang.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Braun, Marc/00_Arichiv/Marc Braun Langprofil.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Braun, Marc/Marc Braun Langprofil.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Breidenbach, Kevin/Breidenbach_Kevin_Langprofil.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Breuninger, Moritz/Langprofil Moritz Breuninger.docx'
            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Brzoska, Michael/Archiv/Michael_Brzoska_Langprofil_DB.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Brzoska, Michael/Archiv/Michael_Brzoska_Langprofil_SC.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Brzoska, Michael/Archiv/Michael_Brzoska_Langprofil_neu.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Brzoska, Michael/Michael_Brzoska_Langprofil_SC - 2018.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Brzoska, Michael/Michael_Brzoska_Langprofil_SC - 2019.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/Bubel_Mirko_DUS_Profil_lang_Betrieb.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/Bubel_Mirko_DUS_Profil_lang_fuer_Architektur.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/Bubel_Mirko_DUS_Profil_lang_fuer_Architektur_072017.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/Bubel_Mirko_DUS_Profil_lang_fuer_BD2.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/Bubel_Mirko_Profil_lang_neues Template.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/archiv/Bubel_Mirko_DUS_Profil_lang_07_2013.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bubel, Mirko/archiv/Bubel_Mirko_DUS_Profil_lang_ZIVIT_NEU.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Buer, Amy/2020_01_Amy_Buer_Projektmanagerin_Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bula, Henryk/Archiv/Bula_Henryk_Profil_lang_neues Template.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bula, Henryk/Archiv/Langprofil_HenrykBula_BD2.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Bula, Henryk/Langprofil_HenrykBula_20170314.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/B/Busche, Christopher/Busche_Christopher_Profil_lang_2018.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Can, Özgür/CC_Can_Özgür_Langprofil_v3.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Canzek, Hrvoje/CC_Canzek_Hrvoje_Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Caputo Crapa, Nando/CC_Caputo-Crapa_Nando_Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Caputo Crapa, Nando/CC_Caputo-Crapa_Nando_Langprofil_1119.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Cierpiol, Marie-Luise/CC_Cierpiol_Marie-Luise_Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Conrad, Mathias/Conrad_Mathias_Profil_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Cordes, Stefan/Archiv/stefan_cordes_langprofil_lotto.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Corts, Lucas/Corts_Lucas_Profil_Lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/C/Cun, Gonca/CAS_Gonca_CGN_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dahlen, Christoph/Dahlen, Christoph Maria - Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dahlen, Christoph/spezifische Profile/Dahlen, Christoph Langprofil für Henkel.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Daut, Patrick/Daut_Patrick_Profil_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dierich, Anika/Langprofil_AnikaDierich.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dietrich, Holger/Archiv/BA_Dietrich_Holger_Profil_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dietrich, Holger/Archiv/Dietrich_Holger_Profil_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dietrich, Holger/Archiv/Dietrich_Holger_Profil_lang_ING-Diba.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dietrich, Holger/Dietrich_Holger_Profil_lang.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dittmeier, Hannah/Archiv/Langprofil_Hannah Dittmeier.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dittmeier, Hannah/Langprofil_Hannah Dittmeier_2017.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dollekamp, Patrick/Dollekamp_Patrick_Langprofil.docx'
#            ,'/Users/cassini/Cassini AG/CAS Mitarbeiterprofile - Dokumente/D/Dufhues, Stephan/2019-01_Stephan_Dufhues_Langprofil.docx'
         ]

    json_list, translator = generate_json_list(profiles)
    translate_table = [ (j['id'], t) for (j,t) in zip(json_list['documents'], translator)]
    for (i,t) in translate_table:
        print(f'{i:02} {t}')
    print(analyse_json_list(json_list))

