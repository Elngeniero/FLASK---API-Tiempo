from flask import Flask
from main import main  # importa la app que creaste

app = Flask(__name__)

# Registrar la "aplicación" (Blueprint)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
