## Integrantes do Grupo:

- Henrique Baptista - RM 97796
- Gabriel Amancio - RM 97936
- Pedro Pacheco - RM 98043
- Ricardo Brito - RM 98370

---

## Descrição do Projeto:

O nosso projeto visa criar um sistema de automação de seguro para bicicletas. Neste contexto, realizamos interações com APIs, especialmente para a verificação de imagens, e incluímos uma simulação de login e criação de usuários. Essa abordagem permite uma imersão e compreensão do funcionamento completo do aplicativo. Vale destacar que, no projeto final, as interações com Python concentram-se principalmente na integração com a inteligência artificial.

## Requisitos:

Para executar o projeto, siga as instruções abaixo para instalar as dependências.

### Pré-requisitos

- Python 3.x instalado
- Ambiente virtual (opcional, mas recomendado)

### Instalação

1. Clone o repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   ```

2. Navegue até o diretório do projeto:

   ```
   cd nome-projeto
   ```

3. (Opcional) Crie e ative um ambiente virtual:

   ```
   python -m venv venv
   No Windows: venv\Scripts\activate
   No Linux/Mac: source venv/bin/activate
   ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt

   ```

5. Execute o projeto:

   ```
   python main.py
   ou
   uvicorn main:app --reload

   ```

## Estrutura do Projeto:

Este projeto está organizado de acordo com a seguinte estrutura de diretórios:

-**app**: Contém o código principal da aplicação.

-`main.py`: Ponto de entrada do aplicativo.

-`ia_preditc.py`: Módulo para interação com a IA e predição de imagens.

-**database**: Contém os módulos relacionados ao banco de dados.

-`crud.py`: Operações CRUD para interação com o banco de dados.

-`models.py`: Define os modelos de dados usados no projeto.

-**schemas**: Define os esquemas de dados utilizados nas requisições e respostas da API.

-`user.py`: Esquemas relacionados aos usuários.

-`bike.py`: Esquemas relacionados às bicicletas.

-`image_prediction.py`: Esquemas relacionados às predições de imagens.

-**docs**: Documentação do projeto.

-`README.md`: Arquivo principal de documentação.

-`requirements.txt`: Lista de dependências do projeto.

-**`received_images`**: Diretório para armazenar imagens recebidas pelo sistema.

- **venv**: Ambiente virtual (criado apenas se você optar por usá-lo).

# Uso:

### Como Usar o Projeto

Este projeto é uma aplicação FastAPI que fornece um serviço de automação de seguro para bicicletas, incluindo integração com uma API de predição de imagens.

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Recomenda-se o uso de um ambiente virtual.

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-projeto.git
   cd nome-do-projeto
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Executando a Aplicação

1. Inicie a aplicação:

   ```bash
   uvicorn main:app --reload
   ```

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para obter detalhes sobre as rotas disponíveis.

### Exemplo de Interatividade com a API

### 1. Criação de um Novo Usuário

Faça uma requisição POST para `/users` com os dados do novo usuário:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "João",
  "email": "joao@example.com",
  "password": "senha123"
}'
```

# Contribuição:

## Contribuindo para o Projeto

Agradecemos por considerar contribuir para este projeto! Siga as diretrizes abaixo para garantir uma colaboração suave.

## Solicitações de Pull (Pull Requests)

1. Antes de enviar uma solicitação de pull, certifique-se de ter a versão mais recente do código.
2. Crie um fork do repositório e faça as alterações no seu fork.
3. Mantenha cada solicitação de pull focada em uma única melhoria ou correção.
4. Descreva claramente as alterações na sua solicitação de pull e forneça contextos relevantes.
5. Adicione testes, se aplicável, para garantir a estabilidade do código.
6. Certifique-se de que o código siga os padrões de codificação do projeto.
7. Evite fazer alterações desnecessárias ou relacionadas a problemas existentes sem uma boa razão.
8. Esteja disposto a discutir e ajustar as mudanças propostas conforme necessário.

## Issues

Antes de criar uma nova issue, verifique se a mesma ainda não foi relatada. Se for uma nova funcionalidade, discuta-a primeiro em uma issue antes de implementar.

Agradecemos pela sua contribuição!

---

## Bugs Conhecidos:

Ao usar este projeto, tenha em mente os seguintes problemas conhecidos:

1.**Erro de Decodificação de Caracteres Especiais em Nomes de Arquivos:** -**Descrição:** O sistema pode apresentar problemas ao lidar com nomes de arquivos que contenham caracteres especiais. -**Solução Alternativa:** Evite usar caracteres especiais nos nomes de arquivos.

2.**Resposta Inconsistente da API em Condições de Rede Instáveis:** -**Descrição:** Em condições de rede instáveis, a API pode fornecer respostas inconsistentes. -**Solução Alternativa:** Tente novamente em uma conexão de rede mais estável.

3.**Problemas de Desempenho em Dispositivos com Recursos Limitados:** -**Descrição:** Dispositivos com recursos limitados podem enfrentar lentidão ou falhas devido a requisitos de desempenho do projeto. -**Solução Alternativa:** Execute o projeto em um dispositivo com recursos mais adequados.

## Contato:

Se você tiver alguma dúvida, sugestão ou problema relacionado a este projeto, sinta-se à vontade para entrar em contato com os desenvolvedores/mantenedores:

- Henrique Baptista

  - Email: [henriquebaptista2003@gmail.com]
  - GitHub: [https://github.com/henriquebap]

- Agradecemos seu interesse e contribuições!

---

# Agradecimentos e Referências:

### Gostaríamos de expressar nossa gratidão às seguintes pessoas e projetos que foram fontes de inspiração ou forneceram suporte ao desenvolvimento deste projeto:

- Aos nossos professores e colegas de equipe, que contribuíram com ideias valiosas e ofereceram suporte durante o desenvolvimento.
- À comunidade de código aberto e todos os desenvolvedores que compartilham conhecimento online.
- À equipe do Roboflow, cuja biblioteca foi fundamental para a integração de recursos de visão computacional em nosso projeto.

Agradecemos a todos que contribuíram direta ou indiretamente para o sucesso deste projeto!
