+++
date = '2026-04-06T19:11:24+02:00'
draft = false
title = 'Week 08 post'
+++

In the eigth week of the project:

I have modified the User so that it now only contains Username, password, email, roles and collections. I have deleted phonenumber, lastname, firstname. 
User creation is now a part of securitydao completely I have removed it from the UserController and dao. I have also removed or commented out the endpoint in main. The user creation part of my project now is under /api/auth/register. 
I have had to change my UserDAO and its entityManagerFactory due to it grabbing the wrong instance or it was more like it wasn't grabbing the one from its constructor which I have fixed now. Instead of the SecurityDAO taking in a DTO as class now it is User. I have modified my bookService. The bookService class is also more for me as like a guide to what functions the users will have at their disposal and a guide for my frontend when I get there. The code in there is not tested (only manually in the console). 

getByName() in collectionDAO has been modified to take a user in the paramter to connect it to a user otherwise it could possibly find collections with the same name but from a different user. 

The Item entity new has fetch type eager on its collection to make sure that its collection is always there. Items contructor now has collection in it. All of this goes for book as well since it is subtype of item. All of DAO tests are now complete not every CRUD method is tested since some of htem are not necessary in my eyes (to be tested)

Collection now has fetch type eager on items as well for the same reason as the item with collection.

I have finished the DAO testing. The security dao interface is holding two methods that im currently not using createRole() and addUserRole() I am not deleting them or throwing them away because I might need them for later. My main reason for keeping them is because I am not entirely sure if I want an admin role or not yet, it depends on where I want to take my project. 
IDAOTest class is now complete
ItemControllerTest is renamed to ControllerTest and is complete with tests.
ControllerTest holds all of the integration tests. The tests are setup with the security package on top of it. 

Thoughts: 

I have removed the fields from the user because they aren't needed for where I want to take the project. I want it to stay as just a collection tracker and I think at some point I had in mind that there would be a hub of some sort for other collectors to see information about each other (might happen at some point but not for now). So thats why I removed it.
I am really considering/contemplating if I need the admin role, because as the project is right now there is no use for it at least what I can think of. My reason for that is why would there be an admin that can see or change every collection there is. This isnt something I have decided on yet, because I recognize that I have some endpoints that doesnt make sense if there is multiple people using my application. An example of such endpoint with be api/user which gives back a set of all users in the database. So maybe I should make an owner role which would be the only role that has access to that endpoint that could be a solution and then I could make use of the createRole() method which is inactive as of now. 

I have completed the tests for the project for what I already have built. There will be more in the coming weeks and months for sure. 

