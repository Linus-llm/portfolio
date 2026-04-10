+++
date = '2026-04-06T19:11:24+02:00'
draft = false
title = 'Week 08 post'
+++

In the eighth week of the project:

I have modified the User so that it now only contains username, password, email, roles, and collections. I have deleted phone number, last name, and first name.
User creation is now completely a part of securityDAO. I have removed it from the UserController and DAO. I have also removed or commented out the endpoint in main. The user creation part of my project is now under /api/auth/register.

I have had to change my UserDAO and its EntityManagerFactory due to it grabbing the wrong instance, or it was more like it wasn't grabbing the one from its constructor, which I have fixed now. Instead of the SecurityDAO taking in a DTO as a class, now it is User. I have modified my BookService. The BookService class is also more for me as a guide to what functions the users will have at their disposal and a guide for my frontend when I get there. The code in there is not tested (only manually in the console).

getByName() in CollectionDAO has been modified to take a user in the parameter to connect it to a user; otherwise, it could possibly find collections with the same name but from a different user.

The Item entity now has fetch type eager on its collection to make sure that its collection is always there. The Item constructor now has collection in it. All of this goes for Book as well, since it is a subtype of Item. All DAO tests are now complete. Not every CRUD method is tested since some of them are not necessary in my eyes (to be tested).

Collection now has fetch type eager on items as well, for the same reason as the item with collection.

I have finished the DAO testing. The security DAO interface is holding two methods that I am currently not using: createRole() and addUserRole(). I am not deleting them or throwing them away because I might need them later. My main reason for keeping them is because I am not entirely sure if I want an admin role or not yet; it depends on where I want to take my project.
IDAOTest class is now complete.
ItemControllerTest is renamed to ControllerTest and is complete with tests.
ControllerTest holds all of the integration tests. The tests are set up with the security package on top of it. 

I have fixed an endpoint that had the same routing. By fixed, I mean that I have renamed or restructured my endpoints to have a better hierarchy, in my opinion. Before, some of my endpoints had /item/{collectionId}, which I now have made into /collection/{collectionId}/item. This is just one example.

Thoughts during the week:

I have removed the fields from the user because they aren't needed for where I want to take the project. I want it to stay as just a collection tracker, and I think at some point I had in mind that there would be a hub of some sort for other collectors to see information about each other (might happen at some point, but not for now). So that's why I removed it.

I am really considering if I need the admin role, because as the project is right now, there is no use for it, at least from what I can think of. My reason for that is why there would be an admin that can see or change every collection there is. This isn't something I have decided on yet, because I recognize that I have some endpoints that don't make sense if there are multiple people using my application. An example of such an endpoint would be /api/user, which gives back a set of all users in the database. So maybe I should make an owner role which would be the only role that has access to that endpoint. That could be a solution, and then I could make use of the createRole() method, which is inactive as of now.

I have completed the tests for the project for what I already have built. There will be more in the coming weeks and months for sure.

