

def makedict():
    with open('file_read.txt') as f:
        words = [i.strip().lower() for i in f.read().split()]
        return dict(zip(words[:-1], words[1:]))

makedict()

print (makedict())
