from argparse import ArgumentParser
import random
import urllib.request
from cowsay import cowsay

def bullcows(candidate: str, reference: str) -> (int, int):
    bulls = sum(
        1 for i in range(
            len(candidate)) if (
            i < len(reference) and candidate[i] == reference[i]))
    cows_count = sum(min(candidate.count(c), reference.count(c))
                     for c in set(candidate))
    cows = cows_count - bulls
    return bulls, cows


def ask(promt: str, valid: list[str] = None) -> str:
    word = input(promt)
    if valid is None or word in valid:
        return word
    print("Недопустимое слово, попробуйте снова.")


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay(message=format_string.format(bulls, cows)))


def file_read(filepath: str, length: int = 5) -> list[str]:
    words = []
    with open(filepath, 'r', encoding='utf-8')as f:
        for line in f:
            word = line.strip("\n")
            if len(word) == length:
                words.append(word)
    return words


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    candidate = ""
    attempts = 0
    reference = words[random.randint(0, len(words) - 1)]
    while (candidate != reference):
        attempts += 1
        candidate = ask("Введите слово:")
        if len(candidate) == 0:
            print("Вы не ввели слово")
            continue
        bulls, cows = bullcows(candidate, reference)
        inform("Быки: {}, Коровы: {}", bulls, cows)
    return attempts


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('dict', help="Пожалуйста введите словарь")
    parser.add_argument('length', default=5, type=int, nargs='?')
    args = parser.parse_args()
    filepath = 'dict.txt'
    if args.dict.startswith('http'):
        urllib.request.urlretrieve(args.dict, filepath)
        words = file_read(filepath, args.length)
    else:
        words = file_read(args.dict, args.length)
    attempts = gameplay(ask, inform, words)
    print("Вы выйграли! Количество попыток: {}".format(attempts))
