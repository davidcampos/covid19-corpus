#!/bin/bash
docker run -d -p 8010:8010 -m 8G --log-driver=none neji-server:latest
