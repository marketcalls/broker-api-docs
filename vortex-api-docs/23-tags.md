<!-- Source: https://vortex.rupeezy.in/docs/2.2/tags/ -->

# Tags

Use the below apis to manage Tags:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/reports/tags](#fetch-tags) | Fetch all tags in the account | 1/sec |
| `POST` | [{{base_url}}/reports/tags](#create-tag) | Create a tag | 1/sec |
| `PUT` | [{{base_url}}/reports/tags/{tag_id}](#modify-tag) | Modify a tag | 1/sec |
| `DELETE` | [{{base_url}}/reports/tags/{tag_id}](#delete-tag) | Delete a tag | 1/sec |

## Fetch Tags

```
Endpoint: {{base_url}}/reports/tags
```

### Fetch Tags Response

```
{
    "status": "success",
    "data": [
        {
            "id": 6,
            "client_code": "DEMO001",
            "name": "API 5",
            "description": "fredsfadf",
            "created_at": "2023-12-05T15:13:45.53Z",
            "updated_at": "2023-12-05T15:13:45.53Z"
        },
        {
            "id": 7,
            "client_code": "DEMO001",
            "name": "API 5",
            "description": "fredsfadf",
            "created_at": "2023-12-05T15:17:38.953Z",
            "updated_at": "2023-12-05T15:17:38.953Z"
        }
    ] 
}
```

## Create Tag

```
Endpoint: {{base_url}}/reports/tags
```

### Create Tag Object

```
{
    "name": "Swing", 
    "description": "source 1"
}
```

| field | description |
| --- | --- |
| name | Name of the tag. Max length 50 |
| description | Description of the tag. Max length 100 |

## Modify Tag

```
Endpoint: {{base_url}}/reports/tags/{{tag_id}}
```

### Modify Tag Object

```
{
    "name": "Swing 2", 
    "description": "source 3"
}
```

| field | description |
| --- | --- |
| name | Name of the tag. Max length 50 |
| description | Description of the tag. Max length 100 |

## Delete Tag

```
Endpoint: {{base_url}}/reports/tags/{{tag_id}}
```

- Once a tag is deleted, it stops appearing in the list of tags and the tag id cannot be used again while tagging orders. However, orders which are already tagged will keep on showing the tag id even if the corresponding tag is deleted.
