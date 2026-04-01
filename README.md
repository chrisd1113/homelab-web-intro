# Homelab DevOps Project

A simple multi-VM web service built with Python Flask, demonstrating basic DevOps practices on Linux.

## Overview

This project consists of a **backend API** running on RHEL and a **frontend API** running on Ubuntu. The frontend fetches data from the backend to simulate a client-server architecture.

## Architecture

- **RHEL VM**: Hosts the Backend service
- **Ubuntu VM**: Hosts the Frontend service
- **GitHub**: Version control and source of truth

### Components

**Backend (RHEL)**
- Flask application (`backend/backend.py`)
- Exposes `/data` endpoint
- Returns JSON with status and timestamp
- Managed as a systemd service (`backend.service`)

**Frontend (Ubuntu)**
- Flask application (`frontend/app.py`)
- Calls the RHEL backend using HTTP
- Uses environment variable for backend location (kept private via `.env`)

## Technologies Used

- Python + Flask
- systemd (service management)
- Linux (RHEL & Ubuntu)
- Git & GitHub
- Virtual Environment (venv)

## Project Structure

<img width="996" height="1035" alt="image" src="https://github.com/user-attachments/assets/b6fa57e4-886c-4de7-ad2c-414a49ab30a5" />
