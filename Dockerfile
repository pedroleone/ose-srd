# Debian 12 (Bookworm) + nodejs 18
FROM node:18-bookworm

# Create app directory
WORKDIR /app

# Install app dependencies
# RUN npm -g install serve
RUN npm -g install gatsby-cli

COPY package*.json ./
RUN npm ci

# Bundle app source
COPY . .

# O Node.js >= 17 mudou o backend de criptografia para usar OpenSSL 3.0 por
# padrão. Isso quebra o Webpack 4 (e algumas versões do 5) que usam
# createHash('md4'), algoritmo não mais suportado por padrão.
# Solução clássica (sem downgrade): Forçar o uso do modo legacy de OpenSSL na
# variável de ambiente NODE_OPTIONS:
ENV NODE_OPTIONS=--openssl-legacy-provider

# Build static files
RUN npm run build

# serve on port 8080
# CMD ["serve", "-l", "tcp://0.0.0.0:8080", "public"]
CMD ["gatsby", "serve", "--prefix-paths", "--host", "0.0.0.0", "-p", "8080"]
