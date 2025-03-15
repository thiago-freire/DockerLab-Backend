from flask import Flask
from src.routes.routes import register_routes
# from src.configs import configs_env
# from apifairy import APIFairy

app = Flask(__name__)
# app.config["SECRET_KEY"] = configs_env["secret_key"]

# fc.CORS(app)

register_routes(app)

# apifairy_config = {
#     "APIFAIRY_TITLE": "PIIR API",
#     "APIFAIRY_VERSION": "0.0.1",
#     "APIFAIRY_UI": "swagger_ui",
#     "APIFAIRY_UI_PATH": "/docs"
# }

# app.config.update(apifairy_config)

# apifairy = APIFairy(app)
