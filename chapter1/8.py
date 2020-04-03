def cipher(ch):
    return chr(219 - ord(ch)) if ord("a") <= ord(ch) and ord(ch) <= ord("z") else ch


print("".join(map(cipher, list("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))))
