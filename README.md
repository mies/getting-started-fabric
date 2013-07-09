getting-started-fabric
======================

Sample application for wercker and fabric-based deployment

Status on wercker:
[![Wercker
status](https://app.wercker.com/status/1fdd6d59d5347df9b0d596bfe608ca34/m)](https://app.wercker.com/project/bykey/1fdd6d59d5347df9b0d596bfe608ca34)

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
