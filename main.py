import ttkbootstrap as ttkb
import os
from pytube import YouTube as yt

class janelaPrincipal():

  # Posiciona automaticamente a janela no centro
  def autoPosicionar(self, larguraDesktop, alturaDesktop) -> None:
    larguraJanela = 600
    alturaJanela = 300
    desktopX = (larguraDesktop / 2) - (larguraJanela / 2)
    desktopY = (alturaDesktop / 2) - (alturaJanela / 2)
    return larguraJanela, alturaJanela, desktopX, desktopY

  def ytConsulta(self) -> None:
    try:
      ytObject = yt(self.ytLink.get())
      ytVideo = ytObject.streams.get_highest_resolution()
      self.ytLinkTitulo.configure(text= ytVideo.title)
    except Exception as erro:
      self.ytLinkTitulo.configure(text= erro)
      print(f"Erro: {erro}")
      
  def __init__(self) -> None:
    # Configuração da janalea principal
    self.mainWindow = ttkb.Window(themename="superhero")
    self.larguraDesktop = self.mainWindow.winfo_screenwidth()
    self.alturaDesktop = self.mainWindow.winfo_screenheight()
    self.larguraJanela, self.alturaJanela, self.desktopX, self.desktopY = self.autoPosicionar(self.larguraDesktop, self.alturaDesktop)
    self.mainWindow.geometry(f"{self.larguraJanela}x{self.alturaJanela}+{int(self.desktopX)}+{int(self.desktopY)}")
    self.mainWindow.title("ytDonwloader")
    
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
      pady= 15
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
      padx= 50,
      pady= 15
    )
    self.ytLinkTitulo = ttkb.Label(
      self.mainWindow,
      text= "",
      font=(
        "helvetica",
        12,
        "bold"
      ),
      bootstyle= "light",
      anchor= "center"
    )
    self.ytLinkTitulo.pack(
      fill= "x",
      padx= 10,
      pady= 15
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
      bootstyle= "success"
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

if __name__ == '__main__':
  try:
    janelaPrincipal()
  except Exception as erro:
    print(f"Erro: {erro}")