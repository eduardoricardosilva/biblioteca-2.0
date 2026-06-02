import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
import sqlite3

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#region BOTÕES DA TELA

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
        command=lambda: montar_tela_editar_livro(janela_livros,montar_tela_livros,funcao_voltar),
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
#endregion

#region do botão de cadastro de livros


def montar_tela_cadastrar_livro(janela_cad_livros, voltar_livros, voltar_menu,):

    for widget in janela_cad_livros.winfo_children():
        widget.destroy()

    janela_cad_livros.geometry("500x550")
    janela_cad_livros.configure(fg_color="#dff3df")
    janela_cad_livros.grid_columnconfigure(0, weight=1)
    janela_cad_livros.grid_rowconfigure(0, weight=1)
    janela_cad_livros.title("Cadastrar Livro")

    frame_tela_cad_livros = ctk.CTkFrame(
        janela_cad_livros,
        width=400,
        height=450,
        fg_color="#cae9ca"
    )
    frame_tela_cad_livros.grid(row=1,column=0, padx=20, pady=25)
    frame_tela_cad_livros.grid_propagate(False)
    frame_tela_cad_livros.grid_columnconfigure(0,weight=1)
    frame_tela_cad_livros.grid_columnconfigure(1, weight=1)
    

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
    ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

    titulo = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="CADASTRAR LIVRO",
        font=("Segoe UI Semibold",24),
        text_color="#163822"
    )
    titulo.grid(row=0,column=0,columnspan=2,pady=20)

#==========TITULO DO LIVRO==========

    label_titulo_cad = ctk.CTkLabel(
            frame_tela_cad_livros,
            text="Título do livro",
            font=("Segoe UI Semibold", 12),
            text_color="#000",
    )
    label_titulo_cad.grid(row=1, column=0, pady=0)
    entry_titulo = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_titulo.grid(row=2, column=0, pady=(0,10))

#========EDITORA==========

    label_editora = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Editora",
        font=("Segoe UI Semibold", 12),
            text_color="#000",
    )
    label_editora.grid(row=1, column=1, pady=0)
    entry_editora = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_editora.grid(row=2, column=1, pady=(0,10))

#==========QUANTIDADE DE LIVRO==========

    label_quant = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Quantidade",
        font=("Segoe UI Semibold", 12),
        text_color="#000",
    )
    label_quant.grid(row=3, column=0, pady=0)
    entry_quant = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_quant.grid(row=4, column=0, pady=(0,10))

#==========ISBN==========

    label_isbn = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="ISBN",
        font=("Segoe UI Semibold", 12),
        text_color="#000",
    )
    label_isbn.grid(row=3, column=1,pady=0)
    entry_isbn = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_isbn.grid(row=4,column=1,pady=(0,10))

