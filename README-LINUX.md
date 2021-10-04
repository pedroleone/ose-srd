# OSE SRD
Repositório dos dados do OSE SRD

## Rodando localmente no Linux

### 1. Instalar ferramentas
No `Debian 11` e nas distribuições nele baseadas:
```sh
sudo aptitude install npm nodejs
```
No `Debian 10` e anteriores, e nas distribuições nele baseadas, primeiro instale o `npm`:
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
Para outras distribuições consulte o site do desenvolvedor, as instruções são bem simples: [nodesource distributions](https://github.com/nodesource/distributions/blob/master/README.md).
### 2. Clonar o repositório
```sh
git clone https://github.com/pedroleone/osr-srd.git
```
### 3. Na pasta do projeto (osr-srd)
```sh
npm install
sudo npm install -g gatsby
```
### 4. Visualizar o site
Já está tudo instalado, agora pode rodar o site. Ainda na pasta do projeto (osr-srd), execute:
```sh
gatsby develop
```
Pode demorar um pouquinho (cerca de 1 minuto), mas quando aparecer uma mensagem parecida com essa:
```sh
success Building development bundle - 9.146s
```
Não feche o terminal. Abra o navegador e acesse a página: [http://localhost:8000](http://localhost:8000)
