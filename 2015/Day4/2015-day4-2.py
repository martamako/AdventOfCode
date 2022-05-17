import hashlib

key = "ckczppom"

number = 0

while True:
    napis = key + str(number)
    napis_bytes = bytes(napis, 'utf-8')
    result = hashlib.md5(napis_bytes)

    result_in_hex = result.hexdigest()
    czesc_hasha = result_in_hex[:6]
    if czesc_hasha == "000000":
        print(number)
        break
    number += 1
