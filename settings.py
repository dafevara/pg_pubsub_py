import os
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default_handler': {
            'class': 'logging.FileHandler',
            'level': os.getenv('LOG_LEVEL'),
            'formatter': 'standard',
            'filename': os.path.join('log', 'app.log'),
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {
            'handlers': ['default_handler'],
            'level': os.getenv('LOG_LEVEL'),
            'propagate': False
        }
    }
}
