echo Install packages
echo I am provisioning... >> /home/vagrant/test

# Install Nginx
echo Install nginx
sudo yum install -y epel-release
sudo cat <<EOT >> /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=https://nginx.org/packages/mainline/centos/7/\$basearch/
gpgcheck=0
enabled=1
EOT
yum update
sudo yum install -y nginx

sudo rm /etc/nginx/conf.d/default.conf

sudo cat <<EOT >> /etc/nginx/conf.d/assignment.local.conf
server {
  listen        80;
  server_name   0.0.0.0;

  location / {    
    root  /home/vagrant/;
	index result.json;
  }
}
EOT

sudo chmod 777 /home/vagrant/

# By default SELinux does not allow the web server to read files in users' home directories.
sudo setsebool -P httpd_read_user_content true

sudo systemctl restart nginx

# Install Git
echo Install git
sudo yum install -y git
sudo git clone https://github.com/efi1397/assignment1.git

# Install Python3
echo Install python3
sudo yum install -y python3
sudo pip3 install -r /home/vagrant/assignment1/requirements.txt
python3 /home/vagrant/assignment1/main.py

echo Done :)