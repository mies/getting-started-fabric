getting-started-fabric
======================

Sample application for wercker and fabric-based deployment

# create virtualenv
virtualenv venv --distribute

# activate virtualenv
sourc venv/bin/activate

# install dependencies
pip install flask
pip install fabric
pip install gunicorn
pip install wercker

# freeze requirements
pip freeze > requirements.txt

# create wercker.yml
...

# add to git
git init
git add .
git commit -am 'initial commit'

# add to wercker
wercker create

# create app
app.py

# create gunicorn config

# create fabfile

# update wercker.yml
