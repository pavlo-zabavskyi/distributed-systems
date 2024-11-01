import uvicorn
from src.api import app


def main():
    uvicorn.run(app, host='0.0.0.0', port=8051)


if __name__ == '__main__':
    main()
