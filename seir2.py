import sys
import requests
from bs4 import BeautifulSoup

def body_text(url):
    res= requests.get(url)
    bs= BeautifulSoup(res.text,"html.parser")
    if bs.body:
        return bs.body.get_text(" ")
    return ""


def w_freq(text):
    text=text.lower()

    freq={}
    curr_word=""

    for ch in text:
        if ch.isalnum():
            curr_word += ch
        else:
            if curr_word != "":
                if curr_word in freq:
                    freq[curr_word] += 1
                else:
                    freq[curr_word] = 1
                curr_word = ""

    if curr_word != "":
        if curr_word in freq:
            freq[curr_word] += 1
        else:
            freq[curr_word] = 1

    return freq

def sim_hash(freq_dict):
    vector=[]
    for i in range(64):
        vector.append(0)

    for word in freq_dict:
        count=freq_dict[word]
        p=53
        m=2**64
        hash_val=0
        power=1
        i = 0
        while i < len(word):
            ch = word[i]
            ascii_val= ord(ch)
            term = ascii_val* power
            hash_val += term
            hash_val %= m
            power = power * p
            power = power % m
            i = i + 1

        j=0
        while j< 64:
            if hash_val & 1<< j :
                vector[j] += count
            else:
                vector[j] -= count
            j+= 1
   
    simhash=0
    for i in range(64):
        if vector[i] > 0:
            simhash |= (1 << i)
    return simhash
# def sim_hash(freq_dict):
#     vector = [0] * 64

#     p = 53
#     m = 2**64

#     for word, count in freq_dict.items():
#         hash_val = 0
#         power = 1

#         for ch in word:
#             hash_val = (hash_val + ord(ch) * power) % m
#             power = (power * p) % m

#         for i in range(64):
#             if hash_val & (1 << i):
#                 vector[i] += count
#             else:
#                 vector[i] -= count

    
#     simhash=0
#     for i in range(64):
#         if vector[i] > 0:
#             simhash |= (1 << i)

#     return simhash

def common_bits(hash1, hash2):
    x = hash1 ^ hash2
    diff= bin(x).count('1')
    return 64 - diff


def main():
    if len(sys.argv) < 3:
        return

    u1 = sys.argv[1]
    u2 = sys.argv[2]

    t1 = body_text(u1)
    t2 = body_text(u2)

    freq1 = w_freq(t1)
    freq2 = w_freq(t2)

    s1 = sim_hash(freq1)
    s2 = sim_hash(freq2)

    common = common_bits(s1,s2)

    print("Common bits in simhash:", common)


if __name__ == "__main__":
    main()