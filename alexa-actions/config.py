# Built-In Imports
import os

# Local Imports
from const import (
    HA_URL,
    HA_TOKEN,
    SSL_VERIFY,
    DEBUG,
    AWS_DEFAULT_REGION,
)


configuration = {
    HA_URL: os.environ[HA_URL],
    HA_TOKEN: os.environ[HA_TOKEN],
    SSL_VERIFY: os.environ.get(SSL_VERIFY, default=False),
    DEBUG: os.environ.get(DEBUG, default=False),
    AWS_DEFAULT_REGION: os.environ.get(AWS_DEFAULT_REGION),
}
