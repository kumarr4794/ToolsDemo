{{- define "container1" -}}
- name: container1
  image: "{{ .Values.deployment.image.app }}:{{ .Values.deployment.image.version }}"
  imagePullPolicy: "{{ .Values.deployment.image.pullPolicy }}"
  ports:
    - name: http
      containerPort: 80
      protocol: TCP
{{- end -}}

{{- define "container2" -}}
- name: container2
  image: "{{ .Values.deployment.image.app }}:{{ .Values.deployment.image.version }}"
  imagePullPolicy: "{{ .Values.deployment.image.pullPolicy }}"
  ports:
    - name: http
      containerPort: 80
      protocol: TCP
{{- end -}}