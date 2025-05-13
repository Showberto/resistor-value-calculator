# ui.py

import tkinter as tk
from tkinter import ttk
from constants import color


def create_widgets(app):
    """Cria todos os widgets (botões, menus, etc.)."""
    tipo_frame = ttk.LabelFrame(app.root, text="Tipo de Resistor")
    tipo_frame.pack(pady=10)

    ttk.Button(tipo_frame, text="4 Faixas", command=lambda: app.set_faixas(4)).pack(side=tk.LEFT, padx=5)
    ttk.Button(tipo_frame, text="5 Faixas", command=lambda: app.set_faixas(5)).pack(side=tk.LEFT, padx=5)

    # Frame para seleção das faixas de cores
    app.inputs_frame = ttk.LabelFrame(app.root, text="Selecione as Cores")
    app.inputs_frame.pack(pady=10)

    app.color_menus = []
    for i in range(5):
        label = ttk.Label(app.inputs_frame, text=f"{i+1}ª Faixa:")
        label.grid(row=0, column=i, padx=5)
        menu = ttk.OptionMenu(app.inputs_frame, app.opcoes[i], app.opcoes[i].get(), *color, command=app.atualizar_resistor)
        menu.grid(row=1, column=i, padx=5)
        app.color_menus.append(menu)

    # Canvas para desenhar o resistor
    app.canvas = tk.Canvas(app.root, width=500, height=100, bg="white")
    app.canvas.pack(pady=10)

    # Label para mostrar o resultado
    app.result_label = ttk.Label(app.root, text="Valor: ")
    app.result_label.pack(pady=5)

    app.atualizar_resistor()
