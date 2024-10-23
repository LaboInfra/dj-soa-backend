migra:
	poetry run python manage.py makemigrations account
	poetry run python manage.py migrate

admin:
	poetry run python manage.py shell -c "from account.models import User; User.objects.create_superuser('admin@laboinfra.net', 'admin')"

serv:
	poetry run python manage.py runserver

reset:
	rm -f db.sqlite3
	make migra
	make admin

init:
	poetry install
	make migra
	make admin
