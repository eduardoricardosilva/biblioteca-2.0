import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

#region config_tela
#def montar_tela_login(janela_login, validar_e_entrar):
    # Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Janela
janela_login = ctk.CTk()
janela_login.geometry("400x450")
janela_login.title("Login de Usúario")


janela_login.grid_columnconfigure(0, weight=1)
janela_login.grid_rowconfigure(0, weight=1)

frame_login = ctk.CTkFrame(
    janela_login,
    width=350,
    height=400,
    fg_color="#5eb373",
    border_color="#65dd36",
    border_width=1.5,
    corner_radius=10)

frame_login.grid(row=0, column=0, padx=30, pady=30)
frame_login.grid_propagate(False)
frame_login.grid_columnconfigure(0, weight=1)

#endregion

#region frame_titulo
frame_titulo = ctk.CTkFrame(
    frame_login,
    fg_color="transparent")
frame_titulo.grid(
    row=0,column=0,pady=(20,10))

linha_esq = ctk.CTkFrame(
    frame_titulo,
    width=60,
    height=2,
    fg_color="#2E8B57")
linha_esq.grid(row=0, column=0, padx=10)

titulo_login = ctk.CTkLabel(
    frame_titulo,
    text="LOGIN", 
    font=("Segoe UI", 40,"bold"),
    text_color="#d6f8d1"
)
titulo_login.grid(row=0,column=1)

linha_dir = ctk.CTkFrame(
    frame_titulo,
    width=60,
    height=2,
    fg_color="#2E8B57")
linha_dir.grid(row=0, column=2,padx=10)
#endregion

#region frame_usuario

frame_usuario = ctk.CTkFrame(
    frame_login,
    fg_color="transparent"
)
frame_usuario.grid(row=1,column=0,pady=(40,10))

icone_user = ctk.CTkLabel(
    frame_usuario,
    text="👤",
    font=("Segoe UI Emoji", 20),
    text_color="black",
    padx=5
)
icone_user.grid(row=0, column=0)
user_entry = ctk.CTkEntry(
    frame_usuario,
    width=220,
    text_color="#000000",
    placeholder_text="Usuário",
    height=30,
    border_width=1,
    fg_color="#c4e7bd",
    border_color="black"
)
user_entry.grid(row=0,column=1)


#endregion

#region frame_senha


frame_senha = ctk.CTkFrame(
    frame_login,
    fg_color="transparent")
frame_senha.grid(row=2, column=0,pady=(10,30))

icone_senha = ctk.CTkLabel(
    frame_senha,
    text="🔒",
    font=("Segoe UI Emoji", 20),
    text_color="#000000",
    padx=5)
icone_senha.grid(row=1,column=0)
senha_entry = ctk.CTkEntry(
    frame_senha,
    width=220,
    show="*",
    text_color="#000000",
    placeholder_text="Senha",
    height=30,
    border_width=1,
    fg_color="#c4e7bd",
    border_color="black",
)
senha_entry.grid(row=1, column=1)

frame_icone = ctk.CTkFrame(
    frame_senha,
    fg_color="#c4e7bd")
frame_icone.grid(row=1, column=1,pady=5,padx=(175,0))

senha_visivel = False

def mostrar_senha():
    global senha_visivel

    if senha_visivel:
        senha_entry.configure(show="*")
        botao_olho.configure(text="👁")
        senha_visivel = False
    else:
        senha_entry.configure(show="")
        botao_olho.configure(text="🙈")
        senha_visivel = True

botao_olho = ctk.CTkButton(
    frame_icone,
    font=("Segoe UI Emoji", 17),
    text="👁",
    width=25,
    height=25,
    fg_color="#c4e7bd",
    hover_color="#c4e7bd",
    text_color="black",
    border_width=0,
    command=mostrar_senha
)
botao_olho.grid(row=0, column=0)
#endregion

#region frame_btn

frame_btn = ctk.CTkFrame(
    frame_login,
    fg_color="transparent")
frame_btn.grid(row=3, column=0,pady=15)

btn_login = ctk.CTkButton(
    frame_btn,
    width=150,
    fg_color="#083609",
    height=40,
    text="🔑 ENTRAR",
    font=("Segoe UI", 12, "bold"),
    corner_radius=25,
    border_width=1,
    border_color="#102517"
    )
btn_login.grid(row=0, column=0)

#endregion


def validar_senha(senha):

    if len(senha) < 8:
        return "A senha precisa ter no mínimo 8 caracteres"

    elif not any(c.islower() for c in senha):
        return "A senha precisa ter letra minúscula"

    elif not any(c.isupper() for c in senha):
        return "A senha precisa ter letra maiúscula"

    elif not any(c.isdigit() for c in senha):
        return "A senha precisa ter número"

    elif not any(c in "@#$%&*!?" for c in senha):
        return "A senha precisa ter caractere especial"

    return True







janela_login.mainloop()
