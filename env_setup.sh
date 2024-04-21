sudo apt install python3-venv
python3 -m venv venviron
source .venviron/bin/activate
sudo apt-get update && sudo apt-get upgrade
python -m pip install -r requirements.txt