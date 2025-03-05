from argparse import ArgumentParser
from cowsay import cowsay

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', default='default')
    parser.add_argument('-e', default='oo')
    parser.add_argument('-n', action='store_true')
    parser.add_argument('-F', default='default')
    parser.add_argument('-E', default='oo')
    parser.add_argument('-N', action='store_true')
    parser.add_argument('msg_1', type=str)
    parser.add_argument('msg_2', type=str)
    args = parser.parse_args()
    print(args)
    cow1 = cowsay(message=args.msg_1,
                  cow=args.f,
                  eyes=args.e).split("\n")
    cow2 = cowsay(message=args.msg_2,
                  cow=args.F,
                  eyes=args.E).split("\n")
    strlen1, strlen2 = len(cow1), len(cow2)
    print(strlen1, strlen2)
    if strlen1 > strlen2:
        print('\n'.join(i for i in cow1[:strlen1 - strlen2]))
        cow1 = cow1[strlen1 - strlen2:]
        strlen1 = strlen2
    elif strlen1 != strlen2:
        print('\n'.join(' ' * len(max(cow1, key=len)) +
              i for i in cow2[:strlen2 - strlen1]))
        cow2 = cow2[strlen2 - strlen1:]
        strlen2 = strlen1
    for i in range(strlen1):
        print(cow1[i] + ' ' * (len(max(cow1, key=len)) - len(cow1[i])) + cow2[i])
