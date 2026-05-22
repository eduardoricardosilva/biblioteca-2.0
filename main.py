import customtkinter as ctk
import login
import sqlite3
from CTkMessagebox import CTkMessagebox



def validar_e_entrar(usuario, senha):
    try:
        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM user WHERE email = ? AND senha = ?",
            (usuario, senha)
        )

        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            CTkMessagebox(
                title="Login",
                message="Sucesso!",
                icon="check"
            )

            for widget in janela_login.winfo_children():
                widget.destroy()

            montar_menu_principal(janela_login)

        else:
            CTkMessagebox(
                title="Login",
                message="E-mail ou senha inválidos!",
                icon="cancel"
            )

    except Exception as e:
        CTkMessagebox(
            title="Erro",
            message=f"Erro ao conectar no banco: {e}",
            icon="cancel"
        )


janela_login = ctk.CTk()
tela_login(janela_login, validar_e_entrar)
janela_login.mainloop()