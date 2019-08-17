from art import tprint

connect = f"{'32'*4}4732323267427878696784{'32'*32}9210"
the = f"3260{'32'*9}847269{'32'*4}42{'32'*54}6210"
pythonistas = f"{'32'*6}923232808984724278738384658332323247"

for word in (connect, the, pythonistas):
    tprint("".join(chr(int(word[i - 2 : i])) for i in range(2, len(word) + 1, 2)))
