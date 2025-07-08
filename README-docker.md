# OSE-SRD via Docker

Este documento explica como rodar o projeto OSE-SRD via Docker, tanto em modo de **produção** quanto de **desenvolvimento**, no Linux.

## 1. Instalar o Docker no Linux

### Debian, Ubuntu e derivados

Certifique-se de que esses pacotes estão instalados:

```sh
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release
```

Adiciona a chave GPG oficial do Docker:

```sh
sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/debian/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Adiciona o repositório oficial do Docker:

```sh
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```

Se o `lsb_release -cs` retornar algo como `trixie`, que ainda não está oficialmente suportado, substitua por `bookworm`:

```sh
sudo sed -i 's/trixie/bookworm/' /etc/apt/sources.list.d/docker.list
```

Atualiza os pacotes e instala o Docker:

```sh
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verifica se o serviço está rodando:

```sh
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
```

**(Opcional)** Para usar o Docker sem `sudo`:

```sh
sudo usermod -aG docker $USER
newgrp docker
```

Verifique se a instalação foi bem-sucedida:

```sh
docker --version
docker compose version
```

---

## 2. Clonar o repositório

```sh
git clone https://github.com/pedroleone/ose-srd.git
cd ose-srd
```

---

## 3. Rodar em modo de desenvolvimento

Esse modo recompila o site sempre que você salvar um arquivo. Ideal para editar e ver as mudanças ao vivo.

```sh
docker compose up dev
```

Depois de alguns segundos, acesse o site no navegador:

[http://localhost:8000](http://localhost:8000)

Para encerrar, use `Ctrl+C`. Se estiver usando um terminal que intercepta o `Ctrl+C` (como o Alacritty configurado para copiar com `Ctrl+C`), você pode parar o container com:

```sh
docker stop ose-dev
```

---

## 4. Rodar em modo de produção

Esse modo compila os arquivos estáticos e serve o site como será visto em produção.

### 4.1. Build (com cache)

```sh
docker compose up --build prod
```

Se tiver alterado a versão do Node ou feito mudanças estruturais, recomende-se limpar o cache:

```sh
docker compose build --no-cache prod
docker compose up prod
```

O site ficará disponível em:

[http://localhost:8080](http://localhost:8080)

### 4.2. Parar o container de produção

```sh
docker stop ose-prod
```

---

## Observações

- A imagem usada é baseada em `node:18-bullseye`, compatível com as exigências do Gatsby.
- O ambiente de produção usa `gatsby serve`, enquanto o ambiente de desenvolvimento usa `gatsby develop`.
- A variável `NODE_OPTIONS=--openssl-legacy-provider` já está configurada no `Dockerfile`, não precisa se preocupar com erros de crypto.
- Conselho: não apague o `package-lock.json`, nem tente recriá-lo. Você vai ter MUITOS problemas.