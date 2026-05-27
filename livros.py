import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#region config_tela_livros


janela_livros = ctk.CTk()
janela_livros.geometry("500x600")
janela_livros.title("Menu de livros")
janela_livros.configure(fg_color="#dfecdf")
janela_livros.grid_columnconfigure(0, weight=1)
janela_livros.grid_rowconfigure(0, weight=1)

frame_livros = ctk.CTkFrame(
    janela_livros,
    width=400,
    height=500,
    fg_color="#dfecdf"
)
frame_livros.grid(row=1,column=0, padx=20, pady=25)
frame_livros.grid_propagate(False)
frame_livros.grid_columnconfigure(0,weight=1)


#endregion

#region btn_voltar

ctk.CTkButton(
    janela_livros,
    text="← Voltar ao menu anterior",
    font=("Segoe UI Semibold", 12),
    text_color="#1E4D2B",
    hover_color="#8abb8c",
    width=150,
    fg_color="#adc2ae",
    border_color="#020e05",
    border_width=1,
    corner_radius=5
).grid(row=0, column=0, sticky="w", padx=10)

#endregion

#region titulo

frame_titulo_livros = ctk.CTkFrame(
    frame_livros,
    fg_color="transparent",
    width=300,
    height=50
)
frame_titulo_livros.grid(row=0, column=0,pady=(0,5))

title_livros = ctk.CTkLabel(
    frame_titulo_livros,
    text="GERENCIAMENTO DE LIVROS",
    font=("Segoe UI Semibold",24),
    text_color="#163822"
)
title_livros.grid(row=0,column=0)
#endregion

#region 







janela_livros.mainloop()