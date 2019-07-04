from flask import Flask, render_template
app = Flask(__name__)

users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
    for value in some_list:
        for key in value:
            print(f'{key} - {value[key]}', end = ", ")
        print()
iterateDictionary(users)


@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug = True)