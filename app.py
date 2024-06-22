import flet as ft
from models import Produto, session


def main(page: ft.Page):
    page.title = "Cadastro de produtos"
    
    product_list = ft.ListView()
    
    
    def cadastrar(e):
        try:
            new_Produto = Produto(titulo=produto.value, preco=preco_produto.value)
            session.add(new_Produto)
            session.commit()
            product_list.controls.append(
                ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                )
            )
            txt_error.visible = False
            txt_sucess.visible = True
        except:
            txt_error.visible = True
            txt_sucess.visible = False
                 
        page.update()

    txt_error = ft.Container(ft.Text("Erro ao salvar o produto"), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_sucess = ft.Container(ft.Text("Produto salvo com sucesso!"), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)
    
    txt_titulo = ft.Text("Titulo do produto:")
    produto = ft.TextField(label="Digite o título do produto...", text_align=ft.TextAlign.START)
    txt_preco = ft.Text("Preço do produto:")
    preco_produto = ft.TextField(label="Digite o preço do produto...", value=0)
    btn = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    
    
    for p in session.query(Produto).all():
        product_list.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )
    
    page.add(
        txt_sucess,
        txt_error,
        txt_titulo,
        produto,
        txt_preco,
        preco_produto,
        btn,
        product_list
    )
    
        



ft.app(target=main)