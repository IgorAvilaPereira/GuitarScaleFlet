import flet as ft
from datetime import datetime

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
        # print(violao)
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
    def salvar(e):
        print("chamou o salvar")
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        global violao
        print(dt_string)
        print(violao)
        # salvando
        page.client_storage.set(dt_string, violao)
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
        open_dlg(e)     

    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("1")),
                ft.DataColumn(ft.Text("2")),
                ft.DataColumn(ft.Text("3")),
                ft.DataColumn(ft.Text("4")),
                ft.DataColumn(ft.Text("5"))
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
        ),
    )

    page.add(ft.ElevatedButton(text="Salvar", on_click=salvar))
    # recuperar chave salva
    print(page.client_storage.get("20_11_2023_22_44_32"))

# https://flet.dev/docs/guides/python/testing-on-android/
# https://flet.dev/docs/cli/run/

# para rodar como app
#  pip install flet --upgrade
# flet run main.py --android

# para rodar como desktop
# python main.py

ft.app(target=main)