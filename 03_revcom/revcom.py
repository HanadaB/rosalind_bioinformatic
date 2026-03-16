"""Reverse complement of DNA and RNA"""

import sys

def reverse_complement_dna(seq : str) -> str:
    return seq.strip().upper().translate(str.maketrans("ACGT" , "TGCA"))

def reverse_complement_rna(seq : str) -> str:
    table = str.maketrans("ACGU" , "UGCA")
    return seq.strip().upper().translate(table)[::-1]

def read_input() -> str:
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            return f.read()

    if not sys.stdin.isatty():
        return sys.stdin.read()

    return input("Enter your DNA or RNA sequence: ")

def main():

    seq = read_input()

    if "U" in seq:
        print(f"Reverse complement of RNA is:\n {reverse_complement_rna(seq)}")

    else:
        print(f"Reverse complement of DNA is:\n {reverse_complement_dna(seq)}")

if __name__ == "__main__" :
    main()

