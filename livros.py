import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
import sqlite3

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


def buscar_livro():
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, titulo FROM livros ORDER BY id ASC")
            resultado = cursor.fetchall()
            conn.close()
            lista_livros = [f"{livro[0]} - {livro[1]}" for livro in resultado]
            return lista_livros
        except sqlite3.Error as erro:
            print(f"Erro ao buscar dados {erro}")
            return[]


def buscar_dados_livro(id_livro):
        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("SELECT livros.titulo, livros.editora, livros.quantidade,livros.isbn, generos.nome, autores.nome FROM livros LEFT JOIN generos ON livros.genero_id = generos.id LEFT JOIN autores ON livros.autor_id = autores.id WHERE livros.id = ?", (id_livro,))
            resultado_busca = cursor.fetchone()
            conn.close()
            return resultado_busca

        except sqlite3.Error as erro:
            print(f"Erro ao buscar livro: {erro}")
            return None


def preencher_campos(
        livro_selecionado,
        titulo_entry,
        editora_entry,
        quant_entry,
        isbn_entry,
        combo_edit_genero,
        combo_edit_autor
    ):

        livro_id = livro_selecionado.split(" - ")[0]
        dados = buscar_dados_livro(livro_id)

        if not dados:
            return

        titulo = dados[0]
        editora = dados[1]
        quantidade = dados[2]
        isbn = dados[3]
        genero = dados[4]
        autor = dados[5]

        titulo_entry.delete(0, "end")
        editora_entry.delete(0, "end")
        quant_entry.delete(0, "end")
        isbn_entry.delete(0, "end")

        titulo_entry.insert(0, titulo)
        editora_entry.insert(0, editora)
        quant_entry.insert(0, quantidade)
        isbn_entry.insert(0, isbn)

        combo_edit_genero.set(genero)
        combo_edit_autor.set(autor)


#region BOTÕES DA TELA GERENCIAMENTOS de LIVROS

    #region config_tela_livros

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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

    #region titulo da tela


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

    #region 1- btn_cad_livros

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

    #region 2- btn_edit_livro

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
        command=lambda: montar_tela_excluir_livro(janela_livros,montar_tela_livros,funcao_voltar),
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

#region 1- do botão de cadastro de livros

    #region config tela cadatrar livro

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
    
    #endregion

    #region btn voltar

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

    #endregion

    #region das funções cadastro de livros

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

    #endregion

    #region titulo da tela

    titulo = ctk.CTkLabel(
        frame_tela_cad_livros,
        text="CADASTRAR LIVRO",
        font=("Segoe UI Semibold",24),
        text_color="#163822"
    )
    titulo.grid(row=0,column=0,columnspan=2,pady=20)

    #endregion

    #region Cad titulo do livro

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

    #endregion

    #region Cad editora do livro

    lista_generos = carregar_generos()
    lista_autores = carregar_autores()

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

    #endregion

    #region Cad quantidade de livro

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

    #endregion

    #region isbn do livro

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

    #endregion

    #region Cad genero do livro

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

    #endregion

    #region Cad autor do livro

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

    #endregion

    #region Btn Salvar livro

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

#endregion

