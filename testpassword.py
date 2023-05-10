import openpyxl
import json
from datetime import datetime

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
    coretech_keywords = ["pcr", "lt", "gfx"]
    audiotech_keywords = ["scr"]
    viz_accounts_keyword = ["NHNWAPGFX","NHNWAPGFX","NHNZAPGFXHUB","NHNZAPVIZ","EPAWAPGFX","NHNZAPVIZ"]

    if entry['service'] == "EPA" and any(keyword in entry['service account'] for keyword in coretech_keywords):
        entry["perimeter"] = "coretech"
        entry['email'] = "dl_core_technology_engineering@discovery.com"
    elif entry['service'] == "EPA" and any(keyword in entry['service account'] for keyword in audiotech_keywords):
        entry["perimeter"] = "audiotech"
        entry['email'] = "jerome.bordier@wbd.com"
    elif any(keyword in entry['service account'] for keyword in viz_accounts_keyword):
        entry["perimeter"] = "coretech"
        entry['email'] = "luc.duhamel@wbd.com"
    else:
        entry["perimeter"] = "none"

    return entry

def json_dump_accounts(entries):
    with open('data_accounts.json', 'w') as file:
        json.dump(entries, file)

def extract_password(xlsx_file):
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
                    'service account': account,
                    'service': service,
                    'email': get_email_for_service(service),
                    "perimeter": None
                }
                entry['expiration date'] = entry['expiration date'].strftime('%Y-%m-%d')
                entry = split_epa_perimeters(entry)
                data.append(entry)

    json_dump_accounts(data)

    for entry in data:
        print(f"Expiration date: {entry['expiration date']}")
        print(f"Service account: {entry['service account']}")
        print(f"Service: {entry['service']}")
        print(f"Email: {entry['email']}")
        print(f"Perimeter: {entry['perimeter']}")
        print()





extract_password("test.xlsx")


