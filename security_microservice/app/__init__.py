from flask import Flask

from app.controllers.security_controller import security_bp

app = Flask(__name__)
app.register_blueprint(security_bp)
