# Aula Framework Flask e REST API

## Bootcamp Desenvolvedor Full Stack Python

### Etapas:

- [x] O que é uma API?
- [x] O que é REST?
- [x] O que é um REST API?
- [x] Métodos do protocolo HTTP
- [x] XML e JSON
- [x] URL, URN e URI
- [x] Framework Flask

---------------------------------------------------------

#### O que é uma API?

- É um conjunto de rotinas para acesso a um aplicativo / software / plataforma, baseado na web;

- Acrônimo de *Application Programming Interface*;

- API's são importantes quando existe a intenção de realizar integrações com outros serviços;

- A comunicação de software fica "transparente" ao usuário;

- API's podem ser locais, tanto baseados na web quanto em programas.

--------------------------------------------------

#### O que é REST?

- É um modelo a ser utilizado para projetar arquiteturas de software, baseado em comunicação via rede;

- Acrônimo de *Representational State Transfer*;

- Considera que todo recurso deveria responder aos mesmos métodos.

------------------------------------------------------------

#### O que é REST API?

- É uma API desenvolvida utilizando os princípios da arquitetura REST;

- É utilizado na comunicação / integração entre softwares através de serviços web;

- É consumido através de requisições HTTP;

- Geralmente são representadas em seus formatos JSON e XML. Também são usadas páginas HTML, PDF's e arquivos de imagem;

- Ao implementar, cada método deve ser responsável por um tipo diferente de ação. Exemplo: Consulta, Alteração, Inclusão e Exclusão.

--------------------------------------------------------------

#### Métodos do protocolo HTTP

- GET: Método que solicita algum recurso ou objeto do servidor por meio da URI;

- POST: Método usado para envio de arquivo / dados ou formulário HTML para o servidor;

- PUT: Aceitar, criar ou modificar um objeto do servidor;

- DELETE: Informa por meio da URI o objeto a ser deletado.

*no total são 9.

-----------------------------------------------------------------

#### URL, URN e URI?

- URL: Uniform Resource Locator. Host que será acessado. Exemplo: globallabs.academy

- URN: Uniform Resource Name. Recurso que será identificado. Exemplo: /category/blog/

- URI: Uniform Resource Identifier. É o identificador do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globalllabs.academy/category/blog/

*URI une o protocolo (https://), URL (globallabs.academy) e a URN (/category/blog)

------------------------------------------------------------------

#### XML - Extensible Markup Language

- É uma linguagem de marcação;

- Utilizada para compartilhamento de informações através de requisições HTTP. Exemplo:

```
<xmlcep>
    <cep>22041-001</cep>
    <logradouro>Avenida Atlântica</logradouro>
    <complemento>de 2174 a 2634 - lado par</complemento>
    <bairro>Copacabana</bairro>
    <localidade>Rio de Janeiro</localidade>
    <uf>RJ</uf>
    <unidade/>
    <ibge>3304557</ibge>
    <gia/>
</xmlcep>
```

-----------------------------------------------------------------

#### JSON - JavaScript Object Notation

- É um formato de troca de dados entre sistemas, independentemente da linguagem utilizada, derivada do JavaScript;

- Muitas linguagens possuem suporte nativo ao JSON. Exemplo:

```
{
    "cep":"22041-001",
    "logradouro": "Avenida Atlântica",
    "complemento": "de 2174 a 2634 - lado par",
    "bairro": "Copacabana",
    "localidade": "Rio de Janeiro",
    "uf": "RJ",
    "unidade": "",
    "ibge": "3304557",
    "gia": ""
}
```

-------------------------------------------------------------------

#### Flask

- É um *microframework* para Python, utilizado para desenvolvimento de aplicações web;

- É chamado de *microframework* porque mantém um núcleo simples, mas é estendível;

- Flask não possui camada de abstração para banco de dados, validação de formulários, entre outros. Mas, é possível estender com outras bibliotecas;

- Por ser leve e simples de se usar, Flask é um dos *frameworks* Python mais utilizados para desenvolvimento de API's.

-------------------------------------------------------------------

#### Desenvolvido por Henrique Matheus Alves Pereira