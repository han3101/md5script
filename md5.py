import hashlib
import config

HASH = config.HASH
salt = config.salt


def main():
    with open("7letterwords.txt") as file:
        for word in file:
            flag = word.replace("\n", "") + salt
            guess = hashlib.md5(flag.encode('utf-8')).hexdigest()
            # print(guess)
            # print(guess)
            if guess.lower() == HASH:
                print(word)
                exit(0)

if __name__ == '__main__':
    main()