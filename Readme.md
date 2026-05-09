# Tower of Hanoi

Animated Tower of Hanoi using Python's `turtle` module.  

## Run with Docker

**Linux / macOS**
```bash
xhost +local:docker
docker build -t hanoi .
docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hanoi
```

**Windows (with VcXsrv or WSL2 + X server)**
```bash
docker build -t hanoi .
docker run --rm -e DISPLAY=host.docker.internal:0 hanoi
```

> No Python installation needed — Docker handles everything.

## Run without Docker

Requires Python 3 with Tk support.

```bash
python main.py
```
