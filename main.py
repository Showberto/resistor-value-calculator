# main.py

from app import ResistorApp
import tkinter as tk


def main():
    """Função principal para executar o aplicativo."""
    root = tk.Tk()
    app = ResistorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
