FROM python:3.9
COPY user.py /app/user.py
COPY menu.py /app/menu.py
COPY option.py /app/option.py
COPY bike.py /app/bike.py
COPY launch.json /app.launch.json
RUN pip install -r requirements.txt
