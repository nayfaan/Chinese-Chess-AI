cd "$(dirname "$0")"

source venv/bin/activate
python3 -m pip install -r requirements.txt

python3 main.py
