+++
date = '2026-04-04T16:32:24+02:00'
draft = false
title = 'week 05 log'
+++

In the fifth week of the project:

This mean I will work on completing the method for the user so that they can choose a book and store it in the database with the needed information about the book. This means I will be creating a new table in my database called Books. it will work nearly the same as Items but will be holding different information. it will have a collection_id. 
After that is done I will start work on my own REST API and have the proper documentation for it. 

I have now made the first method in my BookService class that can save an Item to my database as the type Book. Right now it is taking user input from the console, so that needs to change at some point but for now it is working. It is set simply up so the user just chooses a number from a list to what matches the wished or desired input. 
At the moment in my BookService class I have a method that is named saveBookChoiceToDatabase(String keyword). This takes a keyword that the user needs to choose (right now it is in main)
and then it will help the user by creating choice lists. So this is where at the moment my User is created (dummyUser) and a collection is created and set to that user and finally the Book is put/set in the collection and then created in that order. This is because the user owns the collection and the collection owns the item/book. Finally the method for now just prints to console "Book saved to database successfully".

I have created three controllers UserController, ItemController, CollectionController. I will avoid making a controller for each individual sub-Item class if I can avoid it. 

So regarding the endpoint selection:
I have decided to use /api as like a collector or binder to the rest. all the user "crud" methods are under the /user. for collections it is different if you want a list of a users collections then it is under /users/{userId}/collection and if you to create it is under the same endpoint. but for the other crud methods regarding collections it is covered by the /collection. I have now created 3 controller classes. Some of the controllers at the moment have logic that should be in a service class but that will be done during the week.