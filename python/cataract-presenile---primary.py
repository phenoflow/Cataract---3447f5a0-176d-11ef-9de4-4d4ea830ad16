# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F461z00","system":"readv2"},{"code":"F460.00","system":"readv2"},{"code":"F461000","system":"readv2"},{"code":"F460200","system":"readv2"},{"code":"F461800","system":"readv2"},{"code":"FyuE000","system":"readv2"},{"code":"F461y00","system":"readv2"},{"code":"F461.00","system":"readv2"},{"code":"H26.0","system":"readv2"},{"code":"H25","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cataract-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cataract-presenile---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cataract-presenile---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cataract-presenile---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
