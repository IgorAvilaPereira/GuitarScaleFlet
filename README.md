# GuitarScaleFlet

## Instalação

1) Extraia o zip baixado através do link https://github.com/IgorAvilaPereira/GuitarScaleFlet/archive/refs/heads/main.zip
2) Cole database.db na pasta **/dist**. 
3) O executável está na pasta **/dist**. 
4) Execute o arquivo executável clicando 2x. 

## Para cria um executável:
```
pip install -r requirements
pip install pyinstaller
flet pack main.py
```
O executável será gerado dentro da pasta **/dist**.

Antes de executá-lo, cole **database.db** na pasta **/dist**. 

Se for windows: dist\main.exe

Se for Linux: dist/main
