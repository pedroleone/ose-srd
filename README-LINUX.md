# Rodando OSE SRD localmente no Linux

## 1. Instalar Node.js 24 (LTS)

O projeto usa Node.js `>=22` e é desenvolvido sob a versão LTS atual (24).
A forma mais confiável de instalar é via [nvm](https://github.com/nvm-sh/nvm)
— assim você não conflita com a versão do Node empacotada pela sua distro:

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# reabra o terminal ou rode: source ~/.bashrc (ou ~/.zshrc)
nvm install 24
nvm use 24
```

Alternativamente, em distros recentes como Debian 12 (Bookworm) e Ubuntu 24.04,
você pode usar o [nodesource](https://github.com/nodesource/distributions).

## 2. Habilitar pnpm via corepack

O projeto usa **pnpm** como gerenciador de pacotes (muito mais rápido que o
npm e com suporte nativo via corepack, que já vem com o Node 24):

```sh
corepack enable
```

A versão do pnpm é fixada pelo campo `packageManager` no `package.json`;
o corepack resolve automaticamente na primeira vez que você rodar `pnpm`.

## 3. Clonar o repositório

```sh
git clone https://github.com/pedroleone/ose-srd.git
cd ose-srd
```

## 4. Instalar dependências

```sh
pnpm install
```

## 5. Rodar o site em modo de desenvolvimento

```sh
pnpm start
```

Depois de alguns segundos o Docusaurus vai subir o dev server e mostrar
algo como:

```
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

Não feche o terminal. Abra o navegador em [http://localhost:3000](http://localhost:3000).
As mudanças nos arquivos em `content/` são refletidas automaticamente
via hot reload.
