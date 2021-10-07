FROM python:3.8
MAINTAINER Pantelis Karatzas <pantelispanka@gmail.com>

RUN pip install --upgrade pip
RUN pip install tornado==4.2
RUN pip install numpy
RUN pip install pandas
RUN pip install xgboost==1.3.3
RUN pip install scikit-learn==0.20.0
# Expose the ports we're interested in
EXPOSE 8002


ADD source /generic-python/source
ADD application.py /generic-python/application.py



CMD ["python","/generic-python/application.py"]

