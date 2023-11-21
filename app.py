import flet as ft

def main(page: ft.Page):

    # def open_dlg_modal(e):
    #     page.dialog = dlg_modal
    #     dlg_modal.open = True
    #     e.control.text = "1"
    #     e.control.update()
    #     page.update()

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
        
        # elif (e.control.text == "2"):
        #     e.control.text = "3"
        # elif (e.control.text == "3"):
        #     e.control.text = "4"
        # elif (e.control.text == "4"):
        #     e.control.text = "--"
        e.control.update()



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
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked)),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10), on_click=button_clicked)),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                ),
                ft.DataRow(
                    cells=[
                      ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                ),
                ft.DataRow(
                    cells=[
                   ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                ),
                  ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                ),
                  ft.DataRow(
                    cells=[
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10))),
                        ft.DataCell(ft.ElevatedButton(text="--", style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=10)))
                    ],
                )
                
            ],
        ),
    )


ft.app(target=main)