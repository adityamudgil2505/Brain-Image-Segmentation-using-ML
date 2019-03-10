from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)

# for sqlite run these command on terminal
#
# python
# from flaskblog import db
# db.create_all()
# from flaskblog.models import User, Patient
# User.query.all()