import configparser

config = configparser.ConfigParser()
config.read('./settings.ini')

backend_port = config['BACKEND']['PORT']
backend_ip = config['BACKEND']['IP']
backend_api = config['BACKEND']['API']
api_token = config['TOKEN']['API_TOKEN']
admin_id = int(config['TOKEN']['ADMIN_ID'])
internal_backend = True if config['BACKEND']['INTERNAL_BACKEND'] == 'YES' else False
