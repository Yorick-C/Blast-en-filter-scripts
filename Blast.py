from Bio.Blast import NCBIWWW, NCBIXML
import time
import re


def run_blast():
    """
    Functie die een fasta bestand pakt inleest en een timer begint
    :return:
    """
    with open("Hier je blast sequenties zetten in fasta formaat", "r") as fasta:
        start = time.time()
        blast(fasta.read())
        print(time.time() - start)


def blast(seq: str):
    """
    Functie die blast begint en het omzet tot een nieuwe file
    :return: een xml file met de blast resultaten
    """
    # print de sequenties die gevonden zijn in het fasta bestand
    print(seq)
    # Voert een blastx uit met parameters van een e-value treshhold van 0,05
    # en gelimiteerde list van 10
    res = NCBIWWW.qblast("blastx", "nr", seq, expect=0.05, hitlist_size=10)
    print("Done")
    # maakt een nieuwe xml file aan als die klaar is
    with open("geef de naam van het nieuwe xml file aan met .xml", "a+") as file:
        file.write(res.read())


if __name__ == "__main__":
    run_blast()
  
