FROM ustclug/debian:bookworm

# Install deps
RUN apt update && apt install -y --no-install-recommends \
    wget ca-certificates

# Download latest hmcl
RUN wget -O /hmcl.jar https://github.com/huanghongxun/HMCL/releases/download/release-3.5.5/HMCL-3.5.5.jar

# Install openjdk-17 and x-related packages
RUN apt install -y --no-install-recommends \
    openjdk-17-jre \
    libxext6 libxrender1 libxtst6 libxi6 \
    adduser \
    pipewire pipewire-alsa alsa-utils \
    && rm -rf /var/lib/apt/lists/*

# Create user
RUN adduser --disabled-password --gecos "" --uid 1000 hmcl
USER 1000:1000
WORKDIR /home/hmcl

CMD ["java", "-jar", "/hmcl.jar"]
# CMD ["tail", "-f", "/dev/null"]
