python -m venv venv
.\venv\Scripts\activate
pip install -Ur requirements.txt
uvicorn app:app --reload --port 8899