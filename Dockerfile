FROM ubuntu:latest
USER root
RUN apt-get update && apt-get install -y python3 
RUN apt-get install nano -y
RUN apt-get install pip -y

#WORKDIR /home
COPY . /home
WORKDIR /home
#ENTRYPOINT ["python3"]
#CMD ["hola.py"]
RUN pip install -r requirements.txt
##RUN uvicorn main:app --reload

