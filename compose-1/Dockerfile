FROM ustclug/ubuntu:22.04

RUN apt update && apt install -y x11-apps mesa-utils \
    pipewire-audio-client-libraries alsa-utils pulseaudio-utils
COPY 99-pipewire-default.conf /etc/alsa/conf.d/99-pipewire-default.conf
COPY pulse-client.conf /etc/pulse/client.conf
