import base64

def extract_base64_part(file_name):
    parts = file_name.split(".")
    return parts[-2]

def calculate_start_offsets(file_name):
    encoded = extract_base64_part(file_name)
    r = base64.urlsafe_b64decode(encoded + '==')[16:]
    r1 = int.from_bytes(r[:8], "little")
    r2 = int.from_bytes(r[8:], "little")
    sp1 = r1%0x900000
    sp2 = r2%0x9FFC00

    return (sp1, sp2)

