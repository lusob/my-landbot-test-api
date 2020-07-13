FROM python:3
ADD . /
EXPOSE 5000
RUN pip install -r requirements.txt
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]
