Существует 3 сущности Client, Document и Relative. Для них соответственно 3 запроса
REST

GET /clients/123
GET /clients/123/documents
GET /clients/123/relatives

Эти запросы можно заменить на аналогичные через  graphql или наоборот, более емкие.
Теперь клиент может сам выбрать какие данные ему нужны и не запрашивать лишние.
Благодаря новому подходу можно одним запросом получить все данные при необходимости, при этом не менять ничего не сервере.

Схема с GraphQL находится [тут](schema.graphql)

``` json
query {
  client(id: "123") {
    id
    name
    age
  }
}

query {
  client(id: "123") {
    id
    name
    documents {
      type
      number
      expiryDate
    }
  }
}

query {
  client(id: "123") {
    id
    name
    age

    documents {
      id
      type
      number
      issueDate
      expiryDate
    }

    relatives {
      id
      relationType
      name
      age
    }
  }
}
```