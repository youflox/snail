# snail
User can upload a JSON file and can save the data in a database.

username: admin
password: admin

#Technologies used
- Python
- Django
- DRF
- VueJS

#Requirements: 
- Python (3.8)
- Django (4.0.2)
- DRF (3.13.1)
- npm (6.13.4)
- Node (v12.14.0)
- vue/cli (4.5.13)
- npm(6.13.4)
- Bootstrap(5.1.3)

#Project setup
once Required versions of Python, node and vue are installed.

- Go the project level "/snail"  run the following commands

- pip install -r requirements.txt
- npm install

#AUTH used
- Django session based authentication.


#Django Restframework Endpoints

- Login : http://localhost:8000/login/
	methods: POST
	data format : {
			"username" : admin,
			"password" : admin
			}
			
- Signup: http://localhost:8000/signup/
	methods: POST
	data format : {
			"username": "username",
			"email" : "email@email.com",
			"first_name":"name",
			"last_name" : "name",
			"password": "passowrd"
			}
			
-file ://localhost:8000/file/upload/
	methods: GET, POST
	
	GET method shows all the uploaded files details.
	
	POST format : {
			"file": FILE
			}

- push file data to database : http://localhost:8000/data/
	methods: POST
	 format : {
 		"file_id" : INT
	 		}
	 		
	 		
- Check the pushed file data : http://localhost:8000/data/upload/<int:id>/
	method: GET
	
	- File should be uploaded by the user only then the GET req will return the file data.
	

#Front end url's

- SIGNUP : http://localhost:8081/#/signup

- LOGIN : http://localhost:8080/#/login

- About : http://localhost:8080/#/about 

- HOME : http://localhost:8080/#/home (LOGIN REQUIRED)

- LOGOUT : http://localhost:8081/#/logout (LOGIN REQUIRED)



#Application flow

- User should login to access HOME page.

- From home page user can upload the file, update the data and view the data.

- Once the file is uploaded then it will be added to the server.

- User can click on "upload" to upload the data to the database.
























