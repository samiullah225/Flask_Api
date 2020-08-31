# Flask_Api
This repo consist of 5 parts as under.

1) FileUpload.py  is server file with two routes. First route is '/' the base route, which serves front end form to collect
file from user. Another route /upload is used to save the uploaded file to server.

2) Count_Names.py is used to count names that contains siddique in their last name.

   3&4) Combining 1 and 2 means to upload text file and count name in it. Goal1AndGoal2.py has three routes  as under
   --> The / base url is used to request html page which is form to upload the file that contains names.
   --> The /uploader route is used to process the upload file and count the names that contains  siddique in their last name.
       It also saves the names of user in file to database file named as User.db
   --> The /names route is used to retreive  the saved names in database from the files.
   
5)  TODO.py contains three routes as follow,
    --> The /todo/create is used to create new todo by passing title as get request for example
	    http://127.0.0.1:5000/todo/create?title=hit the gym
	--> The /todo/delete is used to delete created todo by passing its id for example,
	    http://127.0.0.1:5000/todo/delete?id=2
	--> The /todo/show is used to list all saved todos. It return json array of todos.