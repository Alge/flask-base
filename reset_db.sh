rm -r migrations/
rm instance/dev.db

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

python manage.py seed


