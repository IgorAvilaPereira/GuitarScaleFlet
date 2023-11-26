import flet as ft
from datetime import datetime
import sqlite3

NRO_BOTOES = 42
violao = []
i = 1
while (i <= NRO_BOTOES):
    violao.append(["--", ft.colors.BLUE, None])
    i = i + 1

def main(page: ft.Page):   
    page.title = "GuitarScaleFlet"
    page.auto_scroll = True   
    
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
        # sabendo o botao que foi clicado
        # print(e.control.data)
    
        # print(violao)
        # violao[int(e.control.data)-2] = [e.control.text, e.control.color, e.control.bgcolor]    
        
        # dedo, fundo, letra
        violao[int(e.control.data)-2] = [e.control.text, e.control.bgcolor, e.control.color]    
        # print(violao[int(e.control.data)-2])            
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
                # print(True if botao[1] == ft.colors.RED else False)
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
    # lv.auto_scroll = True    

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
            # radio selecione
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
                            # eh tonica
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
            # print(violao)
            salvar(e)     
            # conn = sqlite3.connect("database.db")
            # cur = conn.cursor()
            # sql = "DELETE FROM notas where shape_id = ?"
            # cur.execute(sql, [id]) 
            # conn.commit()           
            # i = 0  
            # while (i < NRO_BOTOES):
            #     botao = violao[i]
            #     if (botao[0] == "1" or botao[0] == "2" or botao[0] == "3" or botao[0] == "4"):                                
            #         sql = "INSERT INTO notas (botao, dedo, dominante, shape_id) values (?, ?, ?, ?);";                
            #         cur.execute(sql, [str(i+2), botao[0], True if botao[2] == ft.colors.RED else False, id])         
            #         conn.commit()                     
            #     i = i + 1
            # cur.close()
            # conn.close()
            open_dlg_duplicar_acerto(e)  
            # open_dlg_editar(e)  
        except:
            open_dlg_duplicar_erro(e)  

    # row = ft.Row(spacing=0, con)
    # page.add(

    # items = []
    # for i in range(1, 1 + 1):
    #     items.append(
    #         ft.Container(
    #             content=dataTable,
    #             alignment=ft.alignment.top_left,
    #             # width=50,
    #             # height=50,
    #             # bgcolor=ft.colors.AMBER,
    #             # border_radius=ft.border_radius.all(5),
    #         )
    #     )
    #     items.append(
    #         ft.Container(
    #             content=lv,
    #             alignment=ft.alignment.center,
    #             # width=50,
    #             # height=50,
    #             # bgcolor=ft.colors.AMBER,  
    #             # border_radius=ft.border_radius.all(5),
    #         )
    #     )
    
    
    # page.add(dataTable)  
    # page.add(lv)  
    # 
      

    txt_name = ft.TextField(label="Nome do shape:")


    def items(count):
        items = []
        for i in range(1, count + 1):
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Salvar", on_click=salvar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Limpar", on_click=limpar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Restaurar", on_click=restaurar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )
            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Deletar", on_click=deletar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )

            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Editar", on_click=editar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )

            items.append(
                ft.Container(
                    content=ft.ElevatedButton(text="Duplicar", on_click=duplicar),
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
                )
            )


            items.append(
                ft.Container(
                    content=txt_name,
                    alignment=ft.alignment.center,
                    # width=50,
                    # height=50,
                    # bgcolor=ft.colors.AMBER,
                    # border_radius=ft.border_radius.all(5),
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
                    alignment=ft.alignment.center,
                    # bgcolor=ft.colors.AMBER,
                    # width=150,
                    # height=150,
                    # border_radius=10,
                ),
                ft.Container(
                    content=lv,
                    # margin=10,
                    # padding=10,
                    alignment=ft.alignment.center,
                    # bgcolor=ft.colors.GREEN_200,
                    width=300,
                    height=300,
                    # border_radius=10,
                    # on_click=lambda e: print("Clickable without Ink clicked!"),
                )
            ]))
        
    # row = ft.Row(spacing=0, controls=items)
    # page.add(ft.Column(), row)    


    lista_shapes()    

  

    # page.add(ft.ElevatedButton(text="Salvar", on_click=salvar))
    # page.add(ft.ElevatedButton(text="Limpar", on_click=limpar))    
    # page.add(ft.ElevatedButton(text="Restaurar", on_click=restaurar))
    # page.add(ft.ElevatedButton(text="Deletar", on_click=deletar))
    # page.add(ft.ElevatedButton(text="Editar", on_click=editar))
    # page.add(ft.ElevatedButton(text="Duplicar", on_click=duplicar))  
    # recuperar chave salva
    # print(page.client_storage.get("*"))

# https://flet.dev/docs/guides/python/packaging-desktop-app/#customizing-windows-executable-metadata
# Linux
# flet pack main.py --add-data "assets:assets"
# Windows
# flet pack main.py --add-data "assets;assets"

# https://flet.dev/docs/guides/python/testing-on-android/
# https://flet.dev/docs/cli/run/

# para rodar como app
#  pip install flet --upgrade
# flet run main.py --android

# para rodar como desktop
# python main.py

# destop
ft.app(target=main, assets_dir="assets")

# web
# autoreload
# flet run main.py --web
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

# @app.route("/tela_adicionar_tags/<int:id>", methods=['GET'])
# def tela_adicionar_tags(id):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM questoes where questoes.id = ?", [id])
#     questao = cur.fetchone()

#     cur.execute("SELECT * FROM tags")    
#     vetTag = cur.fetchall()

