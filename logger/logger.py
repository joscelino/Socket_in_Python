import logging

# Configs
log_format = '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s: %(message)s'

logging.basicConfig(filemode='a',
                    filename='logs\errors.log',
                    level=logging.DEBUG,
                    format=log_format
                    )

logger = logging.getLogger('root')
