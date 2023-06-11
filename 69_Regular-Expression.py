import re

def find_sentence_lengths(text):
    pattern = r"(?:\.{1,3}|\?|!)[\s\u202F]*(?=[A-Z\"'\(\[]|\b|$)"
    sentences = re.split(pattern, text)
    sentence_lengths = [len(sentence.strip()) for sentence in sentences]
    return sentence_lengths

text = "Hello! How are you? I am Aman Kumar Gupta. I study in IIIT Bhubaneswar."
lengths = find_sentence_lengths(text)
print(lengths)

'''
OUTPUT

[5, 11, 21, 27, 0]
'''

text = 'clone cyclone bawander aman he was going to a walk, suddenly the weather started to change like a cycone was on its way lolicon. hahahah'
m = re.findall('\w+one', text)
print(m)

'''
OUTPUT

['clone', 'cyclone', 'cycone']
'''