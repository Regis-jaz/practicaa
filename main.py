import flet as ft

def main(page: ft.Page):
    
    page.add(ft.TextField(
        label="Nombre",
        hint_text="Ingresa tu nombre",
        value="",
        prefix_icon=ft.Icons.PERSON,
        suffix=ft.Text(".com"),
        password=False,
        can_reveal_password=False,
        multiline=False,
        max_length=50,
        keyboard_type=ft.KeyboardType.TEXT,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.BLUE,
        focused_border_color=ft.Colors.RED,
        filled=True,
        bgcolor=ft.Colors.GREY_100,
        on_change=lambda e: print(e.control.value),
        on_submit=lambda e: print("Enter presionado")))
    
    page.add(ft.Checkbox(
            label="Acepto términos",
            value=False,
            tristate=False,
            check_color=ft.Colors.WHITE,
            fill_color=ft.Colors.GREEN,
            on_change=lambda e: print(f"Estado: {e.control.value}")))
    
    
    
    page.add(ft.Text(
        value="Hola mundo",
        size=24,
        color=ft.Colors.PINK,
        weight=ft.FontWeight.BOLD,
        italic=False,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    ))
    
    page.add(ft.Image(
        src="https://picsum.photos/200/200",
        width=200,
        height=200,
        border_radius=ft.BorderRadius.all(10),
        repeat=ft.ImageRepeat.NO_REPEAT
    ))  
    
    page.add(ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400))
    page.add(ft.Row([
        ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    ]))
    
ft.app(target=main)
