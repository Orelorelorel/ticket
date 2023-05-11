import openpyxl
import json
from datetime import datetime
import pandas as pd

def extract_service_from_account(account):
    keywords = {
        'epa': 'EPA',
        'zmi': 'ZMI',
        'ldc': 'LDC',
        'nhn': 'NHN',
        'nhx': 'NHX',
        'elh': 'ELH',
        'epc': 'EPC',
        'mmu': 'MMU',
        'sso': 'SSO',
        'sto': 'STO',
        'sot': 'SOT',
        'ehe': 'EHE',
        'met': 'MET',
        'aug': 'AUG',
        'w16': 'W16',
        'emo': 'EMO',
        'eat': 'EAT',
        'eli': 'ELI',
        'fbu': 'FBU',
        'ebe': 'EBE',
        'ebc': 'EBC',
        'eso': 'ESO',
        'dis': 'DIS',
        'upr': 'UPR',
        'ame': 'AME',
        'bncs': 'BNCS',
        'oma': 'OMA',
        'ebu': 'EBU',
        'epr': 'EPR',
        'war': 'WAR',
        'gfx': "GFX"
    }
    for keyword, service in keywords.items():
        if keyword in account:
            return service
    return 'Service inconnu'

def get_email_for_service(service):
    email_mapping = {
        'EPA': 'mav@eurosport.com',
        'ZMI': 'yurij.gazzola@wbd.com + marco.domante_guest@it.emglive.com + michele_chiarulli@discovery.com',
        'LDC': 'service3@example.com',
        'NHN': 'service4@example.com',
        'NHX': 'jeroen_roeper@discovery.com',
        'ELH': 'mav@eurosport.com',
        'EPC': 'mav@eurosport.com',
        'MMU': 'jochen_eberlein@discovery.com + helmar_schmidt@discovery.com',
        'SSO': 'service9@example.com',
        'STO': 'tomas.vileaholm@wbd.com + jacob.mueller@wbd.com',
        'SOT': 'service11@example.com',
        'EHE': 'service12@example.com',
        'MET': 'ismael.gonzalez@wbd.com + laura.martin@wbd.com',
        'AUG': 'service14@example.com',
        'W16': 'service15@example.com',
        'EMO': 'maxim.yanchevsky@wbdcontractor.com',
        'EAT': 'mbolierakis@eurosport-tv.gr',
        'ELI': 'service18@example.com',
        'FBU': 'gszabo@eusp.hu',
        'EBE': 'marija@alterrights.com',
        'EBC': 'service21@example.com',
        'ESO': 'lyubomir.chochov@dolimediastudio.com',
        'DIS': 'bagis.erten@gmail.com',
        'UPR': 'roman8575@gmail.com',
        'AME': 'dl_m2p_playout@discovery.com',
        'BNCS': 'louis.marrel@wbd.com',
        'OMA': 'ismael.gonzalez@wbd.com + laura.martin@wbd.com',
        'EBU': 'ionut@digitalbroadcast.ro',
        'EPR': 'service29@example.com',
        'GFX': 'luc.duhamel@wbd.com',
        "WAR": "testemail@email.com",
        'others': 'service30@example.com'  # Adresse e-mail pour les autres services
    }

    return email_mapping.get(service, 'Adresse inconnue')

def split_epa_perimeters(entry):
    keywords = {
        "coretech": ["pcr", "lt", "gfx"],
        "audiotech": ["scr"],
    }

    if entry['service'] == "EPA":
        for perimeter, keyword_list in keywords.items():
            if any(keyword in entry['service account'] for keyword in keyword_list):
                if perimeter == "coretech":
                    entry["perimeter"] = perimeter
                    entry['email'] = "dl_core_technology_engineering@discovery.com"
                elif perimeter == "audiotech":
                    entry["perimeter"] = perimeter
                    entry['email'] = "jerome.bordier@wbd.com"
                else:
                    entry["perimeter"] = perimeter
                break
        else:
            entry["perimeter"] = "epa"
    else:
        entry["perimeter"] = entry["service"].lower()

    return entry

def sort_after_epa(entry):
    keywords = {
        "viz_accounts": ["nhnwapgfx", "nhnwapgfx", "nhnzapgfxhub", "nhnzapviz", "epawapgfx", "nhnzapviz", "viz","nhngfx","gfx_eng"],
        "playout": [],
        "postprod": ["ame", "stratus"],
        "livetouch": []
    }
    emails = {
        "viz_accounts": "luc.duhamel@wbd.com",
        "playout": "dl_m2p_playout@discovery.com",
        "postprod": "dl_m2p_postprod@discovery.com",
        "livetouch": "luc.duhamel@wbd.com"
    }
    for perimeter, keyword_list in keywords.items():
        if any(keyword in entry['service account'] for keyword in keyword_list):
            entry["perimeter"] = perimeter
            entry["email"] = emails[perimeter]
        else:
            pass

    return entry

def json_dump_accounts(entries):
    with open('data_accounts.json', 'w') as file:
        json.dump(entries, file)

def create_perimeter_dataframes(data):
    perimeter_dataframes = {}

    for entry in data:
        perimeter = entry['perimeter']

        if perimeter in perimeter_dataframes:
            df = perimeter_dataframes[perimeter]
            df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
            perimeter_dataframes[perimeter] = df
        else:
            df = pd.DataFrame([entry])
            perimeter_dataframes[perimeter] = df

    return perimeter_dataframes


def extract_password_v2(xlsx_file):
    wb = openpyxl.load_workbook(xlsx_file)
    sheet = wb.active

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        expiration_date = row[8]  # Colonne I (indexée à partir de 0)
        account = row[6]  # Colonne G (indexée à partir de 0)
        if expiration_date is not None and account is not None:
            service = extract_service_from_account(account)
            if expiration_date != "PWDExpires":
                entry = {
                    'expiration date': expiration_date,
                    'service account': account.lower(),
                    'service': service,
                    'email': get_email_for_service(service),
                    "perimeter": None
                }
                entry['expiration date'] = entry['expiration date'].strftime('%Y-%m-%d')
                entry = split_epa_perimeters(entry)
                entry = sort_after_epa(entry)
                data.append(entry)

    # for entries in data:
    #     print(entries)

    perimeter_dataframes = create_perimeter_dataframes(data)
    return perimeter_dataframes


xlsx_file = "test tools.xlsx"

def save_dataframes_to_txt(dataframes, filename):
    with open(filename, 'w') as file:
        for perimeter, df in dataframes.items():
            file.write(f"Perimeter: {perimeter}\n")
            file.write(df.to_string(index=False))
            file.write("\n\n")


def create_html_dataframes(dataframes):
    html_dataframes = {}
    for perimeter, df in dataframes.items():
        html_table = df.to_html(index=False)
        html_dataframes[perimeter] = html_table
    return html_dataframes

dataframes = extract_password_v2(xlsx_file)
save_dataframes_to_txt(dataframes, 'data.txt')

