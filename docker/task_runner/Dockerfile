FROM node:7.1.0
WORKDIR /app
ADD package.json /app/package.json
RUN npm install
ADD webpack.config.js /app/webpack.config.js
ADD start-watch.sh /app/start-watch.sh
