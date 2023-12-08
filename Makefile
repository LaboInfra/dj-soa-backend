migra:
	poetry run python manage.py makemigrations account
	poetry run python manage.py migrate

deldb:
	rm db.sqlite3