+++
date = '2026-04-04T19:11:24+02:00'
draft = false
title = 'week 07 log'
+++

In the seventh week of the project:

Security layer has been added. I have added a security layer and put it in a package. 
The package contains:
- ISecurityController
- ISecurityDAO
- ISecurityUser
- Role (enum)
- SecurityController
- SecurityDao
- UserRole
- User (changes to existing Class)
- ValidationException
- ApiException

The security controller interface has the methods login, register, authenticate and authorize
The security DAO interface has the methods getVarifiedUser, createUser, createRole, addUserRole 
The security user interface has the methods getRolesAsStrings, verifyPassword, addRole and removeRole
Role enum has ANYONE, USER, ADMIN

A lot of this code has been taken directly from my teacher Thomas which he went over during the week.

The code works by directing trafic through this layer before the other endpoints this is done in my Main class
with these lines: 
app.post("/api/auth/login", securityController::login);
app.post("/api/auth/register", securityController::register);

So the authenticate method works by checking if the matched endpoint is protected by a role or not if that is true then we skip because then there is no reason to check anything. If there is however a role then we make a verifiredTokenUser and store it in the ctx object. Then the authorize method runs and checks if the endpoint is open or not and if not then we run the method userHasAllowedRole and if not then we are met with an ApiException with a statuscode 403. (All of this is after login or register)

The login takes the received JSON and converts it into a DTO that DTO is then used in the securityDAO and run through getVerifiredUser method then a token is created and both the found user object and the token object is but into a node and sent back to the client if everything goes well with a 200 status code. If any of the above goes wrong a ApiException with 401 status code is thrown. Register work by taking the received JSON and converting it into a DTO object, that object gets checked for null and if not null then the createUser method is run and if everything goes well then the newly created user is put into the database and a node is given back to the client with a "user registered" msg and a 201 status code.

I will not go in depth with the token methods here but they are being utilized in my project.
