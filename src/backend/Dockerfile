FROM python:3.11.2-alpine3.17

WORKDIR /flask-app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

COPY . .

CMD [ "python", "app.py" ]