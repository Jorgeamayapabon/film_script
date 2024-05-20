import flet as ft
import requests

BASE_URL = "http://localhost:8000/api/"  # Cambia esto si tu servidor Django está en otra URL

def main(page: ft.Page):

    def obtener_guiones():
        response = requests.get(f"{BASE_URL}guiones/")
        if response.status_code == 200:
            guiones = response.json()
            lista_guiones.controls.clear()
            for guion in guiones:
                lista_guiones.controls.append(ft.Text(f"{guion['titulo']}"))
            page.update()

    def crear_guion(e):
        titulo = input_titulo.value
        contenido = input_contenido.value
        response = requests.post(f"{BASE_URL}guiones/", json={'titulo': titulo, 'contenido': contenido})
        if response.status_code == 201:
            obtener_guiones()

    lista_guiones = ft.Column()
    input_titulo = ft.TextField(label="Título")
    input_contenido = ft.TextField(label="Contenido", multiline=True)
    boton_crear = ft.ElevatedButton(text="Crear Guion", on_click=crear_guion)

    page.add(
        ft.Column([
            input_titulo,
            input_contenido,
            boton_crear,
            ft.Text("Guiones:"),
            lista_guiones
        ])
    )

    obtener_guiones()

ft.app(target=main)