#region 2- do botão de editar livro

    #region config tela editar livro

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

    #endregion

    #region funções tela editar livro

    def atualizar_livro():

        livro_selecionado = combo_edit.get()
        livro_id = livro_selecionado.split(" - ")[0]
        titulo = titulo_entry.get()
        editora = editora_entry.get()
        quantidade = quant_entry.get()
        isbn = isbn_entry.get()
        genero = combo_edit_genero.get()
        autor = combo_edit_autor.get()


        if titulo == "":
            CTkMessagebox(
                title="Aviso",
                message="Titulo não pode ficar em branco",
                icon="warning")
            return

        elif editora == "":
            CTkMessagebox(
                title="Aviso",
                message="Editora não pode ficar em branco",
                icon="warning")
            return

        elif quantidade == "":
            CTkMessagebox(
                title="Aviso",
                message="Quantidade não pode ficar em branco",
                icon="warning")
            return

        elif isbn == "":
            CTkMessagebox(
                title="Aviso",
                message="ISBN não pode ficar em branco",
                icon="warning")
            return

        conn = sqlite3.connect("banco.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM generos WHERE nome = ?",(genero,)
        )
        resultado_genero = cursor.fetchone()
        genero_id = resultado_genero[0]

        cursor.execute(
            "SELECT id FROM autores WHERE nome = ?", (autor,)
        )
        resultado_autor = cursor.fetchone()
        autor_id = resultado_autor[0]

        cursor.execute("""
            UPDATE livros 
            SET titulo = ?,
                editora = ?,
                quantidade = ?,
                isbn = ?,
                genero_id = ?,
                autor_id = ?
            WHERE id = ?""",(
                titulo,
                editora,
                quantidade,
                isbn,
                genero_id,
                autor_id,
                livro_id
            ))

        conn.commit()
        conn.close()

        CTkMessagebox(
            title="Sucesso",
            message="Livro atualizado com sucesso!",
            icon="check")

    #endregion

    #region titulo

    label_titulo_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="EDITAR LIVRO",
        font=("Segoe UI Semibold",24),
        text_color="#163822"
    )
    label_titulo_edit.grid(row=0,column=0,columnspan=2,pady=10)

    #endregion

    #region para selecionar o livro para editar

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
        command=lambda livro_selecionado: preencher_campos(
        livro_selecionado,
        titulo_entry,
        editora_entry,
        quant_entry,
        isbn_entry,
        combo_edit_genero,
        combo_edit_autor),
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

    #endregion

    #region dados dos livros para editar

    titulo_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Título",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    titulo_edit.grid(row=3,column=0,sticky="w",padx=(80,0),pady=(10,0))

    titulo_entry = ctk.CTkEntry(
        frame_tela_edit_livros,
        width=175,
        height=20,
        text_color="#000",
        fg_color="#fff",
        font=("Segoe UI Semibold", 11),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    titulo_entry.grid(row=4,column=0,sticky="w", pady=0,padx=20)

    editora_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Editora",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    editora_edit.grid(row=3,column=1,sticky="e", padx=(0,80),pady=(10,0))

    editora_entry = ctk.CTkEntry(
        frame_tela_edit_livros,
        width=175,
        height=20,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 11),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    editora_entry.grid(row=4,column=1,sticky="e", pady=0,padx=20)

    quant_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Quantidade",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    quant_edit.grid(row=5,column=0,sticky="w",padx=(70,0),pady=(10,0))

    quant_entry = ctk.CTkEntry(
        frame_tela_edit_livros,
        width=175,
        height=20,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold",11),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    quant_entry.grid(row=6, column=0, sticky="w",padx=20,pady=0)

    isbn_edit = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="ISBN",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    isbn_edit.grid(row=5,column=1,sticky="e", padx=(0,90),pady=(10,0))

    isbn_entry = ctk.CTkEntry(
        frame_tela_edit_livros,
        width=175,
        height=20,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 11),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    isbn_entry.grid(row=6,column=1,sticky="e", pady=0,padx=20)

    label_edit_genero = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Gênero",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    label_edit_genero.grid(row=7,column=0,sticky="w",padx=(80,0),pady=(10,0))

    lista_generos = carregar_generos()
    lista_autores = carregar_autores()

    combo_edit_genero = ctk.CTkComboBox(
        frame_tela_edit_livros,
        values=lista_generos,
        width=200,
        height=20,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_edit_genero.grid(row=8, column=0,sticky="w",padx=20,pady=0)

    label_edit_autor = ctk.CTkLabel(
        frame_tela_edit_livros,
        text="Autor",
        font=("Segoe UI Semibold", 11),
        text_color="#000"
    )
    label_edit_autor.grid(row=7,column=1,sticky="e", padx=(0,90),pady=(10,0))

    combo_edit_autor = ctk.CTkComboBox(
        frame_tela_edit_livros,
        values=lista_autores,
        width=200,
        height=20,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_edit_autor.grid(row=8,column=1,sticky="e", pady=0,padx=20)

    #endregion

    #region btn salvar livro editado

    btn_salvar_livro_editado = ctk.CTkButton(
        frame_tela_edit_livros,
        text="Salvar Alterações",
        command=atualizar_livro,
        font=("Segoe UI Semibold", 15),
        fg_color="#429259",
        width=130,
        height=30
    )
    btn_salvar_livro_editado.grid(row=9, column=0, columnspan=2,pady=40)

#endregion

#endregion

#region 3- do excluir livro

    #region config tela excluir livro
def montar_tela_excluir_livro(janela_delete_livros, voltar_livros, voltar_menu,):

    

    for widget in janela_delete_livros.winfo_children():
        widget.destroy()

    janela_delete_livros.geometry("500x550")
    janela_delete_livros.configure(fg_color="#dff3df")
    janela_delete_livros.grid_columnconfigure(0, weight=1)
    janela_delete_livros.grid_rowconfigure(0, weight=1)
    janela_delete_livros.title("Excluir Livro")

    frame_tela_delete_livros = ctk.CTkFrame(
        janela_delete_livros,
        width=400,
        height=450,
        fg_color="#cae9ca"
    )
    frame_tela_delete_livros.grid(row=1,column=0, padx=20, pady=25)
    frame_tela_delete_livros.grid_propagate(False)
    frame_tela_delete_livros.grid_columnconfigure(0,weight=1)
    frame_tela_delete_livros.grid_columnconfigure(1, weight=1)
    

    ctk.CTkButton(
        janela_delete_livros,
        text="← Voltar ao menu anterior",
        command=lambda: voltar_livros(janela_delete_livros,voltar_menu),
        font=("Segoe UI Semibold", 12),
        text_color="#1E4D2B",
        hover_color="#8abb8c",
        width=150,
        fg_color="#adc2ae",
        border_color="#020e05",
        border_width=1,
        corner_radius=5
    ).grid(row=0, column=0, sticky="w", padx=5, pady=5)

    #endregion

    #region titulo

    label_delete_livro = ctk.CTkLabel(
        frame_tela_delete_livros,
        text="EXCLUIR LIVRO",
        font=("Segoe UI Semibold",24),
        text_color="#163822"
        )
    label_delete_livro.grid(row=0,column=0,columnspan=2,pady=10)

    #endregion

    #region para selecionar o livro para excluir

    combo_delete_livro = ctk.CTkComboBox(
        frame_tela_delete_livros,
        values=buscar_livro(),
        command=preencher_campos,
        width=250,
        height=25,
        fg_color="#fff",
        text_color="#000",
        font=("Segoe UI Semibold", 12),
        border_color="#7dbb8a",
        border_width=1,
        corner_radius=4
    )
    combo_delete_livro.grid(row=1, column=0,columnspan=2,pady=50)


    #endregion


#endregion


