import re

output = open('zet hier nieuwe file naam uit voor de resultaten','a')
n = 0

with open('zet hier een xml file dat uit het blast script is gekregen','r') as xml:
        # looped over het xml file en stript als die specifiece lines tegen komt
        # deze lines worden uiteindelijk toegevoegd aan een file die file wrdt dan gebruikt
        # voor alle resultaten
        for line in xml:
            if re.search('<Iteration_query-def>', line) != None:
                n = n + 1
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Iteration_query-def>')
                line = line.rstrip('</')
                query_def = line
            if re.search('No hits found', line) != None:
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Iteration_message>')
                line = line.rstrip('</')
                print(n)
                print(output, query_def+'\t'+line)
            if re.search('<Hit_def>', line) != None:
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Hit_def>')
                line = line.rstrip('</')
                if '&gt;' in line:
                    line1 = line.split('&gt;')
                    hit_def = line1[0]
                else:
                    hit_def = line
            if re.search('<Hit_accession>', line) != None:
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Hit_accession>')
                line = line.rstrip('</')
                hit_acc = line
            if re.search('<Hsp_score>', line) != None:
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Hsp_score>')
                line = line.rstrip('</')
                score = line
            if re.search('<Hsp_evalue>', line) != None:
                line = line.strip()
                line = line.rstrip()
                line = line.strip('<Hsp_evalue>')
                line = line.rstrip('</')
                e_val = line
                # Schrijft hier alles op in een nieuwe file dat bovenaan een naam heeft gekregen
                output.write(str(n)+'\t'+query_def+'\t'+hit_def+'\t'+hit_acc+'\t'+e_val+'\t'+score+'\n')

output.close()
