import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#region config_tela
# Janela
janela_principal = ctk.CTk()
janela_principal.geometry("500x600")
janela_principal.title("Menu Principal")
janela_principal.grid_columnconfigure(0, weight=1)
janela_principal.grid_rowconfigure(0, weight=1)

frame_principal = ctk.CTkFrame(
    janela_principal,
    width=400,
    height=500,
    fg_color="#5eb373",
    border_color="#65dd36",
    border_width=1.5,
    corner_radius=10
)
frame_principal.grid(row=0, column=0, padx=20, pady=20)
frame_principal.grid_propagate(False)
frame_principal.grid_columnconfigure(0,weight=1)
#endregion

#region principal
frame_titulo_principal = ctk.CTkFrame(
    frame_principal,
    fg_color="#5eb373",
    width=300,
    height=50
)
frame_titulo_principal.grid(row=0, column=0, pady=(35))

title_principal = ctk.CTkLabel(
    frame_titulo_principal,
    text="Bem-vindo ao Menu Principal",
    font=("Segoe UI Semibold",25),
    text_color="#000000"
)
title_principal.grid(row=0, column=0)
#endregion

#region botao_livros

frame_btn_livros = ctk.CTkFrame(
    frame_principal,
    fg_color="transparent",
    width=250,
    height=75
)
frame_btn_livros.grid(row=1, column=0, pady=10)

btn_livros = ctk.CTkButton(
    frame_btn_livros,
    text="Livros",
    font=("Segoe UI Semibold", 20),
    width=175,
    height=30,
    fg_color="#094217",
    border_color="#0d3a07",
    border_width=1.3,
    corner_radius=5
)
btn_livros.grid(row=0,column=0)

#endregion

#region btn_alunos
frame_btn_alunos = ctk.CTkFrame(
    frame_principal,
    fg_color="transparent",
    width=250,
    height=75
)
frame_btn_alunos.grid(row=2, column=0, pady=10)

btn_alunos = ctk.CTkButton(
    frame_btn_alunos,
    text="Alunos",
    font=("Segoe UI Semibold", 20),
    width=175,
    height=30,
    fg_color="#094217",
    border_color="#0d3a07",
    border_width=1.3,
    corner_radius=5
)
btn_alunos.grid(row=0, column=0)
#endregion

#region btn_emp
frame_btn_emp = ctk.CTkFrame(
    frame_principal,
    fg_color="transparent",
    width=250,
    height=75
)
frame_btn_emp.grid(row=3, column=0, pady=10)

btn_emp = ctk.CTkButton(
    frame_btn_emp,
    text="Empréstimos",
    font=("Segoe UI Semibold", 20),
    width=175,
    height=30,
    fg_color="#094217",
    border_color="#0d3a07",
    border_width=1.3,
    corner_radius=5
)
btn_emp.grid(row=0, column=0)


#endregion

#region btn_backup

frame_btn_backup = ctk.CTkFrame(
    frame_principal,
    fg_color="transparent",
    width=250,
    height=75
)
frame_btn_backup.grid(row=4, column=0, pady=10)

btn_backup = ctk.CTkButton(
    frame_btn_backup,
    text="Backup",
    font=("Segoe UI Semibold", 20),
    width=175,
    height=30,
    fg_color="#094217",
    border_color="#0d3a07",
    border_width=1.3,
    corner_radius=5
)
btn_backup.grid(row=0, column=0)
#endregion

#region btn_sair

frame_btn_sair = ctk.CTkFrame(
    frame_principal,
    fg_color="transparent",
    width=250,
    height=75
)
frame_btn_sair.grid(row=5, column=0, pady=40)

btn_sair= ctk.CTkButton(
    frame_btn_sair,
    text="Sair",
    font=("Segoe UI Semibold", 15),
    width=90,
    height=30,
    fg_color="#cc1919",
    border_color="#000000",
    border_width=1.3,
    corner_radius=5,
    hover_color="#cf4a4a"
)
btn_sair.grid(row=0, column=0)
#endregion













janela_principal.mainloop()