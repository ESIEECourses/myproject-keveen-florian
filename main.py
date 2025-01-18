from src.dashboard.app import app
from config import PORT
if __name__ == '__main__':
    app.run_server(debug=True, port=PORT)
