from bitcoin import sha256
import requests

# fetch 2048 words
res = requests.get("https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt")
arr = res.text.strip().split('\n')

# 11 words selected
words_11 = 'garden vacant thumb guard live note whisper fringe snack absent certain'

# 11 words to 121 bits
list = words_11.split(' ')
bits121 = ''
for i in range(len(list)) :
    num = arr.index(list[i])
    bits121 += bin(num)[2:].zfill(11)


for i in range(128) :  # 2^7 = 128
    # 3bit for padding
    padding = bin(i)[2:].zfill(7)
    
    # 128 bit entropy
    hexStr = hex(int(bits121 + padding, 2))[2:].zfill(32)
    
    # sha256 of entropy
    entropy_hash = sha256(bytes.fromhex(hexStr))
    
    # first checksum 4bit of hash
    checksumHex = entropy_hash[:1]
    checksumDec = int(checksumHex, 16)
    checksumBin = bin(checksumDec)[2:].zfill(4)
    
    # index of 12 word
    index = int(padding + checksumBin, 2)
    
    # last word
    print(arr[index])