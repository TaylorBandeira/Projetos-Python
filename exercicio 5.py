from colorama import Fore, Style, init

init()

N = float(input("Digite sua primeira nota: "))
N2 = float(input("Digite sua segunda nota: "))
N3 = float(input("Digite sua terceira nota: "))

MEDIA = (N + N2 + N3) /2
print(float(MEDIA))

if MEDIA >= 7:
    print(Fore.GREEN + "aprovado" + Style.RESET_ALL)
else :
    print(Fore.RED + "reprovado" + Style.RESET_ALL)