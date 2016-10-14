cd /vagrant/flask_project/;
git pull;
sudo /etc/init.d/nginx restart;
cd /vagrant/flask_project/;
gunicorn app:app -b localhost:8000