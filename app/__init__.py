from flask import Flask, jsonify, request


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # Load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    from app import routes
    routes.register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)