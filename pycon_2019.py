from art import tprint

connect = f"{'32'*4}47323267427878696784{'32'*26}9210"
the = f"60{'32'*8}847269{'32'*4}42{'32'*48}6210"
pythonista = f"{'32'*6}92323280898472427873838465323247"

for word in (connect, the, pythonista):
    tprint("".join(chr(int(word[i - 2 : i])) for i in range(2, len(word) + 1, 2)))
