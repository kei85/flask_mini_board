from flask_app import app, bp

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()