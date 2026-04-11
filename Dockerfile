# Debian 12 (Bookworm) + nodejs 24
FROM node:24-bookworm

# Create app directory
WORKDIR /app

COPY package*.json ./
RUN npm ci

# Bundle app source
COPY . .

# Build static files
RUN npm run build

# serve on port 8080
CMD ["npx", "docusaurus", "serve", "--host", "0.0.0.0", "--port", "8080", "--dir", "build"]
