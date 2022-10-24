from flask import Flask,jsonify, request

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

#definindo a rota
@app.route('/books', methods = ['GET'])
def get_books():
    """ returns all books """
    return jsonify(books)

@app.route('/books/<int:id>', methods = ['GET'])
# get books by id
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#run app
app.run(port=5000, host='localhost', debug=True)