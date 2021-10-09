{{- define "container" -}}
- name: nginx
  image: "{{ .Values.deployment.image.app }}:{{ .Values.deployment.image.version }}"
  imagePullPolicy: "{{ .Values.deployment.image.pullPolicy }}"
  ports:
    - name: http
      containerPort: 80
      protocol: TCP
{{- end -}}