import requests

import flet as ft

AUTH_URL = "http://127.0.0.1:8000/user/signin/"
SIGNUP_URL = "http://127.0.0.1:8000/user/signup/"

def main(page: ft.Page):
    page.title = "Tu sitio de Guiones"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def route_change(route):
        page.views.clear()

        if page.route == "/":
            welcome_text = ft.Text(
                "Bienvenido a tu sitio de Guiones",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER
            )
            
            sign_in_button = ft.ElevatedButton(
                text="Sign In",
                on_click=lambda _: page.go("/signin"),
                width=200,
                height=50
            )
            
            sign_up_button = ft.ElevatedButton(
                text="Sign Up",
                on_click=lambda e: page.go("/signup"),
                width=200,
                height=50
            )
            
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Film Script"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Column(
                            controls=[
                                welcome_text,
                                ft.Container(height=50),  # Espaciador
                                sign_in_button,
                                ft.Container(height=20),  # Espaciador
                                sign_up_button
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ]
                )
            )
        
        if page.route == "/signin":

            def login_click(e):
                email = email_input.value
                password = password_input.value
                data = {
                    "email": email,
                    "password": password
                }
                response = requests.post(AUTH_URL, json=data)
                
                if str(response.status_code).startswith("2"):
                    token = response.json()["token"]
                    print(token)
                    page.session.set("token", f"Token {token}")
                    page.go("/filmscript")
                
                else:
                    page.go("/")
                
            signin_text = ft.Text(
                "Ingresa",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER
            )
            invalid_text = ft.Text(
                "email ó contraseña incorrecta",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.RED,
                text_align=ft.TextAlign.CENTER,
                visible=False
            )
            
            email_input = ft.TextField(label="Email", width=300)
            password_input = ft.TextField(label="Password", password=True, width=300)
            login_button = ft.ElevatedButton(text="Login", on_click=login_click)
            signup_button = ft.ElevatedButton(
                text="Signup", 
                on_click=lambda _: page.go("/signup")
            )
            
            page.views.append(
                ft.View(
                    "/signin",
                    [
                        ft.AppBar(title=ft.Text("Sign In"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Column(
                            controls=[
                                signin_text,
                                ft.Container(height=50),  # Espaciador
                                email_input,
                                ft.Container(height=20),  # Espaciador
                                password_input,
                                ft.Container(height=20),  # Espaciador
                                invalid_text,
                                ft.Container(height=20),  # Espaciador
                                ft.Row(
                                    controls=[
                                        login_button,
                                        ft.Container(width=10),  # Espaciador
                                        signup_button,
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ]
                )
            )
        
        if page.route == "/signup":
            def signup_click(e):
                email = email_input.value
                password = password_input.value
                name = name_input.value
                data = {
                    "name": name,
                    "email": email,
                    "password": password
                }
                
                response = requests.post(SIGNUP_URL, json=data)
                
                if str(response.status_code).startswith("2"):
                    body_response = response.json()
                    print(body_response)
                    page.go("/signin")
                
                else:
                    page.go("/")

            signup_text = ft.Text(
                "Registrate",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.WHITE,
                text_align=ft.TextAlign.CENTER
            )
            
            email_input = ft.TextField(label="Email", width=300)
            password_input = ft.TextField(label="Password", password=True, width=300)
            name_input = ft.TextField(label="Name", width=300)
            signup_button = ft.ElevatedButton(
                text="Signup", 
                on_click=signup_click
            )
            
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(title=ft.Text("Sign Up"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Column(
                            controls=[
                                signup_text,
                                ft.Container(height=50),  # Espaciador
                                name_input,
                                ft.Container(height=20),  # Espaciador
                                email_input,
                                ft.Container(height=20),  # Espaciador
                                password_input,
                                ft.Container(height=20),  # Espaciador
                                signup_button,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    ]
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
