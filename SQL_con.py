def main():
    filter()


def filter():
    """
    Een functie die door een gegeven txt file loopt die verkregen is 
    van de filter.py en geeft alles weer wat er in zit in lists
    :return: visualisatie van de data in een txt file
     afkomstig van de filter.py
    """
    with open('een gegeven txt bestand', 'r') as file:
        # maakt allemaal lists aan zodat ze later gebruikt kunnen worden
        read_lijst = []
        eiwit_lijst = []
        taxonomy_lijst = []
        accesie_lijst = []
        e_value_lijst = []
        score_lijst = []
        # looped over de lines in de file en split alles
        for line in file:
            line = line.split('\t')
            # zet erbij of het een forward of reverse read is
            if int(line[0]) % 2 > 0:
                read = 'FW'
            elif int(line[0]) % 2 == 0:
                read = 'RV'
            else:
                print(line[0])
            # wgeeft alle waardes hun data doormiddel van de juiste index eraan koppelen
            line[2] = line[2].replace(']', '')
            eiwit = line[2].split('[')
            taxonomy = eiwit[1]
            eiwit = eiwit[0]
            accesie = line[3]
            e_value = line[4]
            score = line[5]
            # zet alles in de lists
            read_lijst.append(read)
            eiwit_lijst.append(eiwit)
            taxonomy_lijst.append(taxonomy)
            accesie_lijst.append(accesie)
            e_value_lijst.append(e_value)
            score = score.replace('\n', '')
            score_lijst.append(score)
        # print de lists uit voor visualisatie van de data
        print(read_lijst)
        print(eiwit_lijst)
        print(taxonomy_lijst)
        print(accesie_lijst)
        print(e_value_lijst)
        print(score_lijst)


main()
