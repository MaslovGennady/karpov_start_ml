python -m venv venv
.\venv\Scripts\activate
pip install -Ur requirements.txt
uvicorn app:app --reload --port 8899

http://127.0.0.1:8899/post/recommendations/?id=201&time=1&limit=1