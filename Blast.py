from Bio.Blast import NCBIWWW, NCBIXML
import time
import re


def run_blast():
    with open("blast89-90.fasta", "r") as fasta:
        start = time.time()
        blast(fasta.read())
        print(time.time() - start)


def blast(seq: str):
    print(seq)
    res = NCBIWWW.qblast("blastx", "nr", seq, expect=0.05, hitlist_size=10)
    print("Done")
    with open("89-90blast.xml", "a+") as file:
        file.write(res.read())


def read_blast():
    result = open("85-86blast.xml")
    record_list = list(NCBIXML.parse(result))
    print(record_list)
    for record in record_list:
        print(f"\n{record}"
              f"\n{record.descriptions}")
        if len(record.alignments):
            print(len(record.alignments))
            for alignment in record.alignments:
                desc_info = get_desc_info(alignment.title)
                print(f"\n\tDescription: {desc_info['description']}")
                for hsp in alignment.hsps:
                    print(f"\tOrganism: {desc_info['organism']}\n"
                          f"\tAccession: {desc_info['accession']}\n"
                          f"\tE-value: {hsp.expect}\n"
                          f"\tScore: {hsp.score}")
        else:
            print("No matches found.")


def get_desc_info(full_desc: str):
    full_desc = re.match(r".+?\]", full_desc)[0]
    organism = re.search(r'(?<=\[).+?(?=])', full_desc)[0]
    accession = re.search(r"(?<=\|).+?(?=\|)", full_desc)[0]
    desc = re.search(r"(?<=\|).+?(?=\|)", full_desc)[0]
    return {"organism": organism, "accession": accession, "description": desc}


if __name__ == "__main__":
    run_blast()
    # read_blast()

# seq = "ACGATGGACTGCATCATGTTACAACAACTCCCTCTACCCTACGTCACTTCCTCTGCTCGCTC \
#     TGCCCACCCACTTTTCTTCATTATTACCCCACAGGCTCCCAGACACCTGTATTTGCCATTCC \
#    GTCGACCGCGACATGGCAGGAGTTCCCGGTGCAACAAAAGAACCCTTGAGAAACTCGCTCGA \
#   GGAGGCACGACCGTGTCACAGACCGCTACACAAAAAGATTTGCGCATTCGAAGCATTGATAT \
#  TAGCGAAGGCGCGACACGAGCGCCGAACCGCGCCATGTTACGGGACGTCGGCT"
# blast(seq)


# def blast(seq):
#   print("Start BLAST")
# result_handle = NCBIWWW.qblast("blastn", "nr", seq)
#  print("BLAST resultaat in variabele")
# blast_records = NCBIXML.parse(result_handle)
# print(blast_records)
# with open("blast.xml", "w") as out_handle:
# out_handle.write(result_handle.read())

# with open("blast.xml", "r") as out_handle:
#    blast_records = NCBIXML.parse(out_handle)
#   blast_records = next(blast_records)
#  eval_threshold = 0.05
# for alignment in blast_records.alignments:
#    for hsp in alignment.hsps:
#       if hsp.expect < eval_threshold:
#          print("***Alignment***")
#         print("sequentie: ", alignment.title)
#        print("Length: ", alignment.length)
#       print("E value: ", hsp.expect)
