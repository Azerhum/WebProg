FROM python:3.12

RUN mkdir app
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 5000

# ENTRYPOINT [ "python" ]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]