"""Transcribing DNA into mRNA"""

import sys

def transcribe_dna_to_rna(dna: str) -> str:
    return dna.replace("T" , "U").upper().strip()

def read_input() -> str:
    """
    detect where input comes from:
    1. file argument
    2. piped input
    3. manual CLI input
    """
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            return f.read()

    if not sys.stdin.isatty():
        return sys.stdin.read()

    return input("Enter your DNA sequence: ")

def main():
    dna = read_input()
    rna = transcribe_dna_to_rna(dna)
    print(f"RNA sequence: {rna}")

if __name__ == "__main__":
    main()