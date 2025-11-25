# SRE Final Project: FastAPI Calculator with Kubernetes, Observability & Alerts

## Overview
This project delivers a complete Site Reliability Engineering (SRE) stack built around a containerized **FastAPI-based calculator application** deployed on **Kubernetes (Minikube)**.  
It includes **monitoring, dashboards, alerting, and Slack notifications**, following production-inspired SRE practices.

This repository contains:

- FastAPI application with interactive calculator UI  
- Docker image packaging  
- Kubernetes manifests (app, service, monitoring stack)  
- Prometheus scraping configuration  
- Grafana dashboards  
- Alerting rules integrated with Slack  
- Basic automation using Ansible for stack deployment  

---

## Project Architecture

### Components
- **FastAPI Calculator App** – containerized and deployed via Kubernetes Deployment + Service  
- **Prometheus** – scrapes metrics from FastAPI  
- **Grafana** – dashboards + alert evaluation  
- **Slack Alerts** – firing alerts sent directly to a Slack channel  
- **Ansible** – automates manifest application to Minikube  

---

## 1. FastAPI Application

Provides:
- Calculator UI  
- FastAPI backend  
- `/metrics` endpoint for Prometheus  

Run locally:
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 2. Docker Image

Build:
```
docker build -t alejoro21/sre-calculator:1.0 .
```

Push:
```
docker push alejoro21/sre-calculator:1.0
```

---

## 3. Kubernetes Deployment

Apply:
```
kubectl apply -f k8s/app.yaml
kubectl apply -f k8s/prometheus.yaml
kubectl apply -f k8s/grafana.yaml
```

Open app:
```
minikube service fastapi-service -n monitoring --url
```

---

## 4. Prometheus

Scrapes FastAPI metrics through a scrape job defined in:

```
k8s/prometheus.yaml
```

---

## 5. Grafana

Dashboards reflect:
- Latency  
- Request count  
- Errors  
- Availability  

---

## 6. Alerts (Slack)

Prometheus metrics → Grafana alerting → Slack via webhook.

---

## 7. Ansible Automation

Run:
```
ansible-playbook -i ansible/inventory.ini ansible/deploy_stack.yaml
```

---

## Repository Structure
```
app/
k8s/
ansible/
README.md
```
