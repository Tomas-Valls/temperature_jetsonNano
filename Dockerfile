FROM arm32v7/python:3.6-buster
RUN pip3 install --upgrade pip
RUN mkdir /home/Sinanticam && mkdir /home/Sinanticam/sinanticam_cam
COPY . /home/Sinanticam/sinanticam_cam
WORKDIR /home/Sinanticam/sinanticam_cam
