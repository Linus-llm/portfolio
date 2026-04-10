+++
date = '2026-04-06T19:11:24+02:00'
draft = false
title = 'Week 08 post 2'
+++

Work during the week:

I have fixed a test isolation issue with the DAO tests. I had hardcoded some values, which caused the tests to fail when run in sequence.

Fixed user so that username is unique. This means that the controller now tells the client that the username already exists.

I have now deployed my project to my droplet.

My controllers are now handling authorization from users much better due to an additional check in their methods. This method is to check whether or not the user that is asking something from the API is the same user who it originated from.

I have changed my controllers so that they handle responses to the client better. It is more consistent now with its responses; now it only gives back JSON in the same style. Before, some of it was just strings, but now everything is JSON. I made an ApiResponseDTO to streamline it a bit. 

public class ApiResponseDTO {
    private int status;
    private String message;

    public ApiResponseDTO(int status, String message) {
        this.status = status;
        this.message = message;
    }
}

I fixed a small logic error in my UserController where I checked for ownership before I checked if the user was null, so I fixed that.

I have refactored the way exceptions are handled in my project by adding a global exception handler in my Main class to the Javalin app instance. That means that the exceptions will bubble up and eventually be caught there, and the handlers will return my ApiResponseDTO with a status code and a message.

I have removed my RetrieveDAO since it has not been used once in my project and I don't see the need for it. I have now added the custom item creation endpoint so that custom items can be created.

Thoughts and reflections:

My endpoints have been set up wrong, or not wrong, there just isn't the security layer that I wish was there on them yet. Because as of now, everybody can see anyone's items and collections, which I intend to fix. This has been fixed now.