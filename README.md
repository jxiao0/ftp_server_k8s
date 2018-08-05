## FTP SERVER K8S

### Prerequsite

- kubectl
- docker

### Install
- build.sh will deploy into cloud repo using cloud build directly,
if you want to build on local machine you can use the following command
under project folder
```shell
docker build --rm -f docker\Dockerfile -t docker:latest docker
```

- `./k8s/deploy.sh`

### Feature
- One click FTP server for gcs bucket. 
Easy to change permission, change user, passwd and gcs bucket.

### Known issue
- Cannot list directory when the ftp_server scaled up. 
ClientIP sessionAffinity seems not working in this case.