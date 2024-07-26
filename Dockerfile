FROM python:3.7

RUN pip install --upgrade pip
RUN pip install tornado==4.2
RUN pip install numpy
RUN pip install scikit-learn==0.20.4
RUN pip install pandas
RUN pip install xgboost
RUN pip install uvicorn
RUN pip install fastapi
RUN pip install pydantic

# Expose the ports we're interested in
EXPOSE 8002


ADD source /generic-python/source
ADD application.py /generic-python/application.py

CMD ["python","/generic-python/application.py"]

