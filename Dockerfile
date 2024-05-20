FROM python:3.11
WORKDIR /app
COPY ./ /app
RUN pip install -r requriments.txt
Expose 8501
ENTRYPOINT [ "streamlit","Run" ]
CMD [ "customer_comments" ]