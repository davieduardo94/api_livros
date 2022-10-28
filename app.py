import os
from flask import Flask,jsonify, render_template, request

# criando o aplicativo Flask
app = Flask(__name__)

#fonte de dados
books = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# definindo o index
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

#pagina endpoints
@app.route('/endpoints', methods = ['GET'])
def endpoints():
    return render_template('endpoints.html')
    

#definindo a rota
@app.route('/books', methods = ['GET'])
def get_books():
    """ returns all books """
    return jsonify(books)

@app.route('/books/<int:id>', methods = ['GET'])
# get book by id
def get_book_by_id(id):
    """ get book by id"""
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

@app.route('/books/<int:id>', methods = ['PUT'])
def update_book_by_id(id):
    """ updates book by id """
    # requisicao enviada pelo usuario para API
    book_updated = request.get_json()
    for index, book in enumerate(books):
        # verificando se o id é igual ao livro atual
        if book.get('id') == id:
            # atualizando o dicionario com base no index
            books[index] = book_updated
            # retornando o livro atualizado na lista
            return jsonify(books[index])
        
@app.route('/books', methods = ['POST'])
def create_book():
    """ inserts book in list """
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>', methods = ['DELETE'])
def delete_book(id):
    # verificando a posicao e o livro
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

#implemented for heroku
def main():
    port = int(os.environ.get('PORT', 5000))
    #run app
    app.run(port=port, host='0.0.0.0', debug=True)

if __name__ == '__main__':
    main()