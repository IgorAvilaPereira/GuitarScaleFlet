import flet as ft
from datetime import datetime
import sqlite3
# THIS FOR IMPORT COLOR TABLE BACKGROUN
# from reportlab.lib import colors
# # THIS FOR mm OF YOU PAGES
# from reportlab.lib.units import mm
# # FOR SIZE OF YOU PAGES
# from reportlab.lib.pagesizes import letter,landscape,portrait
# # THIS FOR RESULT OF YOU TABLE AND ADD TITLE ABOVE THE TABLE
# from reportlab.platypus import SimpleDocTemplate,Table,Paragraph
# from PIL import Image
# import pyscreenshot as ImageGrab
NRO_BOTOES = 42
violao = []
i = 1
while (i <= NRO_BOTOES):
    violao.append(["--", ft.colors.BLUE, None])
    i = i + 1

def main(page: ft.Page):   
    page.title = "GuitarScaleFlet - Desenvolvido por Igor Avila Pereira"
    page.auto_scroll = True   
    # page.window_width = 1000      
    # page.window_height = 600      
    # page.window_resizable = False     
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    def open_dlg_salvar(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Novo Shape Criado")
        dlg.open = True
        page.update()
    def open_dlg_editar(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Shape Editado")
        dlg.open = True
        page.update()
    def open_dlg_editar_erro(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Selecione algum shape para ser editado")
        dlg.open = True
        page.update()
    def open_dlg_restaurar_erro(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Selecione algum shape para ser duplicado")
        dlg.open = True
        page.update()    
    def open_dlg_duplicar_erro(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Selecione algum shape para ser duplicado")
        dlg.open = True
        page.update()
    def open_dlg_deletar_erro(e):
        page.dialog = dlg
        dlg.title = ft.Text("Selecione algum shape para ser deletado")
        dlg.open = True
        page.update()    
    def open_dlg_duplicar_acerto(e):       
        page.dialog = dlg
        dlg.title = ft.Text("Duplicação realizada com sucesso!")
        dlg.open = True
        page.update()
    def button_clicked(e):   
        global violao            
        if (e.control.text == "--" and e.control.bgcolor is None):
            e.control.text = "1"        
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.BLACK            
        elif (e.control.text == "1" and e.control.bgcolor is ft.colors.BLACK):
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.RED
        elif (e.control.text == "1" and e.control.bgcolor is ft.colors.RED):
            e.control.text = "2"        
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.BLACK            
        elif (e.control.text == "2" and e.control.bgcolor is ft.colors.BLACK):
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.RED
        elif (e.control.text == "2" and e.control.bgcolor is ft.colors.RED):
            e.control.text = "3"        
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.BLACK            
        elif (e.control.text == "3" and e.control.bgcolor is ft.colors.BLACK):
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.RED
        elif (e.control.text == "3" and e.control.bgcolor is ft.colors.RED):
            e.control.text = "4"        
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.BLACK            
        elif (e.control.text == "4" and e.control.bgcolor is ft.colors.BLACK):
            e.control.color=ft.colors.WHITE
            e.control.bgcolor=ft.colors.RED
        elif (e.control.text == "4" and e.control.bgcolor is ft.colors.RED):
            e.control.text = "--"        
            e.control.color=ft.colors.BLUE
            e.control.bgcolor=None
        violao[int(e.control.data)-2] = [e.control.text, e.control.bgcolor, e.control.color]            
        e.control.update()
    def reiniciar():
        global violao
        violao = []
        i = 1
        while (i <= NRO_BOTOES):
            violao.append(["--", ft.colors.BLUE, None])
            i = i + 1
    def salvar(e):
        global violao             
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")          
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        sql = "INSERT INTO shapes (nome) values (?) RETURNING id;"
        if (len(txt_name.value) > 0):
            cur.execute(sql, [txt_name.value])      
        else:
            cur.execute(sql, [dt_string])      
        id = cur.fetchone()[0]
        conn.commit()          
        i = 2
        for botao in violao:
            if (botao[0] == "1" or botao[0] == "2" or botao[0] == "3" or botao[0] == "4"):                                
                sql = "INSERT INTO notas (botao, dedo, dominante, shape_id) values (?, ?, ?, ?);";                
                cur.execute(sql, [str(i), botao[0], True if botao[1] == ft.colors.RED else False, id])         
                conn.commit()                     
            i = i + 1
        cur.close()
        conn.close()
        limpar(e)
        lista_shapes()
        open_dlg_salvar(e)  
    
    radioGroup = ft.RadioGroup()
    def lista_shapes():
        lv.controls = []
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * from shapes order by id;")        
        vetShape = []
        for shape in cur.fetchall():
            vetShape.append(ft.Radio(value=str(shape[0]), label=shape[1]))
        if (len(vetShape) > 0):
            radioGroup.content = ft.Column(vetShape)
            lv.controls.append(radioGroup)
        cur.close()
        conn.close()
        page.update()    
    
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    dlg = ft.AlertDialog(
        title=ft.Text("Shape salvo!")
    )   
    dataTable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text(""))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="2")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="3")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="4")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="5")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="6")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="7")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="8"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="9")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="10")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="11")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="12")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="13")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="14")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="15"))
                ],
            ),
            ft.DataRow(
                cells=[
                ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="16")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="17")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="18")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="19")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="20")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="21")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="22"))
                                    ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="23")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="24")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="25")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="26")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="27")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="28")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="29"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="30")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="31")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="32")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="33")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="34")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="35")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="36"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="37")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="38")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="39")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="40")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="41")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="42")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="43"))
                ],
            )                
        ]
    )    
    def limpar(e):
        txt_name.value = None
        radioGroup.value = None
        dataTable.columns=[
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text("")),
            ft.DataColumn(ft.Text(""))
        ]
        dataTable.rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="2")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="3")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="4")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="5")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="6")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="7")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="8"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="9")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="10")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="11")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="12")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="13")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="14")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="15"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="16")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="17")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="18")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="19")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="20")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="21")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="22"))
                                    ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="23")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="24")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="25")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="26")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="27")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="28")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="29"))
                ],
            ),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="30")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="31")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="32")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="33")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="34")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="35")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="36"))
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="37")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="38")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="39")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="40")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="41")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="42")),
                    ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="43"))
                ],
            )                
        ]
        reiniciar()
        page.update()
    def editar(e):
        global violao     
        try:
            id = int(radioGroup.value)
            conn = sqlite3.connect("database.db")
            if (len(txt_name.value) > 0):
                cur = conn.cursor()
                sql = "UPDATE shapes SET nome = ? where id = ?"
                cur.execute(sql, [txt_name.value, id]) 
                conn.commit()      
            cur = conn.cursor()
            sql = "DELETE FROM notas where shape_id = ?"
            cur.execute(sql, [id]) 
            conn.commit()           
            i = 0  
            while (i < NRO_BOTOES):
                botao = violao[i]
                if (botao[0] == "1" or botao[0] == "2" or botao[0] == "3" or botao[0] == "4"):                                
                    sql = "INSERT INTO notas (botao, dedo, dominante, shape_id) values (?, ?, ?, ?);";                
                    cur.execute(sql, [str(i+2), botao[0], True if botao[1] == ft.colors.RED else False, id])         
                    conn.commit()                     
                i = i + 1
            cur.close()
            conn.close()
            open_dlg_editar(e)  
            lista_shapes()
        except:
            open_dlg_editar_erro(e)  
    def deletar(e):    
        try:    
            id = int(radioGroup.value)
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            sql = "DELETE FROM notas where shape_id = ?"
            cur.execute(sql, [id]) 
            conn.commit()   
            sql = "DELETE FROM shapes where id = ?"
            cur.execute(sql, [id]) 
            conn.commit()   
            limpar(e)
            reiniciar()
            lista_shapes()
            page.update()
        except:
            open_dlg_deletar_erro(e)   
    def restaurar(e):
        global violao     
        try:
            id = int(radioGroup.value)
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            sql = "SELECT * FROM shapes where id = ?";
            cur.execute(sql, [id]) 
            shape = cur.fetchone()
            txt_name.value = shape[1]            
            dataTable.columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text(""))
            ]        
            sql = "SELECT * FROM notas where shape_id = ? order by id";
            cur.execute(sql, [id]) 
            vetNota = cur.fetchall()
            auxNota = 0
            if (len(vetNota) > 0):
                reiniciar()
                dataTable.rows = []        
                i = 2
                aux = 1
                cells=[]        
                while i <= NRO_BOTOES+1:            
                    if (aux >= 1 and aux <= NRO_BOTOES/6):                                              
                        if (auxNota < len(vetNota) and str(i) == vetNota[auxNota][1]):                            
                            if (vetNota[auxNota][2]):
                                cells.append(ft.DataCell(ft.ElevatedButton(text=vetNota[auxNota][4], style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data=str(i), bgcolor=ft.colors.RED, color=ft.colors.WHITE)))
                                violao[i-2]=[str(vetNota[auxNota][4]), ft.colors.RED, ft.colors.WHITE]
                            else:
                                cells.append(ft.DataCell(ft.ElevatedButton(text=vetNota[auxNota][4], style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data=str(i), bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)))
                                violao[i-2] = [str(vetNota[auxNota][4]), ft.colors.BLACK, ft.colors.WHITE]
                            auxNota = auxNota + 1
                        else:
                            cells.append(ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data=str(i))))
                            violao[i-2] = ["--", ft.colors.BLUE, None]                                                
                        if (aux == NRO_BOTOES/6):
                            row = ft.DataRow(cells = cells)
                            dataTable.rows.append(row)
                            cells=[]    
                            aux = 1
                        else:
                            aux = aux + 1

                    i = i + 1             
            cur.close()
            conn.close()
            page.update()
        except:
            open_dlg_restaurar_erro(e)  
    def duplicar(e):
        global violao     
        try:
            id = int(radioGroup.value)
            restaurar(e)    
            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")   
            txt_name.value = txt_name.value+"_"+dt_string
            salvar(e)     
            open_dlg_duplicar_acerto(e)              
        except:
            open_dlg_duplicar_erro(e)

    txt_name = ft.TextField(label="Nome do shape:")
    # def pick_files_result(e: ft.FilePickerResultEvent):        
    #     print("Selected files:", e.files)
    #     print("Selected file or directory:", e.path)
    #     x1 = page.window_top        
    #     y1 = page.window_left        
    #     print(str(x1)+","+str(y1))
    #     print(str(x1+page.width)+","+str(y1+page.height))                                   
    #     x2 = x1+page.width
    #     y2 = y1+page.height
    #     ImageGrab.grab().save(e.path+".png")    
        # screen = ImageGrab.grab()      
        # screen.save(e.path+".png")            
        # sleep(2)
        # import cv2
        # image = cv2.imread(e.path+".png")
        # crop_image = image[y1:y1+page.height, x1:x1+page.width]
        # cv2.imshow("Cropped", crop_image)
        # cv2.waitKey(0)    
        # from PIL import Image
        # img = Image.open(e.path+".png")
        # img2 = img.crop((x1,y1, x1+page.width,y1+page.height))      
        # img2.save('myimage_cropped.jpg')                     
        # img2.show()
        # mydata = [
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},
        #     {"name":"john","last":"smith","age":12},    
        # ]
        # doc = SimpleDocTemplate(e.path+"youfile222.pdf",pagesize=landscape(letter))
        # data = [[value for value in item.values()] for item in mydata]
        # # data.insert(0, ["name", "last", "age"])
        # table = Table(data, colWidths=[10*mm, 20*mm, 10*mm])
        # header_text = "My PDF Data"
        # header = Paragraph(header_text) 
        # # OPTIONAL IF YOU WANT STYLING THE TABLE LIKE ADD COLOR,
        # # BACKGROUND COLOR , FONT SIZE , FONT NAME ,  
        # # table.setStyle([
        # #     ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        # #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        # #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        # #     ('BACKGROUND', (0, -1), (-1, -1), colors.beige),
        # #     ('GRID', (0, 0), (-1, -1), 1, colors.black) 
        # # ])	 
        # doc.build([header,table])    
    
    # export
    # pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    # page.overlay.append(pick_files_dialog)
    # page.update()    
    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Salvar", on_click=salvar),
                    alignment=ft.alignment.center
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Limpar", on_click=limpar),
                    alignment=ft.alignment.center
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Restaurar", on_click=restaurar),
                    alignment=ft.alignment.center
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Deletar", on_click=deletar),
                    alignment=ft.alignment.center
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Editar", on_click=editar),
                    alignment=ft.alignment.center
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Duplicar", on_click=duplicar),
                    alignment=ft.alignment.center
                )
            )
            # items.append(
            #     ft.Container(                    
            #         content=ft.ElevatedButton("Export",   on_click=lambda _: pick_files_dialog.save_file()),
            #         alignment=ft.alignment.center
            #     )
            # )
            items.append(
                ft.Container(
                    content=txt_name,
                    alignment=ft.alignment.center
                )
            )            
        return items
    
    row = ft.Row(spacing=0, controls=items(1))
    page.add(ft.Column(), row)
    page.add(
        ft.Row(
            [
                ft.Container(
                    content=dataTable,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=lv,
                    alignment=ft.alignment.center,
                    width=300,
                    height=300
                )
            ]))  
    lista_shapes()
# criar um executavel => flet pack main.py (eh preciso colocar o database.db junto do executavel (dentro da pasta dist))
ft.app(target=main, assets_dir="assets")