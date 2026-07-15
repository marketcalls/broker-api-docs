# Response Structure

## Success Responses

### Single Object Format

```json
{
  "status": "success",
  "data": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

### Multiple Object Format

```json
{
  "status": "success",
  "data": [
    {
      "key1": "value1",
      "key2": "value2"
    }
  ]
}
```

## Error Responses

```json
{
  "status": "error",
  "errors": [
    {
      "error_code": "string",
      "message": "string",
      "property_path": null,
      "invalid_value": null
    }
  ]
}
```

## Error Properties

| Field | Description |
|-------|-------------|
| error_code | Specific error identifier |
| message | Human-readable error description |
| property_path | Request portion causing error (nullable) |
| invalid_value | Problematic value (nullable) |

## Deprecation Notice

CamelCase field variants (`errorCode`, `propertyPath`, `invalidValue`) are deprecated. Use snake_case versions for forward compatibility.
