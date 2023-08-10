# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"16C4.00","system":"readv2"},{"code":"16C5.00","system":"readv2"},{"code":"16C9.00","system":"readv2"},{"code":"16CA.00","system":"readv2"},{"code":"8HTH.00","system":"readv2"},{"code":"N142.11","system":"readv2"},{"code":"N149.00","system":"readv2"},{"code":"N14y.11","system":"readv2"},{"code":"N23yE00","system":"readv2"},{"code":"7287A","system":"oxmis"},{"code":"7289C","system":"oxmis"},{"code":"7289CA","system":"oxmis"},{"code":"7289CC","system":"oxmis"},{"code":"7289CE","system":"oxmis"},{"code":"7289CI","system":"oxmis"},{"code":"7289H","system":"oxmis"},{"code":"7289J","system":"oxmis"},{"code":"7289PL","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('back-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["back-pain---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["back-pain---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["back-pain---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
