sudo yum install epel-release
sudo yum -y update
sudo yum -y install python-pip
sudo yum install virtualenv
virtualenv venviron
source .venviron/bin/activate
python3 -m pip install -r requirements.txt