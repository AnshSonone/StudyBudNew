FROM python:3.12.1-slim

# install needed packages

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . .

CMD [ "python", "manage.py" , "runserver" ,"0.0.0.0:8000"]