#================FUNÇÕES=================

    def carregar_generos():
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("SELECT nome FROM generos ORDER BY nome ASC")
            resultados = cursor.fetchall()
            conn.close()
            lista_generos = [genero[0] for genero in resultados]
            return lista_generos
        except sqlite3.Error as erro:
            print(f"Erro ao buscar dados {erro}")
            return []


    def carregar_autores():
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("SELECT nome FROM autores ORDER BY nome ASC")
            resultados = cursor.fetchall()
            conn.close()
            lista_autores = [autores[0] for autores in resultados]
            return lista_autores
        except sqlite3.Error as erro:
            print(f"Erro ao buscar dados {erro}")
            return[]

    def salvar_livro():
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()

            titulo = entry_titulo.get()
            editora = entry_editora.get()
            quantidade = entry_quant.get()
            isbn = entry_isbn.get()
            genero_selecionado = combo_genero.get()
            novo_genero = entry_cad_genero.get()
            autor_selecionado = combo_autor.get()
            novo_autor = entry_cad_autor.get()

            if titulo == "":
                CTkMessagebox(
                    title="Aviso",
                    message="Digite o título do livro",
                    icon="warning")
                return

            elif editora == "":
                CTkMessagebox(
                    title="Aviso",
                    message="Digite a editora do livro",
                    icon="warning")
                return
            
            elif quantidade == "":
                CTkMessagebox(
                    title="Aviso",
                    message="Digite a quantidade de livros",
                    icon="warning")
                return
            
            elif isbn == "":
                CTkMessagebox(
                    title="Aviso",
                    message="Digite o ISBN do livro",
                    icon="warning")
                return

            elif novo_genero == "" and genero_selecionado == "Selecione...":
                CTkMessagebox(
                    title="Aviso",
                    message="Selecione ou cadastre um gênero",
                    icon="warning")
                return
                

            elif novo_autor == "" and autor_selecionado == "Selecione...":
                CTkMessagebox(
                    title="Aviso",
                    message="Selecione ou cadastre um autor",
                    icon="warning")
                return


            else:
                if novo_genero != "":
                    genero_usado = novo_genero

                    cursor.execute(
                        "INSERT OR IGNORE INTO generos (nome) VALUES (?)",
                        (genero_usado,)
                    )
                else:
                    genero_usado = genero_selecionado

                cursor.execute(
                    "SELECT id FROM generos WHERE nome = ?",
                    (genero_usado,)
                )
                resultado_genero = cursor.fetchone()
                genero_id = resultado_genero[0]

                if novo_autor != "":
                    autor_usado = novo_autor

                    cursor.execute(
                        "INSERT OR IGNORE INTO autores (nome) VALUES (?)",
                        (autor_usado,)
                    )
                else:
                    autor_usado = autor_selecionado

                cursor.execute(
                    "SELECT id FROM autores WHERE nome = ?",
                    (autor_usado,)
                )
                resultado_autor = cursor.fetchone()
                autor_id = resultado_autor[0]

                cursor.execute(
                    """
                    INSERT INTO livros (
                        titulo, editora, quantidade, isbn, genero_id, autor_id
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (titulo, editora, quantidade, isbn, genero_id, autor_id)
                )

                conn.commit()
                conn.close()

                CTkMessagebox(
                    title="Sucesso",
                    message="Livro cadastrado com sucesso",
                    icon="check"
                )

                combo_genero.configure(values=carregar_generos())
                combo_autor.configure(values=carregar_autores())

                entry_titulo.delete(0,"end")
                entry_editora.delete(0,"end")
                entry_quant.delete(0, "end")
                entry_isbn.delete(0, "end")
                entry_cad_genero.delete(0, "end")
                entry_cad_autor.delete(0, "end")

                combo_genero.set("Selecione...")
                combo_autor.set("Selecione...")
            


        except sqlite3.Error as erro:
            print(f"Erro ao buscar dados {erro}")
            return[]

#==========GÊNERO DO LIVRO==========

    label_genero = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Selecione o gênero",
        font=("Segoe UI Semibold", 12),
        text_color="#000",
    )
    label_genero.grid(row=5, column=0,pady=0)

    label_ou = ctk.CTkLabel(
    frame_tela_cad_livros,
    text="ou",
    font=("Segoe UI Semibold", 11),
    text_color="#da1717"
    )
    label_ou.grid(row=5,column=0,columnspan=2,pady=5)

    lista_generos = carregar_generos()

    combo_genero = ctk.CTkComboBox(
        frame_tela_cad_livros,
        width=160,
        values=lista_generos,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_genero.grid(row=6, column=0,pady=(0,10))
    combo_genero.set("Selecione...")

    label_cad_genero = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Cadastre novo gênero",
        font=("Segoe UI Semibold", 12),
        text_color="#000"
    )
    label_cad_genero.grid(row=5,column=1, pady=0)
    entry_cad_genero = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_cad_genero.grid(row=6, column=1,pady=(0,10))

#==========AUTOR DO LIVRO==========
    label_autor = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Selecione o autor",
        font=("Segoe UI Semibold", 12),
        text_color="#000",
    )
    label_autor.grid(row=7, column=0,pady=0)

    label_ou = ctk.CTkLabel(
    frame_tela_cad_livros,
    text="ou",
    font=("Segoe UI Semibold", 11),
    text_color="#da1717"
    )
    label_ou.grid(row=7,column=0,columnspan=2,pady=5)

    lista_autores = carregar_autores()
    print(lista_autores)

    combo_autor = ctk.CTkComboBox(
        frame_tela_cad_livros,
        width=160,
        values=lista_autores,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_autor.grid(row=8, column=0,pady=(0,10))
    combo_autor.set("Selecione...")

    label_cad_autor = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="Cadastre novo autor",
        font=("Segoe UI Semibold", 12),
        text_color="#000"
    )
    label_cad_autor.grid(row=7,column=1, pady=0)
    entry_cad_autor = ctk.CTkEntry(
        frame_tela_cad_livros,
        width=160,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    entry_cad_autor.grid(row=8, column=1,pady=(0,10))

#==========BOTÂO SALVAR LIVRO==========

    btn_salvar = ctk.CTkButton(
        frame_tela_cad_livros,
        text="Salvar Livro",
        command=salvar_livro,
        font=("Segoe UI Semibold", 15),
        fg_color="#429259",
        width=130,
        height=35
    )
    btn_salvar.grid(row=9, column=0, columnspan=2,pady=20)

#endregion

#region do botão de editar livro

def montar_tela_editar_livro(janela_edit_livros, voltar_livros, voltar_menu,):

    for widget in janela_edit_livros.winfo_children():
        widget.destroy()

    janela_edit_livros.geometry("500x550")
    janela_edit_livros.configure(fg_color="#dff3df")
    janela_edit_livros.grid_columnconfigure(0, weight=1)
    janela_edit_livros.grid_rowconfigure(0, weight=1)
    janela_edit_livros.title("Editar Livro")

    frame_tela_edit_livros = ctk.CTkFrame(
        janela_edit_livros,
        width=400,
        height=450,
        fg_color="#cae9ca"
    )
    frame_tela_edit_livros.grid(row=1,column=0, padx=20, pady=25)
    frame_tela_edit_livros.grid_propagate(False)
    frame_tela_edit_livros.grid_columnconfigure(0,weight=1)
    frame_tela_edit_livros.grid_columnconfigure(1, weight=1)
    

    ctk.CTkButton(
        janela_edit_livros,
        text="← Voltar ao menu anterior",
        command=lambda: voltar_livros(janela_edit_livros,voltar_menu),
        font=("Segoe UI Semibold", 12),
        text_color="#1E4D2B",
        hover_color="#8abb8c",
        width=150,
        fg_color="#adc2ae",
        border_color="#020e05",
        border_width=1,
        corner_radius=5
    ).grid(row=0, column=0, sticky="w", padx=5, pady=5)


    label_titulo_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="EDITAR LIVRO",
        font=("Segoe UI Semibold",24),
        text_color="#163822"
    )
    label_titulo_edit.grid(row=0,column=0,columnspan=2,pady=10)

    label_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Selecione Livro",
        font=("Segoe UI Semibold",12),
        text_color="#000"
    )
    label_edit.grid(row=1,column=0,columnspan=2,pady=(0,0))

    combo_edit = ctk.CTkComboBox(
        frame_tela_edit_livros,
        values=buscar_livro(),
        width=250,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_edit.grid(row=2, column=0, columnspan=2,pady=(0,5))
    combo_edit.set("Selecione...")

    titulo_entry = ctk.CTkEntry(
        frame_tela_edit_livros,
        width=200,
        height=25
    )
    titulo_entry.grid(row=3,column=0)

#============FUNÇÔES TELA EDITAR LIVRO================

    def buscar_livro():
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("SELECT titulo FROM livros ORDER BY titulo ASC")
            resultado = cursor.fetchall()
            conn.close()
            lista_livros = [titulo[0] for titulo in resultado]
            return lista_livros
        except sqlite3.Error as erro:
            print(f"Erro ao buscar dados {erro}")
            return[]

    

#endregion





