from flask import Flask, current_app, request, abort
from .blueprints import kit_bp

class CustomKit:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        """
        """
        app.config.setdefault("KIT_API_KEY", None)
        app.config.setdefault("KIT_ENABLE_HEALTH_CHECK", True)

        if app.config["KIT_ENABLE_HEALTH_CHECK"]:
            app.register_blueprint(kit_bp, url_prefix="/_kit")

        @app.template_filter("currency_format")
        def currency_format(value):
            return f"${value:,.2f}"

        @app.before_request
        def verify_kit_key():
            if request.path.startswith("/_kit/protected"):
                api_key = request.headers.get("X-Kit-Key")
                if api_key != current_app.config["KIT_API_KEY"]:
                    abort(401, description="Invalid Kit API Key")

        app.extensions["custom_kit"] = self