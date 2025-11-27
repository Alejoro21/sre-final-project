# Contributing Guidelines

Thank you for your interest in contributing to this SRE Final Project repository.

This project was originally created as part of an SRE Academy final assignment.  
Contributions are welcome for learning, experimentation and improvement.

## How to Contribute

1. **Fork the repository** on GitHub.
2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-change-name
   ```
3. **Make your changes** to code, manifests, automation or documentation.
4. **Test locally**:
   - Ensure the FastAPI app still builds and runs in Docker.
   - Ensure Kubernetes manifests still apply cleanly to Minikube.
   - Verify that Prometheus and Grafana start without errors.
5. **Commit with a clear message**:
   ```bash
   git commit -m "Describe your change briefly"
   ```
6. **Push your branch**:
   ```bash
   git push origin feature/your-change-name
   ```
7. **Open a Pull Request** on GitHub describing:
   - What changed
   - Why it is useful
   - Any special deployment or testing notes

## Coding & Configuration Style

- Prefer clear, explicit configuration over “magic”.
- Keep Kubernetes manifests readable and small when possible.
- Use meaningful resource names and labels.
- Keep documentation in English.

## Scope of Changes

Examples of valuable contributions include:

- Improving or extending observability (dashboards, alerts, metrics).
- Adding or refining automation (Ansible, scripts, workflows).
- Enhancing README or evidence documentation.
- Adding safe examples related to optional academy topics
  (e.g., tracing, logging, GitOps, Terraform), as long as they remain optional.

## Reporting Issues

If you spot a problem (bug, typo, broken command):

1. Open a GitHub Issue.
2. Include:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (OS, Minikube, Docker, etc.)

## Code of Conduct

Please be respectful, constructive, and collaborative.  
This repository is primarily educational and should remain a safe and positive space for learning about SRE and observability practices.
