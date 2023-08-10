# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"F350.00","system":"readv2"},{"code":"J3A..00","system":"readv2"},{"code":"J3A0.00","system":"readv2"},{"code":"J3A1.00","system":"readv2"},{"code":"J3A2.00","system":"readv2"},{"code":"J3A3.00","system":"readv2"},{"code":"J3Ay.00","system":"readv2"},{"code":"J3Az.00","system":"readv2"},{"code":"N12C400","system":"readv2"},{"code":"N143.00","system":"readv2"},{"code":"N143.11","system":"readv2"},{"code":"353","system":"oxmis"},{"code":"353 HP","system":"oxmis"},{"code":"353 PP","system":"oxmis"},{"code":"353 T","system":"oxmis"},{"code":"5518AT","system":"oxmis"},{"code":"7251D","system":"oxmis"},{"code":"7289A","system":"oxmis"},{"code":"7289D","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('back-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["back-pain-sciatica---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["back-pain-sciatica---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["back-pain-sciatica---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
