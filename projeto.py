# Passo a passo do código

# 1. Entrar no sistema
# 2. Fazer login
# 3. Abrir a base de dados
# 4. Cadastrar um produto
# 5. Repetir o passo a 4 até acabar a lista de produtos

# ============================
# comandos uteis do pyautogui
# ============================
# pyautogui.click #para clicar em alguma coisa
# pyautogui.write #para escrever algo
# pyautogui.press #para apertar alguma tecla
# pyautogui.hotkey #para apertar uma combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 1 #pausa de 1 segundo entre cada comando
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' #link do sistema (inserir para não precisar repetir o link sempre)

# 1. Entrar no sistema
pyautogui.press('win') #abre o menu iniciar
pyautogui.write('edge') #seleciona o navegador nomeado
pyautogui.press('enter') #abre o navegador

pyautogui.write(link) #digita o endereço do sistema
pyautogui.press('enter') #abre o sistema

# fazer uma pausa para o site carregar
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=610, y=409) #clica no campo de email (para descobrir a posição do clique, rode o código do arquivo auxiliar.py e posicione o mouse sobre o campo desejado)
pyautogui.write('pythonimpressionador@gmail.com')
#pyautogui.click(x=559, y=501)
pyautogui.press('tab') #outra forma de selecionar o campo de senha, usando a tecla tab
pyautogui.write('123456') #digita a senha
pyautogui.press('tab') #seleciona o botão para logar
pyautogui.press('enter') #clica no botão para logar

# Fazer uma pausa para o site carregar
time.sleep(3)

# 3. Abrir a base de dados (importar o arquivo para dentro do código)
import pandas as pd

# CURIOSIDADE: pd.read_excel(sheet_name="nome da coluna"): função para ler uma aba dentro de uma planilha excel.

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: # para cada linha da tabela, faça:

# 4. Cadastrar produto
    pyautogui.click(x=642, y=284)
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #o código do produto tem que ser string, por isso a função str()
    pyautogui.write('codigo') #escreve o código do produto
    pyautogui.press('tab')

    # Produto/Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.write ('marca')
    pyautogui.press('tab')

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write('tipo')
    pyautogui.press('tab')

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write('categoria')
    pyautogui.press('tab')

    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write('preço')
    pyautogui.press('tab')

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write('custo')
    pyautogui.press('tab')

    # OBS
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press('tab') #passar para o botão Enviar

    pyautogui.press('enter')

    # Voltar para o início da página para cadastrar o próximo produto
    pyautogui.scroll(1000) #rolar a página para cima

# 5. Repetir o passo a 4 até acabar a lista de produtos





