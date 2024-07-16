Create virtual env
python -m venv devenv

Activate the Virtual Environment
devenv\Scripts\activate.bat

Create requirements.txt
pip freeze > requirements.txt

Install from requirements.txt
pip install -r requirements.txt

Deactivate a Virtual Environment
deactivate