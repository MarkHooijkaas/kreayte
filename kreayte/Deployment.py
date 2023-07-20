from jinja2 import Template

template="""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{APP}}
spec:
  replicas: {{APP_REPLICAS}}
  revisionHistoryLimit: 1
  selector:
    matchLabels:
      app: {{APP}}
  template:
    metadata:
      name: {{APP}}
      labels:
        TODO: custom labels
      annotations:
        app.kubernetes.io/name: {{APP}}
        app.kubernetes.io/version: "{{APP_VERSION}}"
        app.kubernetes.io/component: webservice
        app.kubernetes.io/part-of: {{APP_PROJECT}}
        app.kubernetes.io/managed-by: kreayte
        co.elastic.logs/enabled: "true"
        co.elastic.logs/exclude_lines: DEBUG
        TODO: custom annontations
    spec:
      #restartPolicy: Never
      containers:
      - name: {{CONTAINER_NAME}}
        image: {{APP_IMAGE_NAME}}:{{APP_VERSION}}
        imagePullPolicy: Always
        envFrom:
        - secretRef:
            name: {{SECRETS_NAME}}
        - configMapRef:
            name: {{APP}}-vars
        ports:
        - containerPort: 8080
          protocol: TCP
        resources:
          limits:
            cpu: {{APP_CPU_LIMIT}}
            memory: {{APP_MEMORY_LIMIT}}
          requests:
            cpu: {{APP_CPU_REQUEST}}
            memory: {{APP_MEMORY_REQUEST}}
      serviceAccountName: {{SERVICEACCOUNT_NAME}}  # TODO: optional
      terminationGracePeriodSeconds: {{TERMINATION_GRACE_PERIOD}} # TODO: optional
"""

def kreayte(data):
  j2_template = Template(template)
  print(j2_template.render(data))
