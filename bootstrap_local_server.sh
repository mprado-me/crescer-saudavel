sudo apt-get update;
sudo apt-get install -y python python-pip python-virtualenv;
pip install --upgrade pip;
cd /vagrant;
sudo virtualenv env --always-copy;
source env/bin/activate;
pip install Flask;
pip install Flask-WTF;

# if use sudo in pip install ... the package will not be installed in the env folder
#to init local server: python /vagrant/flask_project/app.py local