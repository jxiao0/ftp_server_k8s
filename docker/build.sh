cp ../ftp_server.py ./
gcloud builds submit --tag gcr.io/${project_name}/ftp_server_k8s . #FIXME: PROJECTNAME HERE