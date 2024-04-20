# computer-vision-client
[ Phase II: Consumer] This repository holds the code developed in partial fulfilment of online credit course "CS370 - OS" offered at Colorado State University Online for Spring 2024.

## Preface
This ReadMe file will highlight the objectives with precedence, setup instructions for first-time user and finally the step-by-step development progress for reference (also reflected in the commits).

## Objectives
The computer-vision-client is the consumer/slave/client of the Producer-Consumer Architectural Pattern on which this project is designed on. Following are it's objectives/features in order of import:

[1] Receive the RTSP/UDP stream over the network/internet and display to user via GUI (security concerns withstanding).

[2] The program should be docker-compatible (platform-agnostic) and any desktop with a monitor should be able to run and view it.

[3] Apply OpenCV algoritms on the input and detect objects as close to real-time as possible (by utilizing multiprocessing if available).

### Autorun:

```autorun 
./autorun.sh
```

### To setup the environment manually:

```setup 
./env-setup.sh
```
