# automatosDePilha-simulador
Simulador Universal de Autômatos de Pilha Não-Determinísticos (APs)

## Exemplo: 
### Entrada
```
3
3 a b c
3 B A Z
1 2
12
0 a Z 0 AZ
0 a B 0 AB
0 a A 0 AA
0 b Z 0 BZ
0 b B 0 BB
0 b A 0 BA
0 c B 1 B
0 c A 1 A
0 c Z 1 Z
1 a A 1 -
1 b B 1 -
1 - Z 2 Z
10
abbcbba
aabbcbbaa
bbabbacbbabbb
bbbbbcbbbbbb
-
abababababab
bbbbacabbbb
abba
c
aaa
```

### Saída desejada
```
aceita
aceita
rejeita
rejeita
rejeita
rejeita
aceita
rejeita
aceita
rejeita
```
