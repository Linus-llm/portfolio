+++
date = '2026-04-04T19:11:24+02:00'
draft = false
title = 'Week 07'
+++

Thoughts and reflections during the week:

I have not altered what we went through during class very much the only thing that has been changed to fit into my project is the way in my Main class. Since I am still putting my endpoint directly into my app instance of javalin in my main class I had to alter or cut a few things. Thomas has been using I think the class is called ApplicationConfig which I haven't incorporated into my project. This means that I only had to put the beforeMatched directly onto where I launch or carete the app instance:
Javalin app = Javalin.create(config -> {config.showJavalinBanner = false;}).start(7070)
                .beforeMatched(securityController::authenticate)
                .beforeMatched(securityController::authorize);
I am finding the applicationConfig class to be a little bit overwhelming for my tastes so I have sticked to doing hte endpoints in main. And besides being a little overwhelmed with the way it has been setup inside of Thomas' project I don't really see the appeal why I should do it that way in my project since it is still fairly small. That is at least the thoughts I have had on this matter during the week but I don't know yet if I should change this or not. This means that my login and register call is also inside of my Main class. 
they are under /api/auth/ both of them
