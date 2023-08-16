# build_files.sh
pip install -r requirements.txt

# make migrations
python3.9 manage.py migrate --noinput
python3.9 manage.py collectstatic --noinput

python3.9 manage.py runserver