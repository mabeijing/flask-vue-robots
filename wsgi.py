from flask_vue_robots import app

celery_app = app.extensions["celery"]

if __name__ == '__main__':
    app.run()
