import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Banco de dados
con = sqlite3.connect("pacientes.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    peso REAL,
    altura REAL,
    imc REAL
)""")
con.commit()

# Função IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Funções do sistema
def cadastrar():
    nome = simpledialog.askstring("Cadastro", "Nome do paciente:")
    idade = simpledialog.askinteger("Cadastro", "Idade:")
    peso = simpledialog.askfloat("Cadastro", "Peso (kg):")
    altura = simpledialog.askfloat("Cadastro", "Altura (m):")

    if nome and idade and peso and altura:
        imc = calcular_imc(peso, altura)
        cur.execute("INSERT INTO pacientes (nome, idade, peso, altura, imc) VALUES (?, ?, ?, ?, ?)",
                    (nome, idade, peso, altura, imc))
        con.commit()
        listar()
        messagebox.showinfo("Sucesso", f"{nome} cadastrado!\nIMC = {imc:.2f}")

def listar():
    for row in tree.get_children():
        tree.delete(row)
    cur.execute("SELECT * FROM pacientes")
    for r in cur.fetchall():
        tree.insert("", "end", values=r)

def editar():
    sel = tree.focus()
    if not sel:
        messagebox.showwarning("Atenção", "Selecione um paciente.")
        return
    item = tree.item(sel)["values"]
    novo_peso = simpledialog.askfloat("Editar", "Novo peso (kg):", initialvalue=item[3])
    nova_altura = simpledialog.askfloat("Editar", "Nova altura (m):", initialvalue=item[4])
    if novo_peso and nova_altura:
        imc = calcular_imc(novo_peso, nova_altura)
        cur.execute("UPDATE pacientes SET peso=?, altura=?, imc=? WHERE id=?",
                    (novo_peso, nova_altura, imc, item[0]))
        con.commit()
        listar()
        messagebox.showinfo("Sucesso", "Dados atualizados!")

def excluir():
    sel = tree.focus()
    if not sel:
        messagebox.showwarning("Atenção", "Selecione um paciente.")
        return
    item = tree.item(sel)["values"]
    cur.execute("DELETE FROM pacientes WHERE id=?", (item[0],))
    con.commit()
    listar()
    messagebox.showinfo("Sucesso", f"Paciente {item[1]} removido!")

# ---------------- INTERFACE ----------------
janela = tk.Tk()
janela.title("Sistema de Pacientes - IMC")
janela.geometry("650x400")
janela.configure(bg="#f0f4f7")

# Estilo ttk
style = ttk.Style(janela)
style.theme_use("clam")
style.configure("Treeview", font=("Arial", 11), rowheight=28, background="white", fieldbackground="white")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3f72af", foreground="white")
style.map("Treeview", background=[("selected", "#112d4e")], foreground=[("selected", "white")])

# Cria botões coloridos com comandos para cada função
frame = tk.Frame(janela, bg="#f0f4f7")
frame.pack(pady=10)

btn1 = tk.Button(frame, text="Cadastrar", command=cadastrar, width=12, bg="#3f72af", fg="white", font=("Arial", 10, "bold"))
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(frame, text="Listar", command=listar, width=12, bg="#3f72af", fg="white", font=("Arial", 10, "bold"))
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(frame, text="Editar", command=editar, width=12, bg="#3f72af", fg="white", font=("Arial", 10, "bold"))
btn3.grid(row=0, column=2, padx=5)

btn4 = tk.Button(frame, text="Excluir", command=excluir, width=12, bg="#d9534f", fg="white", font=("Arial", 10, "bold"))
btn4.grid(row=0, column=3, padx=5)

# Cria tabela com colunas: ID, Nome, Idade, Peso, Altura e IMC.
cols = ("ID", "Nome", "Idade", "Peso", "Altura", "IMC")
tree = ttk.Treeview(janela, columns=cols, show="headings", height=10)

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(pady=10, fill="x", padx=15)

listar()

janela.mainloop()




