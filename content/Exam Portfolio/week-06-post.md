+++
date = '2026-04-04T16:41:24+02:00'
draft = false
title = 'Week 06 post'
+++

In the sixth week of the project:

The ItemControllerTest class has been added to the project alongside the test.http file.
ItemControllerTest utilizes RestAssured and Hamcrest to test its endpoints. The tests do not cover all yet.
I have made the test for a book creation and a user creation. As of now, I have only done these two.

My ItemControllerTest contains a setup method which starts a Javalin server. I then add simple endpoints directly to the app Javalin instance with app.get, app.post, app.put, and app.delete. All this is done in setup with the @BeforeAll annotation.

I have a shutdown method with the @AfterAll annotation to shut down the Javalin app instance.


Thoughts during the week:

I had some trouble with understanding and getting RestAssured and Hamcrest to work. So I struggled during this part of the project, and that's why I only ended up doing 2 tests for now. But I wanted to do the POST or create tests because I think that is the "harder" test instead of a GET test.
The plan ahead will be to at least have a test of each POST, PUT, DELETE, and GET.

During my thinking process of setting up the test, I had a hard time understanding just how I was going to prove or compare my result to what I wanted it to be. I started with it just having the test turn green or true if the statusCode of the given() would be 200, but that way I couldn't really be sure if what I got back was true, which led me to finding .body, where I could test the JSON I got back from my API against the JSON that I gave at the start. I also ended up changing the status code of the request to 201 since it is called "created" and should be given back when something has successfully been created. All of this is true for both of my POST or creation tests.