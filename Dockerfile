FROM continuumio/anaconda3:latest

RUN mkdir /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python-pip
# COPY requirements.txt /app/
RUN conda config --append channels conda-forge
RUN conda install -c ibmdecisionoptimization cplex docplex --yes
COPY . /app/