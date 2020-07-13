from app_factory import create_app
from models import db

# Create the project using a factory to be able to run tests
# with a custom config app (as a test db)
app, _ = create_app("app.cfg")
with app.app_context():
    db.create_all()
