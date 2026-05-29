import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#region config_tela_livros

def montar_tela_livros(janela_livros, funcao_voltar):

    for widget in janela_livros.winfo_children():
        widget.destroy()

    janela_livros.geometry("500x550")
    janela_livros.title("Menu de livros")
    janela_livros.configure(fg_color="#dff3df")
    janela_livros.grid_columnconfigure(0, weight=1)
    janela_livros.grid_rowconfigure(0, weight=1)

    frame_livros = ctk.CTkFrame(
        janela_livros,
        width=400,
        height=450,
        fg_color="#cae9ca"
    )
    frame_livros.grid(row=1,column=0, padx=20, pady=25)
    frame_livros.grid_propagate(False)
    frame_livros.grid_columnconfigure(0,weight=1)


    #endregion

    #region btn_voltar

    ctk.CTkButton(
        janela_livros,
        text="← Voltar ao menu anterior",
        command=lambda: funcao_voltar(janela_livros),
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

    #region btn_cad_livros

    frame_cad_livros = ctk.CTkFrame(
        frame_livros,
        fg_color = "transparent",
        width = 300,
        height=60
    )
    frame_cad_livros.grid(row=1,column=0,pady=(40,5))

    cad_livros = ctk.CTkButton(
        frame_cad_livros,
        text="🕮 Cadastrar Livro",
        command=lambda: montar_tela_cadastrar_livro(janela_livros,montar_tela_livros,funcao_voltar),
        font=("Segoe UI Semibold",15),
        anchor="center",
        text_color="#fff",
        fg_color="#429259",
        hover_color="#347547",
        width = 225,
        height=40,
        corner_radius=5
        
    )
    cad_livros.grid(row=0,column=0)

    #endregion

    #region btn_edit_livro

    frame_edit_livros = ctk.CTkFrame(
        frame_livros,
        fg_color= "transparent",
        width=300,
        height=60
    )
    frame_edit_livros.grid(row=2,column=0, pady=(10,5))

    edit_livros = ctk.CTkButton(
        frame_edit_livros,
        text="🖉 Editar Livro",
        font=("Segoe UI Semibold", 15),
        anchor="center",
        text_color="#ffffff",
        fg_color="#429259",
        hover_color="#347547",
        width=225,
        height=40,
        corner_radius=5
    )
    edit_livros.grid(row=0,column=0)

    #endregion

    #region btn_delete_livro

    frame_del_livros = ctk.CTkFrame(
        frame_livros,
        fg_color="transparent",
        width=300,
        height=60
    )
    frame_del_livros.grid(row=3, column=0, pady=(10,5))

    del_livros = ctk.CTkButton(
        frame_del_livros,
        text="🗑 Excluir Livro",
        font=("Segoe UI Semibold",15),
        anchor="center",
        text_color="#fff",
        fg_color="#429259",
        hover_color="#347547",
        width= 225,
        height= 40,
        corner_radius=5
    )
    del_livros.grid(row=0,column=0)

    #endregion

    #region busca_livros

    frame_busc_livros = ctk.CTkFrame(
        frame_livros,
        fg_color="transparent",
        width=300,
        height=60
    )
    frame_busc_livros.grid(row=5, column=0, pady=(10,5))

    busca_livros = ctk.CTkButton(
        frame_busc_livros,
        text="⌕ Buscar Livros",
        font=("Segoe UI Semibold", 15),
        anchor="center",
        text_color="#fff",
        fg_color="#429259",
        hover_color="#347547",
        width=225,
        height=40,
        corner_radius=5
    )
    busca_livros.grid(row=0, column=0)
    #endregion

    #region cad_autor

    frame_cad_autor = ctk.CTkFrame(
        frame_livros,
        fg_color="transparent",
        width=300,
        height=60
    )
    frame_cad_autor.grid(row=6,column=0, pady=(10,5))

    cad_autor = ctk.CTkButton(
        frame_cad_autor,
        text="👤 Cadastrar Autor",
        font=("Segoe UI Semibold", 15),
        anchor="center",
        text_color="#fff",
        fg_color="#429259",
        hover_color="#347547",
        width=225,
        height=40,
        corner_radius=5
    )
    cad_autor.grid(row=0, column=0)

    #endregion

    #region edit_autor

    frame_edit_autor = ctk.CTkFrame(
        frame_livros,
        fg_color="transparent",
        width=300,
        height=60
    )
    frame_edit_autor.grid(row=7, column=0, pady=(10,5))

    edit_autor = ctk.CTkButton(
        frame_edit_autor,
        text="🛠 Editar Autor",
        font=("Segoe UI Semibold", 15),
        anchor="center",
        text_color="#fff",
        fg_color="#429259",
        hover_color="#347547",
        width=225,
        height=40,
        corner_radius=5
    )
    edit_autor.grid(row=0, column=0)

    #endregion


def montar_tela_cadastrar_livro(janela_cad_livros, voltar_livros, voltar_menu,):

    for widget in janela_cad_livros.winfo_children():
        widget.destroy()

    janela_cad_livros.title("Cadastrar Livro")
    janela_cad_livros.grid_columnconfigure(0, weight=1)

    ctk.CTkButton(
        janela_cad_livros,
        text="← Voltar ao menu anterior",
        command=lambda: voltar_livros(janela_cad_livros,voltar_menu),
        font=("Segoe UI Semibold", 12),
        text_color="#1E4D2B",
        hover_color="#8abb8c",
        width=150,
        fg_color="#adc2ae",
        border_color="#020e05",
        border_width=1,
        corner_radius=5
    ).grid(row=0, column=0, sticky="w", padx=10)