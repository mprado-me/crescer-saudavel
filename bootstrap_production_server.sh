sudo apt-get install -y python nginx gunicorn;
sudo /etc/init.d/nginx start;
sudo rm /etc/nginx/sites-enabled/default;
sudo rm /etc/nginx/sites-available/flask_project;
sudo rm /etc/nginx/sites-enabled/flask_project;
sudo cp /vagrant/ngix_config /etc/nginx/sites-available/flask_project;
sudo ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project;
sudo /etc/init.d/nginx restart;
cd /vagrant/flask_project/;

#to init production server: gunicorn app:app -b localhost:8000