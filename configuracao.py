import logging
from logging.config import dictConfig

loggerConfig = {
  "version": 1,
  "disabled_existing_loggers": False,
  "formatters": {
    "default": {
      "format": "%(asctime)s %(levelname)s %(message)s",
      "datefmt": "%Y-%m-%d %H:%M:%S"
		}
	},
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "default"
		},
    "file": {
			"level": "INFO",
			"class": "logging.FileHandler",
			"filename": "logs/log.log",
      "formatter": "default"
		}
	},
  "loggers": {
    "default": {
      "handlers": ["console", "file"],
      "level": "INFO",
      "propagate": False
		}
	}
}

dictConfig(loggerConfig)