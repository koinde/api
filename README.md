# API interface
https://www.koinde.com 

The OTC and orderbook hybrid exchange for bitcoin.


API Documents and Reference Scripts


Method: POST

    Header: {

      "Content-Type"   : "application/json"

      "Authorization"   : "your_api_key"

    }


Body: JSON


Name of API: UPDATE ADVERTISEMENT


URL: https://www.koinde.com/api/v1/update-ad

Request-1,

    {

      "ad-id": 1,

      "price": 3568.458,

      "status": "active",

    }
 
 

Response-1

    {

      "is_authenticated": true,

      "message": "Your ad is updated successfuly.",

      "status": "success"

    }



##########################################

Request-2

    {

      "ad-id": 1,

      "price": 3568.458,

      "status": "passive",

     }
 
Request-3

    {

      "ad-id": 1,

      "price": 3568.458

     }
 
Request-4

    {

      "ad-id": 1,

      "status": "active",

     }

Response-error


Status= HTTP 401 

Unauthorized Attempt


    {

      "is_authenticated": false,

      "message": "Unauthorized attempt.2",

      "status": "error"

    }


# Public endpoints

ENDPOINT 1

ASSETS   https://www.koinde.com/api/v1/assets
The assets endpoint is to provide a detailed summary for each currency available on the exchange.
OUR RESPONSE
    {
      "coins":{
        "BTC":{
          "can_deposit":true,
          "can_withdraw":true,
          "maker_fee":"0",
          "max_withdraw ":"100",
          "min_withdraw":"0.00200000",
          "name":"Bitcoin",
          "taker_fee":"0",
          "unified_cryptoasset_id":1
        }
      }
    }


ENDPOINT 2

TICKER   https://www.koinde.com/api/v1/ticker
The ticker endpoint is to provide a 24-hour pricing and volume summary for each market pair available on the exchange.
OUR RESPONSE
    {
      "btc_try":{
        "change":1682.4339,
        "high24hr":39987,
        "highestBid":40348,
        "last":38304.5661,
        "lastUpdate":1576679869,
        "low24hr":38304.5661,
        "lowestAsk":39007.42541,
        "percentChange":-0.04,
        "volume":11.5019
      }


 
ENDPOINT 3

ORDERBOOK  https://www.koinde.com/api/v1/orderbook/btc_try
The order book endpoint is to provide a complete level 2 order book (arranged by best asks/bids) with full depth returned for a given market pair.
 
OUR RESPONSE
{
  "asks":[
    42652,
    0.59
  ],
  "bids":[
    41402.88222,
    1.5434
  ],
  "timestamp":"1576672254"
}


ENDPOINT 4

TRADES   https://www.koinde.com/api/v1/trades/btc_try/
The trades endpoint is to return data on all recently completed trades for a given market pair.
 
OUR RESPONSE
[
  {
    "base_volume": 4710.1,
     "price": 47101.0,
     "quote_volume": 0.1,
     "trade_id": 15,
     "trade_timestamp": 1574257873.77,
     "type": "ask"
  },
…
]  


SUMMARY EDNPOINT https://www.koinde.com/api/v1/summary
OUR RESPONSE 

{
  "code":"200",
  "coins":{
    "BTC":{
      "deposit":true,
      "name":"Bitcoin",
      "withdraw":true
    }
  },
  "data":{
    "btc_try":{
      "change":1438.61368,
      "high24hr":44507,
      "highestBid":43400,
      "last":42255.38632,
      "lastUpdate":1577441043,
      "low24hr":41711.84811,
      "lowestAsk":42200.37564,
      "percentChange":-0.03,
      "volume":6.9817
    }
  },
  "msg":"success"
}




Rate limit: 5 second each request interval


