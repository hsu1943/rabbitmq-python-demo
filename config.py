import dotenv

# Load the .env file
envs = dotenv.dotenv_values('.env')

RABBITMQ_HOST = envs.get('RABBITMQ_HOST')
RABBITMQ_PORT = envs.get('RABBITMQ_PORT')
RABBITMQ_USER = envs.get('RABBITMQ_USER')
RABBITMQ_PASSWORD = envs.get('RABBITMQ_PASSWORD')
RABBITMQ_VHOST = envs.get('RABBITMQ_VHOST')