FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

RUN apt-get update -y
RUN apt-get upgrade -y

# install python
RUN apt install software-properties-common -y

# python3 is installed, we want also the python command (for 3rd party tools that might assume python) which python3 
RUN apt install python-is-python3

# install pip
RUN apt-get -y install python3-pip
RUN pip3 install numpy pandas torch scipy python-dateutil==2.8.1 pytz==2021.1 hyperopt==0.2.5 certifi==2020.12.5 pyyaml==5.4.1 networkx==2.5.1 scikit-learn==0.24.2 scikit-learn==0.24.2 keras  six==1.15.0 theano==1.0.3 psutil==5.8.0 pympler==0.9 tensorflow tables scikit-optimize==0.8.1 python-telegram-bot==13.5 tqdm dill
#Installation 
WORKDIR "/root"