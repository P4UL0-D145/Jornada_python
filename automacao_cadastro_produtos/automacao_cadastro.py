# objetivo do projeto
# automatizar uma tarefa de cadastramento de produtos em um portal web
# criar um robo que leia a base de dados e cadastre os produtos no portal web
# passo a passo do projeto
# abri janela windowns
# entrar no navegador (Chrome)
# abrir site do portal web
# logar no portal web
# ler base de dados dos produtos
# cadastrar cada produto da base de dados no portal web

# necessario instalação das bibliotecas
# pip install pyautogui
# pip install pandas

# import de bibliotecas
import pyautogui as pg
import pandas as pd
import time

# definir tempo de espera entre os comandos pyautogui
pg.PAUSE = 1.5

# abrir Chrome
pg.press("win") # clicar no botão windowns
pg.write("Chrome") # escrever nome do app
pg.press("enter") # clicar no botão enter
pg.click(x=805, y=602) # clicar no usuario do Chrome para quem tem mais de um usuario
pg.click(x=394, y=93) # clicar na barra de pesquisa do site
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # escrever link na barra de pesquisa
pg.press("enter") # clicar no botão enter

# esperar site carregar 
time.sleep(5)

# fazendo login no site
pg.click(x=732, y=558) # clicar no campo de login do site
pg.write("seu_usuario") # inserir email no campo de login
pg.press("tab") # clicar em tab para ir para o campo de senha
pg.write("sua_senha") # inserir senha no campo de senha
pg.press("tab") # clicar em tab para ir para o campo logar
pg.press("enter") # clicar em enter para acessa o site

# importar base de dados de produtos
df = pd.read_csv('produtos.csv')

# loop para percorrer todos os produtos
for linha in df.index:
  pg.click(x=730, y=389) # clica no primeiro campo de cadastro
  pg.write(str(df.loc[linha, "codigo"])) # registrar codigo do produto
  pg.press("tab") # seguir para proxima celula de cadastro
  pg.write(str(df.loc[linha, "marca"])) # registrar nome da marca
  pg.press("tab") # seguir para proxima celula de cadastro
  pg.write(str(df.loc[linha, "tipo"])) # registrar nome do tipo
  pg.press("tab") # seguir para proxima celula de cadastro
  pg.write(str(df.loc[linha, "categoria"])) # registrar nome da categoria
  pg.press("tab") # seguir para proxima celula de cadastro
  pg.write(str(df.loc[linha, "preco_unitario"])) # registrar valor do preco_unitario
  pg.press("tab") # seguir para proxima celula de cadastro
  pg.write(str(df.loc[linha, "custo"])) # registrar valor de custo
  pg.press("tab") # seguir para proxima celula de cadastro
  if not pd.isna(df.loc[linha, "obs"]): # verifica se obs esta nula nessa linha
    pg.write(str(df.loc[linha, "obs"])) # registrar descricao da obs
  pg.click(x=827, y=816) # clicar no botão de cadastramento do produto
  pg.scroll(5000) # dar scroll na tela para o inicio do site