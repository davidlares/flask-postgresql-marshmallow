
from app import create_app
from config import config

# environment
environment = config['development']
# retrieve Flask instance
app = create_app(environment)

if __name__ == "__main__":
    # running flask instance
    app.run()
