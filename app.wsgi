import sys
import os

# Agregar el directorio src al path para poder importar el módulo curriculum
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar la aplicación Flask
from curriculum.run import app

if __name__ == "__main__":
    app.run(host='192.168.100.10', port=8000, debug=False)
