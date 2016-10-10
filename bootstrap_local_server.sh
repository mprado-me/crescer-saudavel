sudo apt-get update;
sudo apt-get install -y python python-pip python-virtualenv;
pip install --upgrade pip;
cd /vagrant;
sudo virtualenv env;
source env/bin/activate;
sudo pip install Flask;

#to init local server: python /vagrant/flask_project/app.py local