# Debian 12 (Bookworm) + nodejs 24
FROM node:24-bookworm

# Enable pnpm via corepack; the exact version is pinned by packageManager
# in package.json, so we just need to enable and prepare corepack.
RUN corepack enable && corepack prepare pnpm@10.32.1 --activate

# Create app directory
WORKDIR /app

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# Bundle app source
COPY . .

# Build static files
RUN pnpm run build

# serve on port 8080
CMD ["pnpm", "exec", "docusaurus", "serve", "--host", "0.0.0.0", "--port", "8080", "--dir", "build"]
