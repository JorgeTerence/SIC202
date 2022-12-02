import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Mini-míssil")
        self.geometry("290x170")

        self.txt_distance = ctk.CTkEntry(master=self, placeholder_text="Distância (m)")
        self.txt_distance.pack(pady=(15, 0), padx=15, anchor=ctk.NW)

        self.btn_calc = ctk.CTkButton(
            master=self, text="Calcular ângulo", command=self.calc
        )
        self.btn_calc.pack(pady=(16, 6), padx=15, anchor=ctk.NW)

        self.res = ctk.StringVar()
        self.lbl_res = ctk.CTkLabel(master=self, textvariable=self.res)
        self.lbl_res.pack(pady=10, padx=15, anchor=ctk.NW)

    def calc(self):
        self.lbl_res.fg_color = "#FF0000"
        distance = self.txt_distance.get()

        try:
            s = int(distance)
            if s < 0:
                self.res.set("Digite um valor positivo")
                return

            res = 38.6 + 0.596 * s

            if res >= 60:
                self.res.set("Fora de alcance")
                return

            self.lbl_res.fg_color = "green"
            self.res.set("Ângulo: " + str(round(res, 2)) + "°")

        except ValueError:
            self.res.set("Digite um número!")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = App()
    app.mainloop()
