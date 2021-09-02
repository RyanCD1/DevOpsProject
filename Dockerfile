FROM node:10-alpine as build
WORKDIR /build
COPY . .
FROM nginx:latest
WORKDIR /app
COPY nginx/nginx.conf /etc/nginx/nginx.conf

