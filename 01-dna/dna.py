""" Tetranucleotide frequency """

dna = input("Enter your DNA sequence:").strip().upper()

a = dna.count("A")
c = dna.count("C")
g = dna.count("G")
t = dna.count("T")

print(f"DNA sequence contains:\n A:{a}\n C:{c}\n G:{g}\n T:{t}")






