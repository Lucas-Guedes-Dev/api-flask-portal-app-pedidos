from flask import Flask, request

app = Flask(__name__)

@app.route('/insert/produto', methods=['POST'])
def produto():
    print('ola')
    if request.method == 'POST':

        data = request.form
        print(data)
        return data

if __name__ == '__main__':
    app.run()