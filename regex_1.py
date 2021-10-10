# O link REGEX é: https://www.youtube.com/watch?v=Jao4VwJCByk&t=135s
# Regular Expression HOWTO: https://docs.python.org/3/howto/regex.html

# Importando a biblioteca
import re


print("#######################")
print("# CARACTERES NO REGEX #")
print("#######################")
# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."
texto = 'arbra'
t = re.compile('ar.ra') # Procurar::começa com "ar" "tanto faz" termina com "ra"
check = t.findall(texto) # Este vai nosso padrão de busca
print(check)

