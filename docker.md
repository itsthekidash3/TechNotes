# Docker & Kubernetes (Quick Notes)

## Docker (containers)
- **Goal:** Package an app so it runs the same everywhere (solves *“works on my machine”*).
- A container includes:
  - App code
  - Required runtime (e.g., Python 3.11, Node 18)
  - Dependencies
  - Configuration
- Containers **share the host OS kernel** (lighter than full virtual machines).

## Key terms
- **Dockerfile:** Recipe/instructions to build an image.
- **Image:** Built package (template) created from a Dockerfile.
- **Container:** A running instance of an image.
- Images are built in **layers** (base OS layer → runtime/deps → app).

docker commands
docker pull 
docker build
docker run
docker compose up

## Common Dockerfile instructions
- `FROM` — base image to start from (pulled from a registry).
- `RUN` — run commands during build (install packages, setup).
- `ENV` — set environment variables.
- `CMD` — default command when the container starts.

## Kubernetes (coordination/orchestration)
- Docker packages apps, but running many containers needs coordination.
- Kubernetes:
  - Decides **how many** containers to run and **where** to run them.
  - Replaces failed containers automatically.
  - Manages/coordinates the whole deployment.

### Control plane (the “brains”)
- **API Server:** entry point for commands/requests.
- **Scheduler:** picks which node runs which workload.
- **Controller Manager:** keeps the desired state running (repairs/replaces).

### Worker nodes
- Machines/VMs that actually run containers (e.g., DB node, streaming node, etc.).

port binidng

docker container from docker hub
developing a js app, with mongo db using the image from dockerr hub
commit to git or other vc
triggers a continous integrration - jenkins
builds js apps and creates docker image



cretae a docker image out of that js artifact
poush to private docker repository
devserver pulls the images
