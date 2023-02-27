#include <stdio.h>

int nmr0 = 0;
int nmr1 = 1;
int soma;


int calcula_fibonacci(int* nmr_recebido) {
    int achou = 0;

    printf("%d\n", *nmr_recebido);

    while(soma <= *nmr_recebido) {
        if (soma == *nmr_recebido) {
        achou = 1;
        break;
        }
        soma = nmr0 + nmr1;
        nmr0 = nmr1;
        nmr1 = soma;
    }
    return achou;
}

int main() {
    int nmr_recebido;
    printf("Entre com o numero que deseja: ");
    scanf("%d", &nmr_recebido);

    int achou = calcula_fibonacci(&nmr_recebido);

    if (achou) {
        printf("O numero %d pertence a sequencia de Fibonacci!", nmr_recebido);
    }
    else {
        printf("O numero %d nao pertence a sequencia de Fibonacci", nmr_recebido);
    }
}