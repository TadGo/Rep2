def get_help():
    print('podaj trzy liczby:')


def dodawanie(a, b, c):
    wynik = a + b + c
    return wynik


get_help()
zm1 = int(input())
zm2 = int(input())
zm3 = int(input())
print(dodawanie(zm1, zm2, zm3))
