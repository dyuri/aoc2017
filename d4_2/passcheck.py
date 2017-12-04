PASSPHRASES = []

with open('passphrases.txt') as f:
    PASSPHRASES = [p.strip() for p in f.readlines()]


def check_passphrase(passphrase):
    uniqe_phrases = set()
    phrases = passphrase.split()

    for p in phrases:
        uniqe_phrases.add(''.join(sorted(p)))

    return len(phrases) == len(uniqe_phrases)


valid_passphrases = filter(check_passphrase, PASSPHRASES)

print(len(list(valid_passphrases)))
