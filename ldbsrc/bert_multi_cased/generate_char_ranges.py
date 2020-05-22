import unicodedata

#
# This script computes a set of letters that are from vocab words of the vocab.txt
#  if a token is a single letter token, then we don't include Chinese characters and punctuations
#  since they never go in a sequence
#

def is_bert_chinese(l):
    # [\x3400-\x4DBF\x4E00-\x9FFF\xF900-\xFAFF\x20000-\x2A6DF\x2A700-\x2B73F\x2B740-\x2B81F\x2B820-\x2CEAF\x2F800-\x2FA1F]
    i = ord(l)
    if  (i >= 0x3400 and i <=0x4DBF) or (i >= 0x4E00 and i <=0x9FFF) or \
        (i >= 0xF900 and i <=0xFAFF) or (i >= 0x20000 and i <=0x2A6DF) or \
        (i >= 0x2A700 and i <=0x2B73F) or (i >= 0x2B740 and i <=0x2B81F) or \
        (i >= 0x2B820 and i <=0x2CEAF) or (i >= 0x2F800 and i <=0x2FA1F):
        return True
    return False

def is_punctuation(char): 
    """Checks whether `chars` is a punctuation character.""" 
    cp = ord(char) 
    # We treat all non-letter/number ASCII as punctuation. 
    # Characters such as "^", "$", and "`" are not in the Unicode 
    # Punctuation class but we treat them as punctuation anyways, for 
    # consistency. 
    if ((cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or 
        (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126)): 
      return True 
    cat = unicodedata.category(char) 
    if cat.startswith("P"): 
      return True 
    return False

ranges=[]

def my_hex(i):
    return "\\" + "{0:#0{1}x}".format(i, 6)[1:]

start = -1
end = -1
prev_char = -1
for c in range(0x10ffff):
    ch = chr(c)
    if is_bert_chinese(ch) or is_punctuation(ch):
        if start != -1:
            if (start != prev_char):
                print(my_hex(start) + "-" + my_hex(prev_char), end="")
            else:
                print(my_hex(start), end="")
        start = -1
    else:
        if start == -1:
            start = c
    prev_char = c

print("\n\n\n\n\n\n\nPuncutation ranges")
start = -1
end = -1
prev_char = -1
for c in range(0x10ffff):
    ch = chr(c)
    if not is_punctuation(ch):
        if start != -1:
            if (start != prev_char):
                print(my_hex(start) + "-" + my_hex(prev_char),end="")
            else:
                print(my_hex(start),end="")
        start = -1
    else:
        if start == -1:
            start = c
    prev_char = c





