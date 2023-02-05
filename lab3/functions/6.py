def rev_sent(sent):
    s = sent.split(' ')[::-1]
    print (" ".join(s))
sent = input()
rev_sent(sent)