from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Utilisez le port 5001 ou tout autre port libre