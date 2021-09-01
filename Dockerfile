FROM node:latest as node
WORKDIR /build
COPY ./package*.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:latest
WORKDIR /app
COPY --from=build /build/dist .
COPY nginx.conf /etc/nginx/nginx.conf

