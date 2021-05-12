import sys
import logging

ENV = sys.argv[1] if len(sys.argv) >= 2 else 'pro'

PORT = 5000

log_config = {
    'debug': dict(
        format="%(asctime)s %(levelname)s \"%(pathname)s\", line %(lineno)d, %(message)s",
        level=logging.INFO,
    ),
    'pro': dict(
        format="%(asctime)s %(levelname)s \"%(pathname)s\", line %(lineno)d, %(message)s",
        level=logging.WARNING,
        filename='server.log'
    )
}

logging.basicConfig(
    **log_config[ENV]
)

