import consul
import json
from dotenv import dotenv_values

# Constantes y variables configurables
CONSUL_KEY_PREFIX = 'config'
ENV_VARIABLES = {
    'user_service': {
        'ENV_FILE': './consul/.env',
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
                    'LOCAL_CHAT_URL',
                    # 'CONSUL_AGENT_ADDRESS',
                    # 'CONSUL_AGENT_PORT',
                    # 'CONSUL_CHECK_URL',
                    # 'CONSUL_CHECK_INTERVAL',
                    # 'CONSUL_SERVICE_NAME',
                    # 'CONSUL_SERVICE_ADDRESS',
                    # 'CONSUL_SERVICE_PORT',
                    ],
    },
}

# Conectar con el agente Consul
consul_client = consul.Consul(host='consul', port=8500)

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