#     cur.execute("SELECT tag_id FROM questoes inner join questoes_tags on (questoes.id = questao_id) where questoes.id = ?", [id])
#     vetQuestaoTag = []
#     for i in cur.fetchall():
#         vetQuestaoTag.append(i[0])
#     cur.close()
#     conn.close()
#     return render_template('tela_adicionar_tags.html', vetTag=vetTag, questao=questao, vetQuestaoTag=vetQuestaoTag)    
    

# @app.route("/tela_alterar_questao/<int:id>", methods=['GET'])
# def tela_alterar_questao(id):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM questoes where id = ?", [id])
#     # conn.commit()   
#     questao = cur.fetchone()
#     cur.close()
#     conn.close()
#     # return redirect(url_for('index'))
#     return render_template('tela_alterar_questao.html', questao=questao)

# @app.route("/tela_alterar_tag/<int:id>", methods=['GET'])
# def tela_alterar_tag(id):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tags where id = ?", [id])
#     # conn.commit()   
#     tag = cur.fetchone()
#     cur.close()
#     conn.close()
#     # return redirect(url_for('index'))
#     return render_template('tela_alterar_tag.html', tag=tag)

# @app.route("/remover_tag/<int:id>", methods=['GET'])
# def remover_tag(id):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM tags where id = ?", [id])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/adicionar_tags", methods=['POST'])
# def adicionar_tags():
#     id = int(request.form.get("id"))
    
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()

#     cur.execute("DELETE FROM questoes_tags WHERE questao_id = ?;", [id])
#     conn.commit()   

#     for tag_id in request.form.getlist('tags'):    
#         cur.execute("INSERT INTO questoes_tags (questao_id, tag_id) VALUES(?,?);", [id, tag_id])    
#         conn.commit()   

#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/alterar_tag", methods=['POST'])
# def alterar_tag():
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     tag = request.form.get("tag")   
#     id = int(request.form.get("id"))
#     cur.execute("UPDATE tags SET tag = ? where id = ?", [tag, id])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/alterar_questao", methods=['POST'])
# def alterar_questao():
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     questao = request.form.get("questao")   
#     id = int(request.form.get("id"))
#     cur.execute("UPDATE questoes SET questao = ? where id = ?", [questao, id])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/remover_questao/<int:id>", methods=['GET'])
# def remover_questao(id):
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("DELETE FROM questoes where id = ?", [id])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('listar_questao'))

# @app.route("/adicionar_tag", methods=['POST'])
# def adicionar_tag():
#     tag = request.form.get("tag")        
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO tags (tag) VALUES (?)", [tag])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/adicionar_questao", methods=['POST'])
# def adicionar_questao():
#     questao = request.form.get("questao")        
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO questoes (questao) VALUES (?)", [questao])
#     conn.commit()   
#     cur.close()
#     conn.close()
#     return redirect(url_for('index'))

# @app.route("/gerar", methods=['POST'])
# def gerar():
#     nro_questao = 1
#     nro_questao = int(request.form.get("nro_questao"))   
    
#     vetTag = list(map(int, request.form.getlist('tags')))       
    
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
    
#     if (vetTag is not None):
#         if (len(vetTag) > 0):
#             tags = "("
#             for t in vetTag:
#                 tags = tags + str(t) + ","
#             tags = tags + ")"
#             tags = tags.replace(",)", ")")         

#             cur.execute("SELECT * FROM questoes inner join questoes_tags where tag_id in "+tags+" ORDER BY random() limit "+str(nro_questao))
#         else:
#             # print("aqui2")
#             cur.execute("SELECT * FROM questoes ORDER BY random() limit "+str(nro_questao))
#     else:
#         # print("aqui")
#         cur.execute("SELECT * FROM questoes ORDER BY random() limit "+str(nro_questao))
    
#     vetQuestao = cur.fetchall()
    
#     cur.close()
#     conn.close()
#     return render_template('prova.html', vetQuestao=vetQuestao)

# @app.route("/listar_questao/", defaults={ 'page': 1 })
# @app.route("/listar_questao/<int:page>")
# def listar_questao(page):
#     records = 10
#     start_from = (page-1)*records
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()        
#     cur.execute("select count(*) as total from questoes")    
#     total_records = cur.fetchone()[0]
#     total_pages = math.ceil(total_records/records)    
#     cur.execute("select * FROM questoes order by id desc limit "+str(records)+" offset "+str(start_from))
#     vet = cur.fetchall()
#     cur.close()
#     conn.close()
#     html_paginacao = ""
#     i = 1
#     while (i <= total_pages):        
#         html_paginacao = html_paginacao + "<a href='"+str(i)+"'>"+str(i)+"</a>&nbsp;&nbsp;"; 
#         i = i + 1     
#     return render_template('listar_questao.html', vet=vet, html_paginacao=html_paginacao)

# @app.route("/")
# def index():
#     conn = sqlite3.connect("database.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM tags")
#     vetTag = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('index.html', vetTag=vetTag)

# @app.route("/importar")
# def importar():
#     # conSqlite3 = sqlite3.connect("database.db")
#     # curSqlite3 = conSqlite3.cursor()
#     # curSqlite3.execute("INSERT INTO questoes (questao) VALUES(?)", [questao[1]])
#     # conSqlite3.commit()     
    
#     conn = psycopg2.connect("host=localhost dbname=docente user=postgres password=postgres port=5432")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM avaliacoes where descricao is not null;")
#     vetQuestao = cur.fetchall()
#     for questao in vetQuestao:   
#         # print(questao)            
#         conSqlite3 = sqlite3.connect("database.db")
#         curSqlite3 = conSqlite3.cursor()
#         curSqlite3.execute("INSERT INTO questoes (questao) VALUES(?)", [questao[2]])
#         conSqlite3.commit()    
#     cur.close()
#     conn.close()
#     return "ok"