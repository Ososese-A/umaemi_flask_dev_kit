from flask import Flask, render_template_string
from flask_ui_kit import CustomKit

app = Flask(__name__)

app.config["KIT_API_KEY"] = "my-secret-token"
app.config["KIT_ENABLE_HEALTH_CHECK"] = True

kit = CustomKit(app=app)

@app.route("/")
def home():
    return render_template_string("""
<h1>Welcome to the Test App</h1>
<p>Formatted Price: {{ 4500.75 | currency_format }}</p>
<p><a href="/_kit/health">Check Extension Health Route</a></p>
""")

if __name__ == "__main__":
    app.run(debug=True, port=5000)