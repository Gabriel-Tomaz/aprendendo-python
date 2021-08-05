phrase = input('Digite uma frase: ').strip().upper()

print('A letra A aprece {} vezes na frase'.format(phrase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(phrase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(phrase.rfind('A')+1))