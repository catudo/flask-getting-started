from flask import Flask
from controllers.example_view import ExampleView

app = Flask(__name__)

ExampleView.register(app)


if __name__ == '__main__':
    app.run()