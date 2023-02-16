import flet as ft

from ieee754 import *


class IEEE754GUI:
    def __init__(self):
        self.length_list = [16, 32, 64, 128, 256]
        self.exponent_list = [5, 8, 11, 15, 19]
        self.mantissa_list = [10, 23, 52, 112, 236]

        self.test_text = ft.Text(value="", size=20)
        self.precision_dropdown = ft.Dropdown(
            label="Precision Type",
            hint_text="Please select your precision type",
            width=643,
            autofocus=True,
            on_change=self.dropdown_change,

            options=[
                ft.dropdown.Option(key=0, text="Half Precision"),
                ft.dropdown.Option(key=1, text="Single Precision"),
                ft.dropdown.Option(key=2, text="Double Precision"),
                ft.dropdown.Option(key=3, text="Quadruple Precision"),
                ft.dropdown.Option(key=4, text="Octuple Precision"),

            ],

        )

        self.sign = ft.TextField(label="Sign bit", value="1", disabled=True, width=127)
        self.plus = ft.Icon(name=ft.icons.ADD_ROUNDED)
        self.exponent = ft.TextField(label="Exponent bit", value="11", disabled=True, width=127)
        self.mantissa = ft.TextField(label="Mantissa bit", value="52", disabled=True, width=127)
        self.arrow = ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED)
        self.total_bits = ft.TextField(label="Total bits", value="64", disabled=True, width=127)

        self.input = ft.TextField(label="Enter a number", hint_text="Please enter a number",
                                  keyboard_type="number", text_align="center", text_size=20, icon=ft.icons.INPUT,
                                  bgcolor="red")

        self.convert_button = ft.ElevatedButton(text="Convert", style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10), padding=20
        ), on_click=self.convert)

        self.result = ft.Text(value="", size=20, weight="bold")
        self.result_hex = ft.Text(value="", size=20, weight="bold")

        self.result_text = ft.Text(value="Result:", size=30, weight="bold")
        self.result_hex_text = ft.Text(value="Hex Representation:", size=30, weight="bold")

    def __call__(self, page: ft.Page):
        self.page = page
        self.page.padding = 30
        self.page_style()

        self.page.add(
            ft.Row(
                controls=[
                    self.precision_dropdown,

                ],
                alignment="center",

            )
        )
        self.page.add(
            ft.Row(
                controls=[
                    self.test_text
                ],
                alignment="center",

            )
        )
        self.page.add(
            ft.Container(
                ft.Row(
                    controls=[
                        self.sign,
                        self.plus,
                        self.exponent,
                        self.plus,
                        self.mantissa,
                        self.arrow,
                        self.total_bits
                    ],
                    alignment="center"
                ),
                padding=25
            )
        )
        self.page.add(
            ft.Row(
                controls=[
                    self.input

                ],
                alignment="center"
            )
        )
        self.page.add(
            ft.Row(
                controls=[
                    self.convert_button
                ],
                alignment="center",

            )
        )
        self.page.add(
            ft.Column(
                controls=[
                    self.result_text,
                    self.result,
                    self.result_hex_text,
                    self.result_hex

                ],
                alignment="center",
                horizontal_alignment="center",
                width=self.page.width
            )
        )

        self.page.update()

    def dropdown_change(self, e):
        self.test_text.value = f"Precision changed to {self.precision_dropdown.value}"
        self.exponent.value = self.exponent_list[int(self.precision_dropdown.value)]
        self.mantissa.value = self.mantissa_list[int(self.precision_dropdown.value)]
        self.total_bits.value = 1 + self.exponent_list[int(self.precision_dropdown.value)] + self.mantissa_list[
            int(self.precision_dropdown.value)]

        self.page.update()

    def convert(self, e):
        b = IEEE754(float(self.input.value), int(self.precision_dropdown.value))

        self.result.value = f"{b}"
        self.result_hex.value = f"{b.str2hex().upper()}"

        self.page.update()

    def page_style(self):
        self.page.theme_mode = "dark"
        self.page.title = "IEEE754 Precision Converter"


if __name__ == "__main__":
    ft.app(target=IEEE754GUI())
    # ft.app(target=main, view=ft.WEB_BROWSER)  WEB BROWSER
