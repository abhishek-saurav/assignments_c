a = int(input("Enter input A (0 or 1): "))
b = int(input("Enter input B (0 or 1): "))

and_gate = a & b
or_gate = a | b
xor_gate = a ^ b
not_a = 1 - a
not_b = 1 - b
nand_gate = 1 - (a & b)
nor_gate = 1 - (a | b)

print("AND gate:", and_gate)
print("OR gate:", or_gate)
print("XOR gate:", xor_gate)
print("NOT A:", not_a)
print("NOT B:", not_b)
print("NAND gate:", nand_gate)
print("NOR gate:", nor_gate)
