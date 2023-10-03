FROM python:3.10
WORKDIR /home/aiton/ai/streamlit
ADD ./myapp /home/aiton/ai/streamlit
RUN pip install --upgrade pip
RUN pip install -r /home/aiton/ai/streamlit/requirements.txt

EXPOSE 8052

CMD [ "streamlit", "RUN", "myapp.py" ]