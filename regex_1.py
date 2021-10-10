# O link REGEX é: https://www.youtube.com/watch?v=Jao4VwJCByk&t=135s
# Regular Expression HOWTO: https://docs.python.org/3/howto/regex.html

# Importando a biblioteca
import re


print("#######################")
print("# CARACTERES NO REGEX #")
print("#######################")
# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."
texto = '''
arera
arEDDYra
arTOPra
ar\nra
arMAMÁra
arDATAra
'''
#texto = 'areddyra'
t = re.compile('ar....ra') # Procurar::começa com "ar" "tanto faz" termina com "ra"
check = t.findall(texto) # findall vai procurar isso em nosso texto
print("O método me traz uma lista: ")
print(check)

# NOTA: É importante usar o "r" (row string). Para pegar apenas coisas ligadas ao REGEX e não a outro carater, etc  

print("#############")
print("# Exemplo 2 #")
print("#############")
# ^  - Irá testar o início da string
# [^]  -Irá considerar todos os caracteres EXCETO o indicado
texto = 'arEddyara'
p = re.compile('^a') # Traz as palavras (ou string) que começam com "a"
t = re.compile(r'[^a]') # Traz todos menos os "a"
q = re.compile(r'^a')
check_p = p.findall(texto)
check = t.findall(texto)
check1= q.findall(texto)
print(check_p,'\n' ,check,'\n',check1)


print("#############")
print("# Exemplo 3 #")
print("#############")
# \d - Qualquer caracter que SEJA um algarismo  de 0 a 9
# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
texto = 'arara1992-04-1981'
t = re.compile(r'\d')
q = re.compile(r'\D')
check = t.findall(texto)
check1= q.findall(texto)
print(check,'\n',check1)