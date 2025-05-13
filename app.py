# app.py

import tkinter as tk
from constants import value, Multi, Tol, color
from ui import create_widgets


class ResistorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Resistores")
        self.root.geometry("600x400")

        self.faixas = 4
        self.opcoes = [tk.StringVar(value=color[0]) for _ in range(5)]

        create_widgets(self)

    def set_faixas(self, n):
        """Define o número de faixas e atualiza os menus."""
        self.faixas = n
        for i in range(5):
            self.color_menus[i]["state"] = tk.NORMAL if i < n else tk.DISABLED
        self.atualizar_resistor()

    def calcular_valor_resistor(self):
        """Calcula o valor do resistor com base nas faixas."""
        try:
            if self.faixas == 4:
                d1 = value[self.opcoes[0].get()]
                d2 = value[self.opcoes[1].get()]
                mult = Multi[self.opcoes[2].get()]
                tol = Tol.get(self.opcoes[3].get(), "±20%")
                valor = (d1 * 10 + d2) * mult
            else:
                d1 = value[self.opcoes[0].get()]
                d2 = value[self.opcoes[1].get()]
                d3 = value[self.opcoes[2].get()]
                mult = Multi[self.opcoes[3].get()]
                tol = Tol.get(self.opcoes[4].get(), "±20%")
                valor = (d1 * 100 + d2 * 10 + d3) * mult

            if valor >= 1_000_000:
                valor_str = f"{valor / 1_000_000:.2f} MΩ"
            elif valor >= 1_000:
                valor_str = f"{valor / 1_000:.2f} KΩ"
            else:
                valor_str = f"{valor} Ω"

            return valor_str, tol

        except KeyError:
            return None, "Erro na seleção de cores."

    def atualizar_resistor(self, *args):
        """Atualiza o desenho do resistor e o valor."""
        self.canvas.delete("all")

        self.canvas.create_rectangle(100, 40, 400, 60, fill="gray", outline="black")
        self.canvas.create_line(50, 50, 100, 50, width=4)
        self.canvas.create_line(400, 50, 450, 50, width=4)

        posicoes = [120, 170, 220, 270, 320]
        for i in range(self.faixas):
            cor = self.opcoes[i].get()
            self.canvas.create_rectangle(posicoes[i], 40, posicoes[i] + 10, 60, fill=cor.lower())

        valor_str, tol = self.calcular_valor_resistor()
        if valor_str:
            self.result_label.config(text=f"Valor: {valor_str} {tol}")
        else:
            self.result_label.config(text=f"Valor: {tol}")
