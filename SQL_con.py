def main():
    filter()


def filter():
    with open('result35-80.txt', 'r') as file:
        read_lijst = []
        eiwit_lijst = []
        taxonomy_lijst = []
        accesie_lijst = []
        e_value_lijst = []
        score_lijst = []
        for line in file:
            line = line.split('\t')
            if int(line[0]) % 2 > 0:
                read = 'FW'
            elif int(line[0]) % 2 == 0:
                read = 'RV'
            else:
                print(line[0])
            line[2] = line[2].replace(']', '')
            eiwit = line[2].split('[')
            taxonomy = eiwit[1]
            eiwit = eiwit[0]
            accesie = line[3]
            e_value = line[4]
            score = line[5]
            read_lijst.append(read)
            eiwit_lijst.append(eiwit)
            taxonomy_lijst.append(taxonomy)
            accesie_lijst.append(accesie)
            e_value_lijst.append(e_value)
            score = score.replace('\n', '')
            score_lijst.append(score)

        print(read_lijst)
        print(eiwit_lijst)
        print(taxonomy_lijst)
        print(accesie_lijst)
        print(e_value_lijst)
        print(score_lijst)


main()