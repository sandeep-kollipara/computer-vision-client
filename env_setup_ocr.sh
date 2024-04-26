sudo apt install python3-venv
python3 -m venv venviron
source .venviron/bin/activate
sudo apt-get update && sudo apt-get upgrade
sudo apt install tesseract-ocr
python -m pip install -r requirements_ocr.txt