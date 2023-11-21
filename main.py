import flet as ft
from datetime import datetime
import sqlite3


# dedo, corLetra, corFundo
violao = [
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None],
    ["--", ft.colors.BLUE, None]
]


def main(page: ft.Page):   

    dlg = ft.AlertDialog(
        title=ft.Text("Escala Salva!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    # def close_dlg(e):
    #     dlg_modal.open = False
    #     page.update()

    # def confirmar_dlg(e):
    #     dlg_modal.open = False
    #     # e.control.text = "1"
    #     e.control.update()
    #     page.update()

    # dlg_modal = ft.AlertDialog(
    #     modal=True,
    #     title=ft.Text("Please confirm"),
    #     content=ft.TextField(label="1,2,3,4", read_only=False, value="1"),
    #     actions=[
    #         ft.TextButton("Confirmar", on_click=confirmar_dlg),
    #         ft.TextButton("Cancelar", on_click=close_dlg),
    #     ],
    #     actions_alignment=ft.MainAxisAlignment.END,
    #     on_dismiss=lambda e: print("Modal dialog dismissed!"),

    # )    

    def button_clicked(e):               
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
        global violao
        print(violao)
        violao[int(e.control.data)] = [e.control.text, e.control.color, e.control.bgcolor]    
        print(violao[int(e.control.data)])            
        e.control.update()

    # strings
    # page.client_storage.set("key", "value")

    # # numbers, booleans
    # page.client_storage.set("number.setting", 12345)
    # page.client_storage.set("bool_setting", True)

    # # lists
    # page.client_storage.set("favorite_colors", ["read", "green", "blue"])
    def reiniciar():
        global violao
        violao = [
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None],
            ["--", ft.colors.BLUE, None]
        ]


    def salvar(e):
        print("chamou o salvar")
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        global violao
        print(dt_string)
        print(violao)
        # salvando
        conn = sqlite3.connect("./assets/database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM shapes")
        shape = cur.fetchone()
        print(shape)
        cur.close()
        conn.close()

        # page.client_storage.set(dt_string, violao)
        reiniciar()
        open_dlg(e)     

    # print(page.client_storage.get_keys("key-prefix."))
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text(""))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="1")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="2")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="3")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="4")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="5"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                      ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="6")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="7")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="8")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="9")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="10"))
                    ],
                ),
                ft.DataRow(
                    cells=[
                   ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="11")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="12")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="13")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="14")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="15"))            ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="16")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="17")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="18")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="19")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="20"))
                    ],
                ),
                  ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="21")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="22")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="23")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="24")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="25"))
                    ],
                ),
                  ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="26")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="27")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="28")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="29")),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked, data="30"))
                    ],
                )
                
            ],
        )
    )

    page.add(ft.ElevatedButton(text="Salvar", on_click=salvar))
    # recuperar chave salva
    print(page.client_storage.get("*"))

# https://flet.dev/docs/guides/python/testing-on-android/
# https://flet.dev/docs/cli/run/

# para rodar como app
#  pip install flet --upgrade
# flet run main.py --android

# para rodar como desktop
# python main.py

# destop
# ft.app(target=main)

# web
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

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