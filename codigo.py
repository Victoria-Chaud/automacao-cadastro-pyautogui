import pyautogui

import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

# Passo 1: Entrar no site da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: fazer login e colocar a senha
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir para todos os produtos

# Passo 1: Entrar no site da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Usar uma biblioteca, aqui será usado o pyautogui (fazer automações, teclado e mouse.) -> no terminal usar: pip install pyautogui
# informar para o python que o pyautogui será usado, colocar no começo do código -> import pyautogui
# abrir o chrome / digitar o site
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")

# Aqui precisei solicitar que o py clicasse no usuário do meu chrome, pois utilizo dois
# Por isso acrescentei mais essa linha de código.
# fiz uma aba auxiliar para saber o posicionamento do meu mouse.
# Pedi para aguardar alguns segundo para posicionar o mouse e no usuário desejado -> segue como ficou no auxiliar:
# import pyautogui
# import time
# time.sleep(5)
#print(pyautogui.position())
time.sleep(2)
pyautogui.click(x=928, y=592)


# Coloquei mais uma espera para o chrome carregar
time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2 logar no sistema
# mesmo processo do mouse
time.sleep(3)
pyautogui.click(x=632, y=512)
pyautogui.write("vic_dev@dev.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")

time.sleep(3)

# Passo 3 importar a base de dados. Será usado o pandas, no terminal: pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 cadastrar um produto
for linha in tabela.index: # para cadalinha da tabela / index nº da linha

    pyautogui.click(x=748, y=357)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) #str -> transformar em string para que ele vire texto
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
    

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
