from flask import jsonify

import jwt
import datetime
from functools import wraps

# Secrets and key are managed externally, not in code.
JWT_SECRET = 'your_secret_key'
JWT_ALGORITHM = 'HS256'