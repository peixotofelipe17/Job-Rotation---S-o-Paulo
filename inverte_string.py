def inverte_string(string_inserida):
    string_invertida = string_inserida[::-1]
    print(string_invertida)

def main():
    string_inserida = input("Entre com a string de sua preferência: ")
    inverte_string(string_inserida)
main()