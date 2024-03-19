import sys
import base64

file_name = sys.argv[1]

r = base64.urlsafe_b64decode(file_name + '=' * (4 - len(file_name) % 4))[16:]
r1 = int.from_bytes(r[:8], "little")
r2 = int.from_bytes(r[8:], "little")
sp1 = r1%0x900000
sp2 = r2%0x9FFC00

print("Offset 1:", hex(sp1))
print("Offset 2:", hex(sp2))