FROM python:3.11-slim

# Install only what turtle needs: Tk + X11 libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk \
    tk \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY main.py .

CMD ["python", "main.py"]