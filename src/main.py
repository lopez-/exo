from config import Config
from api import Api

if __name__ == "__main__":
    config = Config().load_config()
    api = Api()

    for table in config['tables']:
        api.get_table(table['name'])