from flask import Flask, render_template

app = Flask(__name__) # por padrão do flask tenho que passar essa variável nesse formato. na documentação do flask explica melhor a respeito

# criar a 1ª página do site

# route -> É o caminho depois do domínio, mostra qual link vai abrir tal página
@app.route("/") # onde app é o nome que dei para o programa acima e route para definir o link da pagina e ("/") é a minha HOME
# função ->É o que quer exibir na página
def homepage(): # criando a função HOMEPAGE, esse nome poderia ser qualquer outro nome, vc escolhe
    return render_template("homepage.html")
# template

@app.route("/contatos")
def contatos(): # não tem a necessidade de ser o mesmo nome
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")  # esse <> vai fazer com que ele seja dinâmico
def usuarios(nome_usuario): # vou definir a função usuário e vou passar ele como parâmetro
    # como vou tenho uma variável, preciso chamar ela na sequencia dessa forma: nome_usuario=nome_usuario
    return render_template("usuarios.html", nome_usuario=nome_usuario)


# colocar o site no ar
if __name__ == "__main__":  # vai executar o codigo abaixo quando estiver rodando esse codigo diretamente, é importante ter essa linha para não dar erro
    app.run(debug=True)  # vamos ativar o debugar do site, todas edições automaticamente serão ajustadas
