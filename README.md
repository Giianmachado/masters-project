# Object Detection by Relevance in Convolutional Neural Networks
Write here your project description.

# Docker Commands

## Test Docker version
Run `docker --version` and ensure that you have a supported version of Docker:
```
$ docker --version

Docker version 17.12.0-ce, build c97c6d6
```
Run `docker info` or (`docker version` without `--`) to view even more details about your docker installation:
```
$ docker info

Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
Images: 0
Server Version: 17.12.0-ce
Storage Driver: overlay2
...
```

## Purging All Unused or Dangling Images, Containers, Volumes, and Networks
Clear all images from Docker.
```
$ docker system prune -a
```

## Running Tensorflow Image
Pull Tensorflow image.
```
$ docker pull tensorflow/tensorflow
```
And run the image from local folder.
```
$ sudo docker run -it -v "$(pwd)":/home/gianluca/Desktop -p 8888:8888 -e PASSWORD=gianlucay12 tensorflow/tensorflow /bin/bash
```