import kopf
import kubernetes
import pytz
from datetime import datetime, time

# kubernetes.config.load_incluster_config()
kubernetes.config.load_kube_config()

def is_time_to_scale(spec):
    utc_now = datetime.now(pytz.utc).time()
    start_time = time(spec['startTime'])
    end_time = time(spec['endTime'])
    return start_time <= utc_now <= end_time

@kopf.on.create('engineerkenji.com', 'v1', 'timescalers')
@kopf.on.update('engineerkenji.com', 'v1', 'timescalers')
@kopf.on.resume('engineerkenji.com', 'v1', 'timescalers')
def create_fn(spec, **kwargs):
    if is_time_to_scale(spec):
        scale_deployments(spec)

def scale_deployments(spec):
    api_instance = kubernetes.client.AppsV1Api()
    for deployment in spec['deployment']:
        body = {
            "spec": {
                "replicas": spec['replicas']
            }
        }
        api_instance.patch_namespaced_deployment(
            name=deployment['name'],
            namespace=deployment['namespace'],
            body=body
        )