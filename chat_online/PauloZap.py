# objetivo do projeto
# criar um interface web de chat ao vivo
# passo a passo do projeto
# criar pagina inicial
  # criar titulo na pagina inicial
  # criar botao na pagina inicial para iniciar o chat
    # botao inicar chat abrirar um pop up
      # criar pop up      
        # criar titulo no pop up
        # criar campo de texto para colocar nome da pessoa
        # criar botao para entrar no chat
# criar pagina do chat
# criar coluna de mensagens do chat
# criar campo de texto para colocar as mensagens do chat
# criar botão de enviar mensagem no chat

# necessario instalação da bibliote
# pip install flet

# import de biblotecas
import flet as ft

# criação da main principal
def main(pagina):
  # tunel de comunicação
  def enviar_mensagem_tunel(mensagem):
    texto_chat = ft.Text(mensagem)
    chat.controls.append(texto_chat)
    pagina.update()
  
  # aplicação do tunel de comunicação na pagina
  pagina.pubsub.subscribe(enviar_mensagem_tunel)

  # titulo da pagina inicial
  titulo = ft.Text("PauloZap")

  # titulo do pop up
  titulo_janela = ft.Text("Bem vindos ao PauloZap")

  # apresentação do chat em colunas
  chat = ft.Column()
  
  # função envio de mensagem no chat
  def enviar_mensagem(evento):
    texto_mensagem = campo_mensagem.value # pegar texto do campo mensagem
    nome_usuario = campo_nome_usuario.value # pegar testo do campo nome usuario
    mensagem = f"{nome_usuario}: {texto_mensagem}" # montar mensagem
    pagina.pubsub.send_all(mensagem) # publicar mensagem no tunel de comunicação
    campo_mensagem.value = "" # limpar campo mensagem da pagina
    pagina.update() # atualizar pagina

  # enviar mensagens no chat
  campo_mensagem = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_mensagem)
  botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

  # concatenar campo de mensagem e envio de mensagem na linha
  linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

  # função entrar no chat
  def entrar_chat(evento):
    pagina.remove(titulo) # remover titulo da pagina
    pagina.remove(botao_iniciar) # remover botao_iniciar 
    janela.open = False # fechar pop up

    pagina.add(chat) # adicionar coluna chat na pagina
    pagina.add(linha_mensagem) # adicionar campo mensagem e botao enviar mensagem
    mensagem = f"{campo_nome_usuario.value} entrou no chat" # formataçao de mensagem de acesso ao chat
    pagina.pubsub.send_all(mensagem) # publicar mensagem pelo tunel de comunicação da pagina
    pagina.update() # atualizar pagina

  # acessar pagina do chat
  campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
  botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

  # pop up para acesso ao chat
  janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

  # função para abrir pop up de acesso ao chat
  def iniciar_chat(evento):
    pagina.dialog = janela # criar pop up na pagina
    janela.open = True # abrir pop up na pagina
    pagina.update() # atualizar pagina
  
  # acessar pop up na pagina
  botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

  pagina.add(titulo) # adicionar titulo na pagina
  pagina.add(botao_iniciar) # adicionar botão na pagina

# inicar função main no navegador
ft.app(main, view=ft.WEB_BROWSER)