# Delivery_Management
#Endpoints
POST api/registerUser/
{
"username":"Ali",
"password":"123",
"password2":"123"
}
POST api/login/
{
"username":"Ali",
"password":"123"
}
POST api/logout/
{
}
POST api/customer/order/
{
"name_customer":"Mouad",
"cin" :"BW123476",
"adress_customer":"Casablanca",
"adress_recipient":"Rabat",
"nature_of_package":"clothes",
"number_phone_customer":"0912873467"
}
POST api/driver/statuses/
{
"user":"Mohamed"
"order":""
statue:"processing"
}
GET api/administrator/order/
GET api/administrator/statuses/





