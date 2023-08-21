import configparser

config = configparser.ConfigParser()
config.read('./settings.ini')

backend_port = config['BACKEND'].get('PORT')
backend_ip = config['BACKEND'].get('IP')
backend_api = config['BACKEND'].get('API')
api_token = config['TOKEN'].get('API_TOKEN')
admin_id = int(config['TOKEN'].get('ADMIN_ID'))
internal_backend = True if config['BACKEND'].get('INTERNAL_BACKEND') == 'YES' else False
