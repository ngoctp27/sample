# Create Batch/v1:Job by interactive API Kubernetes

### Prerequisite
  - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) binary
  - pip: kubernetes
  - kubeconfig credential file (if run on Local Machine)

#### RUN Script on Local MACHINE
- SCRIPT_LOCATE="**local**" | #*create_job.py Line 12*
```
export KUBECONFIG=~/Download/your_kubeconfig
python create_job.py
```

#### RUN Script in Pod Kubernetes
- Service Account for Pod have enough permission to create "Job Kubernetes" in correct namespace.

- SCRIPT_LOCATE="**cluster**" | #*create_job.py Line 12*

```
python create_job.py
```

#### Example
![Example](https://raw.githubusercontent.com/ngoctp27/sample/develop/k8s_api_create_job/images/k8sapi_create_job.gif)