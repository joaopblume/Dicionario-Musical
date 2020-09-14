# Dicionário musical
 Programa com o objetivo de ajudar estudandes de música no geral, mostrando as notas formadoras das tríades e/ou as sétimas dos acordes de acordo com o acorde requerido.

# Como funciona a formação de um Acorde;
Um acorde é formado pela sua nota fundamental (que dá o nome ao acorde), por seu terceiro grau e seu quinto grau dentro de uma escala. As escalas são definidas por uma sequência de 8 notas selecionadas dentro de [C, C#, D, D#, E, F, F# G, G#, A, A#, B, C], formadas de tom, tom, semitom, tom, tom, tom, semitom, a partir da nota desejada. (Cada tom é composto por dois semitons.) 
Logo uma escala de dó maior (C) seria:
C
C + Tom = D
C + Tom + Tom = E
C + Tom + Tom + semitom = F
C + Tom + Tom + semitom + Tom = G
C + Tom + Tom + semitom + Tom + Tom = A
C + Tom + Tom + semitom + Tom + Tom + Tom = B
C + Tom + Tom + semitom + Tom + Tom + Tom + semitom = C (uma oitava acima) 

[C, D, E, F, G, A, B, C] onde sua nota fundamental, terça e quinta são C, E e G respectivamente.

Em acordes menores, sua terça fica um semitom abaixo, então a terça de dó menor (Cm) é D#.

# Lógica da matemática no programa;
Como a sequência de terças, quintas e sétima seguem o mesmo padrão, apenas precisamos numerar a escala cromática [C, C#, D, D#, E, F, F# G, G#, A, A#, B, C] em índices, sendo cada semi tom correspondente à um índice exato. 
Assim, toda terça (que fica 2 tons de diferença da nota fundamental) tem um intervalo absoluto de 4 semitons, ou 4 índices. Sua quinta (que fica 3 tons e um semitom de diferença da nota fundamental) tem um intervalo de 7 semitons, e assim por diante. 
A mudança ocorre apenas quando o acorde é menor, onde a terça do acorde se encontra num intervalo de 3 semitons.

A partir daí fica simples varrer, encontrar e aplicar um grau de um acorde dentro da lista criada, o resto é tudo lógica de programação. 