from flask import Blueprint, jsonify, render_template

kit_bp = Blueprint(
    "custom_kit",
    __name__,
    template_folder="templates"
)

@kit_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "Flask App"})

@kit_bp.route("/dashboard", methods=["GET"])
def system_dashboard():
    return render_template("kit/health.html")