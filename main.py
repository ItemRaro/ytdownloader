import ttkbootstrap as ttkb
import configuracao
import os
from pytube import YouTube as yt
from tkinter import filedialog

logger = configuracao.logging.getLogger("default")

class janelaPrincipal():

  # Posiciona automaticamente a janela no centro
  def configuracaoJanela(self) -> None:
    self.mainWindow = ttkb.Window(themename="superhero")
    larguraJanela = 600
    alturaJanela = 300
    larguraDesktop = self.mainWindow.winfo_screenwidth()
    alturaDesktop = self.mainWindow.winfo_screenheight()
    desktopX = (larguraDesktop / 2) - (larguraJanela / 2)
    desktopY = (alturaDesktop / 2) - (alturaJanela / 2)
    self.mainWindow.geometry(f"{larguraJanela}x{alturaJanela}+{int(desktopX)}+{int(desktopY)}")
    self.mainWindow.title("ytDonwloader")
    
  def salvarCaminho(self) -> str:
    logger.info("Abriu a busca do caminho para salvar")
    caminho = filedialog.askdirectory(title= "Selecione onde salvar o video")
    logger.info(f"Caminho escolhido '{caminho}'")
    self.salvarCaixa.delete(first= 0, last= 500)
    self.salvarCaixa.insert(index= 0, string= caminho)
    return caminho
    
  def progressoDownload(self, stream, bloco, bytesRestantes) -> None:
    bytesTotais = stream.filesize
    bytesBaixados = (bytesTotais - bytesRestantes)
    porcentagemBaixada = ((bytesBaixados / bytesTotais) * 100)
    porcentagem = str(int(porcentagemBaixada))
    logger.info(f"Baixando {porcentagem}%")
    self.ytLinkTitulo.configure(text= f"{porcentagem}%")
    self.ytLinkTitulo.update()
  
  def ytConsulta(self) -> None:
    logger.info("Iniciou consulta")
    logger.info(f"Link para consulta '{self.ytLink.get()}'")
    try:
      ytObject = yt(self.ytLink.get())
      ytVideo = ytObject.streams.get_highest_resolution()
      self.ytLinkTitulo.configure(text= ytVideo.title)
      logger.info(f"Consulta finalizada")
    except Exception as erro:
      self.ytLinkTitulo.configure(text= erro)
      logger.error(f"Erro na consulta '{erro}'")
      
  def ytDownload(self) -> None:
    logger.info("Iniciou download")
    logger.info(f"Link para download '{self.ytLink.get()}'")
    try:
      ytObject = yt(self.ytLink.get(), on_progress_callback= self.progressoDownload)
      ytVideo = ytObject.streams.get_highest_resolution()
      ytVideo.download(output_path= self.salvarCaixa.get())
      self.ytLinkTitulo.configure(text= "Download concluído")
      logger.info(f"Finalizou download")
    except Exception as erro:
      self.ytLinkTitulo.configure(text= erro)
      logger.error(f"Erro no download '{erro}'")
      
  def __init__(self) -> None:
    logger.info("Iniciou o programa")
    self.configuracaoJanela()
    
    # Widgets
    self.titulo = ttkb.Label(
      self.mainWindow,
      text= "ytDownloader",
      font= (
        "ariel",
        20,
        "bold"
      ),
      bootstyle= "light",
      anchor= "center"
    )
    self.titulo.pack(
      fill= "x",
      padx= 10,
      pady= 10
    )
    self.ytLink = ttkb.Entry(
      self.mainWindow,
      bootstyle= "primary",
      font= (
        "helvetica",
        10,
        "italic"
      ),
      justify= "center"
    )
    self.ytLink.pack(
      fill= "x",
      padx= 10,
      pady= 10
    )
    self.ytLinkTitulo = ttkb.Label(
      self.mainWindow,
      text= "Coloque o link do video no campo acima",
      font=(
        "helvetica",
        12,
        "italic"
      ),
      bootstyle= "light",
      anchor= "center"
    )
    self.ytLinkTitulo.pack(
      fill= "x",
      padx= 10,
      pady= 10
    )
    self.salvarQuadro = ttkb.Frame(
      self.mainWindow
    )
    self.salvarQuadro.columnconfigure(
      index= 0,
      weight= 1
    )
    self.salvarQuadro.columnconfigure(
      index= 1,
      weight= 1
    )
    self.botaoSalvar = ttkb.Button(
      self.salvarQuadro,
      text= "Salvar em...",
      bootstyle= "primary",
      command= self.salvarCaminho
    )
    self.botaoSalvar.grid(
      row= 0,
      column= 0,
      padx= 1
    )
    self.salvarCaixa = ttkb.Entry(
      self.salvarQuadro,
      font= (
        "helvetica",
        12,
        "italic"
      ),
      bootstyle= "primary",
      width= 45
    )
    self.salvarCaixa.grid(
      row= 0,
      column= 1,
      padx= 1
    )
    self.salvarQuadro.pack(
      fill= "x",
      padx= 10,
      pady= 10
    )
    
    self.botaoQuadro = ttkb.Frame(
      self.mainWindow
    )
    self.botaoQuadro.columnconfigure(
      index= 0,
      weight= 1
    )
    self.botaoQuadro.columnconfigure(
      index= 1,
      weight= 1
    )
    self.botaoConsulta = ttkb.Button(
      self.botaoQuadro,
      text= "Consultar",
      bootstyle= "primary",
      command= self.ytConsulta
    )
    self.botaoConsulta.grid(
      row= 0,
      column= 0,
      padx= 1
    )
    self.botaoDownload = ttkb.Button(
      self.botaoQuadro,
      text= "Download",
      bootstyle= "success",
      command= self.ytDownload
    )
    self.botaoDownload.grid(
      row= 0,
      column= 1,
      padx= 1
    )
    self.botaoQuadro.pack(
      fill= "x",
      padx= 10,
      pady= 25,
      side= "bottom"
    )

    self.mainWindow.mainloop()
    logger.info("Fechou o programa")

if __name__ == '__main__':
  try:
    janelaPrincipal()
  except Exception as erro:
    print(f"Erro: {erro}")