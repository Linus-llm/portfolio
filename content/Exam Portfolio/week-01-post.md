+++
date = '2026-02-15T17:06:24+01:00'
draft = false
title = 'Week 01 post'
+++

Work from the first week of the project:

- What am I using in this project:
I am using Hibernate 7.1.0.Final, Maven 4.0.0 and Amazon Corretto 17.0.16

- Structure of the code base:
I have it structed so that everything is within the directory .app
within .app I have the folders and files:
1. config
   - HibernateConfig
2. entities
   - Item
   - ItemCondition (enum)
   - ItemDAO
   - ItemStatus (enum)
3. exceptions
   - ApiException
4. utils
   - Utils
5. Main

This means I have setup the early structure of the code base and configured the HibernateFile and made my entities as of now. I have made simple CRUD methods in the DAO file. 

Thoughts, ideas and reflections from the first week:

So the first week for me had been a little bit postponed since I was away. But the one of the first ideas that came to me as a brainstormed or searched for ideas was a collection tracker. It is meant both to be used to gather a nice overview of ones collection through a visual interface. My thoughts about it was that it needs to be something that both passionate collectors and "normal" people can find useful. So as of now my intentions are to have a lot of fields in the creation part of the an item, that you can leave blank if you don't care about filling every detail, thus catering to the regular and passionate people.

The reason I went with this idea is because I can imagine and think back on when I collected cards that it was so hard to keep track of what I had. Of course you can remember the special things in your collection but what about the ones that is just a little notch behind the special things those can be harder to remember but they can still be a vital part of the collection.

I have only thought about the database layout and domain model in my head. So that will be next weeks goal to have an early ERD and Domain-model. 