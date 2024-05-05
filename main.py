import ttkbootstrap as ttkb
import os
from pytube import YouTube as yt

# Posiciona automaticamente a janela no centro
def autoPosicionar(larguraDesktop, alturaDesktop):
  larguraJanela = 700
  alturaJanela = 500
  desktopX = (larguraDesktop / 2) - (larguraJanela / 2)
  desktopY = (alturaDesktop / 2) - (alturaJanela / 2)
  return larguraJanela, alturaJanela, desktopX, desktopY

def main():
  # Configuração da janalea principal
  mainWindow = ttkb.Window(themename="superhero")
  larguraDesktop = mainWindow.winfo_screenwidth()
  alturaDesktop = mainWindow.winfo_screenheight()
  larguraJanela, alturaJanela, desktopX, desktopY = autoPosicionar(larguraDesktop, alturaDesktop)
  mainWindow.geometry(f"{larguraJanela}x{alturaJanela}+{int(desktopX)}+{int(desktopY)}")
  
  
  
  mainWindow.mainloop()

if __name__ == '__main__':
  try:
    main()
  except Exception as erro:
    print(f"Erro: {erro}")