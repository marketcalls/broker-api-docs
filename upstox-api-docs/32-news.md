# News

## Overview

API to retrieve news for one or more instruments. This API returns news published in the past 7 days (one week). You can fetch news articles in three ways — for specific stocks you're interested in, for instruments you currently hold a position in, or for stocks in your long-term portfolio:

1. **Specific instruments** — pass `category=instrument_keys` along with the instrument keys you want news for (up to 30 at a time).
2. **Your open positions** — pass `category=positions` and the API automatically fetches news for everything you currently have a position in.
3. **Your holdings** — pass `category=holdings` and the API fetches news for all stocks in your holdings portfolio.

## Endpoint

**GET** `https://api.upstox.com/v2/news`

## Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| category | Required | string | Category of news to fetch. Allowed values: `instrument_keys` , `positions` , `holdings` . |
| instrument_keys | Optional | string | Comma-separated list of instrument keys. Required when `category` is `instrument_keys` . Maximum 30 keys per request. |
| page_number | Optional | integer | Page number for pagination. Range: 1–100. Default: `1` . |
| page_size | Optional | integer | Number of records per page. Range: 1–100. Default: `100` . |

## Response

```json
{
  "status": "success",
  "data":{
    "NSE_EQ|INE040H01021": [
      {
        "heading": "SMIDs outperform: Nifty Smallcap 100, Nifty Midcap 100 rise over 2%; Suzlon Energy, Afcons Infra top gainers",
        "summary": "On a year-on-year basis, the Nifty Midcap 100 index has gained 13%, while the Nifty Smallcap 100 gauge rose 6%",
        "thumbnail": "https://assets.upstox.com/content/assets/images/news/traders-assemble-hero.webp",
        "article_link": "https://upstox.com/news/market-news/latest-updates/smids-outperform/article-181757/",
        "published_time": 1776251261821
      }
    ]
  }
  "metadata": {
    "page": {
      "page_number": 1,
      "page_size": 10,
      "total_records": 1,
      "total_pages": 1
    }
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Possible values: `success` , `error` |
| data | array | Data object which contains one instrument key mapped to an array of news items for that instrument. |
| data.heading | string | Headline of the news article. |
| data.summary | string | Brief summary of the news article. |
| data.thumbnail | string | URL of the article thumbnail image. |
| data.article_link | string | URL to the full news article. |
| data.published_time | number | Unix timestamp in milliseconds indicating when the article was published. |
| metadata.page.page_number | integer | Current page number returned. |
| metadata.page.page_size | integer | Number of news records returned per page. |
| metadata.page.total_records | integer | Total number of records matching the query. |
| metadata.page.total_pages | integer | Total number of pages available. |

## Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1189 | **Invalid category** - The provided category is not valid. Allowed values: `instrument_keys` , `positions` , `holdings` . |
| UDAPI1190 | **instrument_keys required** - The `instrument_keys` parameter is required when `category` is `instrument_keys` . |
| UDAPI1193 | **Instrument key limit exceeded** - News can be fetched for a maximum of 30 instrument keys per request. |
