from app import app, db

if __name__ == "__main__":
	# app.app_context().push()
	# db.create_all()
	# with app.app_context():
	# 	db.create_all()
	app.run(host='0.0.0.0')
