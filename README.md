# api
koinde.com api interface


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

"status":  "error",

{

"is_authenticated": false,

"message": "Unauthorized attempt.2",

"status": "error"

}


Rate limit: 5 second each request interval


