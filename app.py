from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html style='background-color: #f0f4f8; font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1 style='color: #2c3e50;'>Bem-vindo ao Flask no Docker!</h1>
        <p style='color: #34495e;'>Trabalho de RASI - IFSP Campos do Jordão</p>
        <a href='/sobre'>Sobre</a> | <a href='/contato'>Contato</a>
    </html>
    """

@app.route("/sobre")
def sobre():
    return """
    <html style='background-color: #e8f8f5; font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1 style='color: #16a085;'>Sobre o Projeto</h1>
        <p style='color: #2c3e50;'>Aplicações containerizadas utilizando Docker e Python Flask.</p>
        <a href='/'>Voltar</a>
    </html>
    """

@app.route("/contato")
def contato():
    return """
    <html style='background-color: #fef9e7; font-family: sans-serif; text-align: center; padding-top: 50px;'>
        <h1 style='color: #d35400;'>Página de Contato</h1>
        <p style='color: #2c3e50;'>Entre em contacto com os integrantes do grupo.</p>
        <a href='/'>Voltar</a>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
