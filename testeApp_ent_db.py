import tkinter as tk

def register():
    # Função para processar o registro
    username = username_entry.get()
    password = password_entry.get()
    confirmsenha = confirm_password_entry.get()
    
    if password == confirmsenha:
        print("Usuário registrado com sucesso!")
    else:
        print("As senhas não conhecidem")
    # Fechar a janela de cadastro após o registro
    register_window.destroy()

def open_register():
    # Função para abrir a tela de cadastro
    global register_window
    register_window = tk.Toplevel(root)
    register_window.title("Cadastro")

    # Campos de entrada para nome de usuário e senha
    username_label = tk.Label(register_window, text="Nome de Usuário:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    password_label = tk.Label(register_window, text="Senha:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack(pady=5)
    
    confirm_password_label = tk.Label(register_window, text="Confirmar Senha:")
    confirm_password_label.pack(pady=5)
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.pack(pady=5)

    # Botão para registrar
    register_button = tk.Button(register_window, text="Registrar", command=register)
    register_button.pack(pady=10)

def open_login():
    # Função para abrir a tela de login
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    # Adicione widgets para o login aqui

# Cria a janela principal
root = tk.Tk()
root.title("Meu Aplicativo")

# Botões para cadastro e login
register_button = tk.Button(root, text="Cadastrar", command=open_register)
register_button.pack(pady=10)

login_button = tk.Button(root, text="Login", command=open_login)
login_button.pack(pady=10)

# Loop principal para manter a janela aberta
root.mainloop()