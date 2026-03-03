import flet as ft
def main(page: ft.Page):
    page.title = "Formulario de registro del eventos"
    txt_nombre = ft.TextField(
        label="nombre del evento",
        width=400
    )
    dropdown_tipo = ft.Dropdown(
        label="tipo de evento",
        width=300,
        options=[
            ft.dropdown.Option("conferencia"),
            ft.dropdown.Option("taller"),
            ft.dropdown.Option("reunión"),
        ]
    )
    radio_modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="presencial", label="presencial"),
            ft.Radio(value="virtual", label="virtual"),
        ])
    )
    check_inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?"
    )
    slider_duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} hora/s",
        value=1
    )
    txt_resumen = ft.Text(
        value="Resumen",
        size=16
    )
    def mostrar_resumen(e):
        nombre = txt_nombre.value
        tipo = dropdown_tipo.value
        modalidad = radio_modalidad.value
        inscripcion = "Sí" if check_inscripcion.value else "No"
        duracion = slider_duracion.value
        resumen = f"""
        Nombre: {nombre}
        Tipo: {tipo}
        Modalidad: {modalidad}
        Requiere inscripción previa: {inscripcion}
        Duración estimada: {duracion} hora/s
        """
        txt_resumen.value = resumen
        page.update()
    btn_resumen = ft.ElevatedButton(
        content=ft.Text("mostrar resumen"),
        on_click=mostrar_resumen
)
    page.add(
        ft.Text("Registro de evento", size=24, weight="bold"),
        txt_nombre,
        dropdown_tipo,
        ft.Text("Modalidad:"),
        radio_modalidad,
        check_inscripcion,
        ft.Text("Duración estimada (hora/s):"),
        slider_duracion,
        btn_resumen,
        ft.Divider(),
        txt_resumen
    )

ft.app(target=main)
