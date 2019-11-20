#importar Biblioteca
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Base_Dados

#Criar Janela

jan = Tk ()

jan.title("Primeiro programa") # nome do programa
jan.geometry("600x300") # tamanho da tela undidade em pixels
jan.configure(background="white") # Cor de fundo do programa
jan.resizable(width=False, height=False) # Restrição de configuração da tela (maximizar)
jan.attributes("-alpha",0.9) # Deixar o plano de fundo transparente
jan.iconbitmap(default="icons/LogoIcon.ico") # Incluir Icone na Janela

LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") # Dividindo a lado esquerdo da tela
LeftFrame.pack(side=LEFT) # O detalhe azul da tela ficará do lado esquerdo

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") # Dividindo a lado direito da tela
RightFrame.pack(side=RIGHT)

# Incluir imagem na Janela

logo = PhotoImage(file="icons/logo.png") # Incuindo a foto para inserir no programa
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE") # Definir plano de fundo da image
LogoLabel.place(x=50, y= 100) # Onde a image será plotada

# Incluir Rotulos na Janela


UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White" )
PassLabel.place(x=5, y=150)

# Caixa de entrada de Dados


UserEntry = ttk.Entry(RightFrame, width= 37)
UserEntry.place(x=155, y=115)
PassEntry = ttk.Entry(RightFrame, width=37, show="*")
PassEntry.place(x=155, y =163)

#Funções remover os botões da primeira tela

def Register(): # Esta função e do primeiro botão
    LoginButton.place(x=5000) # Este comando tira o botão Login da visão do usuário
    RegisterButton.place(x=5000) # Este comando tira o botão Resister da visão do usuário

# Rotulos dos dados cadastrais

    NameLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
    NameLabel.place(x=5, y=10)
    EmailLabel = Label(RightFrame, text="E-mail:", font=("Century Gothic", 20),bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

# Dados de entrada

    NameEntry = ttk.Entry(RightFrame, width= 37)
    NameEntry.place(x=155, y=23)
    EmailEntry = ttk.Entry(RightFrame, width= 37)
    EmailEntry.place (x=155, y=68)

#Função Para Conectar ao Banco de Dados

    def RegisterToDataBase ():
        Name = NameEntry.get() # pegar as informações de entrada de cada termo
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

# verificação se todos os dados estão preenchidos
        if (Name == "" and Email == "" and User == "" and Pass ==""):
            messagebox.showerror(title="Register Erro", message="Preencha todos os campos")
        else:
            Base_Dados.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES (?, ?, ?, ?)
            """,(Name, Email, User, Pass)) # retira os dados da aplicação e leva para base de dados
            Base_Dados.conn.commit() # salva os dados na base SQL
            messagebox.showinfo(title="Regist Inf", message="Conta Criada com Sucesso!")


# Botão de registrar o novo Cadastro

    Register = ttk.Button (RightFrame, text="Register", width=20 , command=RegisterToDataBase) # Botão da segunda Tela
    Register.place(x=10, y=250)

# Função do botão Back (Voltar)
    def BackToLogin():
       NameLabel.place(x=5000)    # escondendo os dados do cadastro
       EmailLabel.place(x=5000)
       NameEntry.place(x=5000)
       EmailEntry.place (x=5000)
       Register.place(x=5000)
       Back.place(x=5000)
       LoginButton.place(x=10, y=250) # retornando o botão da tela inicial
       RegisterButton.place(x=253, y=250) #retornando o botão da tela inicial



# Botão Back (voltar)
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin) # Botão da segunda Tela voltar para login
    Back.place(x=253, y=250)

# verificação do cadastro

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
        
    Base_Dados.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """,(User, Pass))

    print('Selecionou')

    VerifyLogin = Base_Dados.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso negado!")

    
# Botões de acionamento da primeira tela Login

LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=10, y=250)
RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register) # Botão da primeira Tela
RegisterButton.place(x=253, y=250)









jan.mainloop()
