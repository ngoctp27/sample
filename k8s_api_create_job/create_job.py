from kubernetes import client, config

import os
import base64
RANDOM_STRING=base64.urlsafe_b64encode(os.urandom(6)).decode()

NAMESPACE="test"
JOB_NAME=f"job-hello-world-{RANDOM_STRING.lower()}"

#use service account in pod: cluster
#use kubeconfig for testing local: local
SCRIPT_LOCATE="local"

def create_job_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="job-container",
        image="python:3.11-slim-bullseye",
        command=["python", "-c", "import time; time.sleep(3); print('Hello World', '--- FINISH JOB ---')"]
    )

    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "job-hello-world"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container])
    )

    # Create the specification of deployment
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=1
    )

    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=JOB_NAME),
        spec=spec
    )

    return job

def create_job(api_instance, job):
    api_response = api_instance.create_namespaced_job(
        body=job,
        namespace=NAMESPACE
    )
    print("Job created. status='%s'" % str(api_response.status))

def main():

    if (SCRIPT_LOCATE == 'cluster'):
        config.load_incluster_config()
    if (SCRIPT_LOCATE == 'local'):
        print("Use credential from KUBECONFIG")
        config.load_kube_config()

    batch_v1 = client.BatchV1Api()
    job = create_job_object()
    create_job(batch_v1, job)

if __name__ == '__main__':
    main()

