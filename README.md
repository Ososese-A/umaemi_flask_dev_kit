PROJECT LAYOUT

flask-custom-kit/
├── src/
│   └── flask_custom_kit/
│       ├── __init__.py         # Main extension class
│       ├── blueprints.py       # Reusable routes/views
│       ├── templates/          # Pre-built Jinja2 templates
│       │   └── kit/
│       │       └── health.html
│       └── utils.py            # Decorators/helpers
├── tests/
│   └── app.py
├── pyproject.toml              # Build & dependency settings
└── README.md