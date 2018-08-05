#!/usr/bin/env bash
kubectl apply -f ftp_server_k8s.yaml
kubectl apply -f ftp_loadbalancer.yaml