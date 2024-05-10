# necessario instalação das bibliotecas
# pip install pyautogui
# script necessario para obter dados da posicao do mouse
# importação de bibliotecas
import pyautogui
import time

# espera de 5 segundos
time.sleep(5)
# informa a posição onde esta o mouse
print(pyautogui.position())
# testa o scroll da tela
pyautogui.scroll(-200)