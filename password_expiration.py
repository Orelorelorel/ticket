import openpyxl

def extract_password(xlsx_file):
    wb = openpyxl.load_workbook(xlsx_file)
    feuille = wb.active
    every_accounts = []

    for cellule_i, cellule_g in zip(feuille['I'], feuille['G']):
        valeur_i = cellule_i.value
        valeur_g = cellule_g.value
        if valeur_i is not None:
            account_dict = {
                "expiration date": valeur_i,
                "service account" : valeur_g
            }
            every_accounts.append(account_dict)
        else:
            pass

    allowed_values_epa = []
    allowed_values_zmi = []
    allowed_values_ldc = []
    allowed_values_nhn = []
    allowed_values_nhx = []
    allowed_values_elh = []
    allowed_values_epc = []
    allowed_values_mmu = []
    allowed_values_sso = []
    allowed_values_sto = []
    allowed_values_sot = []
    allowed_values_ehe = []
    allowed_values_met = []
    allowed_values_aug = []
    allowed_values_w16 = []
    allowed_values_emo = []
    allowed_values_eat = []
    allowed_values_eli = []
    allowed_values_fbu = []
    allowed_values_ebe = []
    allowed_values_ebc = []
    allowed_values_eso = []
    allowed_values_dis = []
    allowed_values_upr = []
    allowed_values_ame = []
    allowed_values_bncs = []
    allowed_values_others = []
    allowed_values_oma = []
    allowed_values_epr = []
    allowed_values_ebu = []

    for account in every_accounts:
        if "epa" in account["service account"]:
            allowed_values_epa.append(account["service account"])
        elif "zmi" in account["service account"]:
            allowed_values_zmi.append(account["service account"])
        elif "ldc" in account["service account"]:
            allowed_values_ldc.append(account["service account"])
        elif "nhn" in account["service account"]:
            allowed_values_nhn.append(account["service account"])
        elif "nhx" in account["service account"]:
            allowed_values_nhx.append(account["service account"])
        elif "elh" in account["service account"]:
            allowed_values_elh.append(account["service account"])
        elif "epc" in account["service account"]:
            allowed_values_epc.append(account["service account"])
        elif "mmu" in account["service account"]:
            allowed_values_mmu.append(account["service account"])
        elif "sso" in account["service account"]:
            allowed_values_sso.append(account["service account"])
        elif "sto" in account["service account"]:
            allowed_values_sto.append(account["service account"])
        elif "sot" in account["service account"]:
            allowed_values_sot.append(account["service account"])
        elif "ehe" in account["service account"]:
            allowed_values_ehe.append(account["service account"])
        elif "met" in account["service account"]:
            allowed_values_met.append(account["service account"])
        elif "aug" in account["service account"]:
            allowed_values_aug.append(account["service account"])
        elif "w16" in account["service account"]:
            allowed_values_w16.append(account["service account"])
        elif "emo" in account["service account"]:
            allowed_values_emo.append(account["service account"])
        elif "eat" in account["service account"]:
            allowed_values_eat.append(account["service account"])
        elif "eli" in account["service account"]:
            allowed_values_eli.append(account["service account"])
        elif "fbu" in account["service account"]:
            allowed_values_fbu.append(account["service account"])
        elif "ebe" in account["service account"]:
            allowed_values_ebe.append(account["service account"])
        elif "ebc" in account["service account"]:
            allowed_values_ebc.append(account["service account"])
        elif "eso" in account["service account"]:
            allowed_values_eso.append(account["service account"])
        elif "dis" in account["service account"]:
            allowed_values_dis.append(account["service account"])
        elif "upr" in account["service account"]:
            allowed_values_upr.append(account["service account"])
        elif "ame" in account["service account"]:
            allowed_values_ame.append(account["service account"])
        elif "bncs" in account["service account"]:
            allowed_values_bncs.append(account["service account"])
        elif "oma" in account["service account"]:
            allowed_values_oma.append(account["service account"])
        elif "ebu" in account["service account"]:
            allowed_values_ebu.append(account["service account"])
        elif "epr" in account["service account"]:
            allowed_values_epr.append(account["service account"])
        else:
            allowed_values_others.append(account["service account"])

    allowed_values = {
        "epa": allowed_values_epa,
        "zmi": allowed_values_zmi,
        "ldc": allowed_values_ldc,
        "nhn": allowed_values_nhn,
        "nhx": allowed_values_nhx,
        "elh": allowed_values_elh,
        "epc": allowed_values_epc,
        "mmu": allowed_values_mmu,
        "sso": allowed_values_sso,
        "sto": allowed_values_sto,
        "sot": allowed_values_sot,
        "ehe": allowed_values_ehe,
        "met": allowed_values_met,
        "aug": allowed_values_aug,
        "w16": allowed_values_w16,
        "emo": allowed_values_emo,
        "eat": allowed_values_eat,
        "eli": allowed_values_eli,
        "fbu": allowed_values_fbu,
        "ebe": allowed_values_ebe,
        "ebc": allowed_values_ebc,
        "eso": allowed_values_eso,
        "dis": allowed_values_dis,
        "upr": allowed_values_upr,
        "ame": allowed_values_ame,
        "bncs": allowed_values_bncs,
        "oma": allowed_values_oma,
        "ebu": allowed_values_ebu,
        "epr": allowed_values_epr,
        "others": allowed_values_others
    }

    return allowed_values