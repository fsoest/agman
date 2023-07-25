import json
from agreement import Agreement
from datetime import date

with open('edgg_loas', 'r') as f:
    contents = json.loads(f.read())

agr = Agreement(**contents[20])
agr.edit_date = str(date.today())
contents[20] = agr.__dict__
with open('edgg_loas', 'w') as fout:
    json.dump(contents, fout, indent=0)