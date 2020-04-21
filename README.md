# OSE SRD

Repositório dos dados do OSE SRD

## Rodando localmente

1. Instalar [NodeJS](https://nodejs.org/en/)
2. (Recomendado) Instalar [Github Desktop](https://desktop.github.com/)
3. (Recomendado) Instalar [Visual Studio Code](https://code.visualstudio.com/)
4. (Recomendado) Instalar [Git for Windows](https://git-scm.com/downloads)
5. Reiniciar a máquina após instalar todos os aplicativos
6. **Clonar o repositório**

Para isso, abra o Github Desktop.

Vá até o menu File -> New, e escolha Clone Repository

![Clone Repository...](https://i.imgur.com/NJc4mTk.png)

Na janela que irá se abrir, você precisa preencher dois campos:
* Repository URL: o endereço do repositório que você está clonando. No caso deste repositório é **pedroleone/osr-srd**
* Local path: onde vai ficar os arquivos que você vai copiar para a sua máquina. Escolha um diretório vazio.

![Dados](https://i.imgur.com/q9dTwOE.png)

Após a cópia dos arquivos, a tela do Github vai ficar assim:

![Tela](https://i.imgur.com/lH6Meif.png)

7. **Rodar localmente o site**

Na mesma tela anterior, clique em "Show in Explorer", ou abra manualmente a pasta que você copiou os arquivos.

No Explorer, clique com o botão direito em um espaço vazio e escolha "Git Bash here"

![Tela](https://i.imgur.com/T2iW1xs.png)

Irá abrir uma tela de comando como a abaixo:

![Tela](https://i.imgur.com/Px10lIE.png)

Digite "npm install" (sem as aspas), pressione enter e aguarde terminar a instalação. Este processo é demorado e pode levar um tempo até aparecer alguma coisa na tela. Isso é normal.

![Tela](https://i.imgur.com/pwEEYAg.png)

Depois que finalizar, digite "gatsby develop" (sem as aspas) e pressione enter.

![Tela](https://i.imgur.com/dQrBkwN.png)

Aguarde alguns minutos e se der tudo certo, irá exibir a seguinte mensagem:

![Tela](https://i.imgur.com/Ig4XiWj.png)

Agora você pode abrir a página no [http://localhost:8000](http://localhost:8000) para visualizar o site:

![Tela](https://i.imgur.com/xZ2Au6e.png)

8. **Editar os arquivos**

Para isso sugiro utilizar o Visual Studio Code.

No diretório que você copiou o site, clique com botão direito num espaço vazio e escolha Open With Code
![Tela](https://i.imgur.com/Q14S88S.png)

Os arquivos com o texto ficam na pasta "content":

![Tela](https://i.imgur.com/jxR5nkq.png)

Você pode editar o arquivo, e quando salvar o site será automaticamente atualizado:

![Tela](https://i.imgur.com/mDmyt2T.png)

Para editar uma dica é no Visual Studio Code, apertar a combinação "Ctrl+K" e depois "V". Isso irá abrir uma visualização do markdown ao lado:

![Tela](https://i.imgur.com/RNI8mAA.png)


