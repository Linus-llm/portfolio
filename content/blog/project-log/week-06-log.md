+++
date = '2026-04-04T16:41:24+02:00'
draft = false
title = 'week 06 log'
+++

In the sixth week of the project:

The ItemControllerTest class has been added to the project alongside with test.http file. 
ItemControllerTest utilizes RestAssured and hamcrest to test its endpoints. The tests do not cover all yet.
I have made the test for a book creationg and a user creation. I have as of now only done these two.

My ItemControllerTest contains a setup method which startes a javalin server. I then add simple endpoints directly to the app javalin instance directly with app.get - app.post - app.put and app.delete. All this is done in setup with @BeforeAll annotation

I have a shutDown method with @AfterAll annotation to shutdown the javalin app instance.

