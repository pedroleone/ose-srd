# Rodando OSE SRD localmente no Linux

## 1. Instalar ferramentas

### Debian 11 (Bullseye) e distros derivadas

```sh
sudo aptitude install npm nodejs
```

### Debian 10 (Buster) e distros derivadas

Primeiro instale o `npm`:

```sh
sudo aptitude install npm
```

Depois instale o `nodejs`, mas não use os repositórios, porque o Debian 10 "Buster" está defasado (versão 10.xx), você vai precisar da versão mais atual (versão 12.xx ou superior).

```sh
# No Ubuntu:
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

# No Debian, como root:
curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
apt-get install -y nodejs
```

### Debian 12 (Bookworm) e distros derivadas

Instale:

```sh
sudo apt update
sudo apt install -y nodejs npm
```

O Debian 12 já vem com Node.js 18, mas para garantir que o Gatsby rode sem problemas com o OpenSSL 3, você deve configurar a variável de ambiente `NODE_OPTIONS` para o fallback legado do OpenSSL.

Sempre que for executar o passo 4, a seguir, você DEVE configurar a variável de ambiente para evitar erro de crypto (ou pode deixá-la no seu `.bashrc`). Você vai digitar essa linha no terminal:

```sh
export NODE_OPTIONS=--openssl-legacy-provider
```

E, sem fechar o terminal, execute o passo 4.

### Outras distros

Para outras distribuições consulte o site do desenvolvedor, as instruções são bem simples: [nodesource distributions](https://github.com/nodesource/distributions/blob/master/README.md).

## 2. Clonar o repositório

```sh
git clone https://github.com/pedroleone/ose-srd.git
```

## 3. Na pasta do projeto (osr-srd)

```sh
npm install
sudo npm install -g gatsby
```

## 4. Visualizar o site

Já está tudo instalado, agora pode rodar o site. Ainda na pasta do projeto (ose-srd), execute:

```sh
gatsby develop
```

Pode demorar um pouquinho (cerca de 1 minuto), mas quando aparecer uma mensagem parecida com essa:

```sh
success Building development bundle - 9.146s
```

Não feche o terminal. Abra o navegador e acesse a página: [http://localhost:8000](http://localhost:8000)
