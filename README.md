# SRE Final Project – FastAPI Calculator with Kubernetes Monitoring

## Project Overview
This project implements a complete, production‑like **SRE monitoring pipeline** around a containerized **FastAPI Calculator** application deployed on **Kubernetes (Minikube)**.  
The stack includes:

- **FastAPI** application (containerized with Docker)
- **Kubernetes Deployment + Service**
- **Prometheus** (metrics collection)
- **Grafana** (dashboards + alerts)
- **Slack alert notifications**
- **Ansible** (automation of deployment steps)

This project demonstrates practical observability and reliability engineering skills learned throughout the academy training.

---

## Architecture Diagram
```
User → FastAPI Service → Kubernetes → Prometheus → Grafana → Slack Alerts
```

---

## 1. FastAPI Application
A simple but interactive calculator with input fields and HTML UI.

### Files:
- `app/main.py`
- `app/requirements.txt`
- `Dockerfile`

### Build & Push:
```bash
docker build -t alejoro21/sre-calculator:1.0 .
docker push alejoro21/sre-calculator:1.0
```

---

## 2. Kubernetes Deployment
The app is deployed inside Minikube using:

- `k8s/deployment.yaml`
- `k8s/service.yaml`

### Apply:
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Access app:
```bash
minikube service fastapi-service -n monitoring --url
```

---

## 3. Prometheus Integration
The Prometheus ConfigMap was updated to scrape FastAPI as a target.

### Key Fragment:
```yaml
scrape_configs:
  - job_name: 'fastapi-calculator'
    static_configs:
      - targets: ['fastapi-service.monitoring.svc.cluster.local:80']
```

### Commands:
```bash
kubectl apply -f prometheus/prometheus.yaml
minikube service prometheus-service -n monitoring
```

---

## 4. Grafana Dashboards
Grafana reads FastAPI metrics from Prometheus.

- Dashboard built manually in UI
- Includes:
  - Request count
  - Latency
  - Error rate
  - CPU/memory from cAdvisor

Access:
```bash
minikube service grafana-service -n monitoring
```

---

## 5. Alerting (Slack Notifications)
A Slack Incoming Webhook was configured.

### Alert Rule (Grafana):
- Fires when FastAPI reports errors
- Sends webhook messages like:

```
FastAPI Calculator Error Rate High
```

---

## 6. Automation with Ansible
Ansible playbook `ansible/deploy.yaml` automates:

- Applying Kubernetes manifests  
- Ensuring Minikube is running  
- Deploying monitoring stack

### Run:
```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy.yaml
```

---

## Project Structure
```
sre-final-project/
│
├── app/
│   ├── main.py
│   └── requirements.txt
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── prometheus.yaml
│
├── grafana/
│   └── datasources.yaml
│
├── ansible/
│   ├── inventory.ini
│   └── deploy.yaml
│
└── README.md  ← this file
```

---

## Future Improvements
These items were part of optional academy topics and can be added later:

- OpenTelemetry tracing → Jaeger  
- cAdvisor dashboards with span metrics  
- Loki logging pipeline  
- Terraform IaC  
- GitOps with ArgoCD  
- Chaos engineering with Litmus  

---

## How to Run Everything (Summary)

### Start Minikube:
```bash
minikube start --driver=docker
```

### Deploy everything:
```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy.yaml
```

### Access:
- FastAPI: `minikube service fastapi-service -n monitoring`
- Prometheus: `minikube service prometheus-service -n monitoring`
- Grafana: `minikube service grafana-service -n monitoring`

---

## Author
**Luis Mejia (Alejoro21)**  
SRE Academy Final Project

