import json
from agreement import Agreement


def gng_import(gng_str: str):
    content = gng_str.split(':')
    if content[-1].strip()[-1] in ['^', '|']:
        at_level = False
    else:

        at_level = True
    is_altitude = False
    try:
        if int(content[-3]) < 6000:
            is_altitude = True
    except:
        pass
    try:
        if int(content[-2]) < 6000:
            is_altitude = True
    except:
        pass
    agreement = Agreement(gng_name=content[-1].strip('\n'), from_sector=content[6][6:].replace("Â·", "·"), to_sector=content[7][6:].replace("Â·", "·"), gng_notes='', sortorder=100, fix_before=content[1], dep_rwy=content[2], copx_fix=content[3], fix_after=content[4], arr_rwy=content[5], climb=content[-3], descend=content[-2], from_vacc=content[6][:4], to_vacc=content[7][:4], at_level=at_level, is_altitude=is_altitude)
    return agreement


with open('gng_copx.txt', 'r') as f:
    lines = f.readlines()
    agreements = []
    for line in lines:
        agreements.append(gng_import(line).__dict__)
    with open('edgg_loas', 'w') as fout:
        json.dump(agreements, fout, indent=0)
