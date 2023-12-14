from bitcoin import sha256
import requests

# fetch 2048 words
res = requests.get("https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt")
arr = res.text.strip().split('\n')

# 23 words selected
words_23 = 'aerobic bulk nice flip focus exit pause census globe garden vacant thumb guard live note whisper fringe snack absent certain prefer worth around'

# 23 words to 253 bits
list = words_23.split(' ')
bits253 = ''
for i in range(len(list)) :
    num = arr.index(list[i])
    bits253 += bin(num)[2:].zfill(11)


for i in range(8) :
    # 3bit for padding
    padding = bin(i)[2:].zfill(3)
    
    # 256 bit entropy
    hexStr = hex(int(bits253 + padding, 2))[2:].zfill(64)
    
    # sha256 of entropy
    entropy_hash = sha256(bytes.fromhex(hexStr))
    
    # first checksum 8bit of hash
    checksumHex = entropy_hash[:2]
    checksumDec = int(checksumHex, 16)
    checksumBin = bin(checksumDec)[2:].zfill(8)
    
    # index of 24 word
    index = int(padding + checksumBin, 2)
    
    # last word
    print(arr[index])