import consul
import json
import pathlib
from dotenv import dotenv_values


# Constantes y variables configurables
CONFIG_DIR = pathlib.Path(__file__).parent.parent
CHAT_SERVICE_DIR = CONFIG_DIR / 'chat_service'
USER_SERVICE_DIR = CONFIG_DIR / 'user_service'
CONSUL_KEY_PREFIX = 'config'
ENV_VARIABLES = {
    'chatservice': {
        'ENV_FILE': CHAT_SERVICE_DIR / '.env',
        'KEYS': [
                    'SECRET_KEY', 
                    'NAME',
                    # 'DATABASE_NAME',
                    # 'DATABASE_USER',
                    # 'DATABASE_PASSWORD',
                    # 'DATABASE_HOST',
                    # 'DATABASE_PORT',
                    # 'REDIS_HOST',
                    # 'REDIS_PORT',
                    # 'STATIC_PATH',
                    # 'CHAT_URL',
                    # 'USER_URL',
                    'LOCAL_USER_URL',
                    # 'CONSUL_AGENT_ADDRESS',
                    # 'CONSUL_AGENT_PORT',
                    # 'CONSUL_CHECK_URL',
                    # 'CONSUL_CHECK_INTERVAL',
                    # 'CONSUL_SERVICE_NAME',
                    # 'CONSUL_SERVICE_ADDRESS',
                    # 'CONSUL_SERVICE_PORT',
                    ],
    },
    'userservice': {
        'ENV_FILE': USER_SERVICE_DIR / '.env',
        'KEYS': [
                    'SECRET_KEY', 
                    'NAME'
                    # Agregar las variables de entorno que se quieran registrar
                    ],
    },
}

# Conectar con el agente Consul
consul_client = consul.Consul()

# Recorrer los servicios y sus variables de entorno correspondientes
for service, service_config in ENV_VARIABLES.items():
    env_file = service_config['ENV_FILE']
    keys = service_config['KEYS']

    # Leer las variables de entorno del archivo .env
    env_vars = dotenv_values(env_file)

    # Construir el diccionario de configuración para el servicio
    config = {key: env_vars[key] for key in keys}

    # Convertir el diccionario a una cadena JSON
    config_json = json.dumps(config)

    # Clave en Consul donde se almacenará la configuración del servicio
    consul_key = f'{service}/{CONSUL_KEY_PREFIX}'

    # Guardar la configuración en Consul para el servicio correspondiente
    consul_client.kv.put(consul_key, config_json)
