import sys
import base64 
from base64 import urlsafe_b64encode

def calculate_start_offsets(file_name):
    r = base64.urlsafe_b64decode(file_name)[16:]
    r1 = int.from_bytes(r[:8], "little")
    r2 = int.from_bytes(r[8:], "little")
    sp1 = r1%0x900000
    sp2 = r2%0x9FFC00

    return (hex(sp1), hex(sp2))

