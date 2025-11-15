from run import create_app

# Llama a la función de fábrica para obtener la aplicación
app = create_app() 

if __name__ == '__main__':
    app.run(debug=True, host='197.168.100.10', port=5000)