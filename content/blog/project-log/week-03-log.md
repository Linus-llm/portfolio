+++
date = '2026-04-04T16:23:24+02:00'
draft = false
title = 'week 03 log'
+++

In the third week of the project:

I have created a Book entity, BookDAO, BookDTO, OpenLibraryDTOresponse and BookService.

Book entity and BookDAO has just been created I haven't done anything with them yet.
I focused on using and making sure that my BookDTO, OpenLibraryDTOresponse and BookService is working before I even proceed to map anything to the database.
I have made the methods inside the BookService static for now so you need to call the class and then the method to use it. Im using the OpenLibraryDTOresponse as like a wrapper to get what is inside "docs" which is an array in the JSON reponse. 
For now it is possible to get a List as a response now I'm just missing the part where it maps to the user and the database.