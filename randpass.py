
dictFile = "/usr/share/dict/words"
minWordLen = 4
maxWordLen = 10

##########################################################################################

def read_in_all_words(fname):
  inFile = open(dictFile)
  words = []
  for line in inFile:
    # remove trailing newline
    line = line.strip()
    # skip words that are too short or too long
    lineLen = len(line)
    if lineLen < minWordLen or lineLen > maxWordLen:
      continue
    words.append(line)
  return words

##########################################################################################

import random

def main():
  words = read_in_all_words(dictFile)
  numWords = len(words)
  # do forever...
  while True:
    # pick 3 random words
    password = []
    for i in range(3):
      index = random.randint(0, numWords-1)
      password.append(words[index])
    # join them together seperated by spaces and print
    print(' '.join(password))


##########################################################################################

main()
