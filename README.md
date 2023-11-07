# Time Scaler Operator - Python

A simple Kubernetes operator made using `KOPF`.

This operator allows you to define a `TimeScale` custom resource that enables time-based scaling of your deployments.
```
apiVersion: "engineerkenji.com/v1"
kind: TimeScaler
metadata:
  name: timescaler-sample
spec:
  startTime: 5             // 05:00 AM UTC
  endTime: 10              // 10:00 AM UTC
  replicas: 2              // no. of replicas
  deployment:
    - name: mysql          // deployment name
      namespace: default   // deployment namespace
```
