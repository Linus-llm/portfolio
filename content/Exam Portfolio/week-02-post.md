+++
date = '2026-04-04T16:20:24+02:00'
draft = false
title = 'Week 02 post'
+++

In the second week of the project I have created entities:
User entity 
Collection entity 
User DAO
Collection DAO
DAO interface

The DAO's have a shared interface which as of now holds the CRUD methods. 
The shared getAll methods withing the DAO interface is where I utilize JPQL.

return new HashSet<>(em.createQuery("SELECT c FROM Collection c", Collection.class).getResultList());


Besides the DAO's and entities I have created a single unit test. 

First JPA relationships have been created


Thoughts, ideas, and reflections from the second week:

I want my user to have collections of items. So the user shouldn't be able to hold items, but only collections. This makes it easier if I want to remove a user.
If I remove a user, then the collections and the items within should be removed.

-------------------------
ERD and entity thoughts:

I originally, from week 1, made the item entity very wide and generic, with the purpose of leaving some variables null.
The variables or fields that I'm talking about are pieceCount, model, and series. Originally, I wanted to keep them in so that Item could, in theory, fit any item thrown at it.
But I'm having second thoughts about that. It is not the cleanest way to do it, in my eyes at least. I want Item to be minimal and generic. Then I can always expand with subclasses of item and use Item as a base. This means that I will introduce a new Enum to the code, and the Item entity will have a variable called type.

Users are very minimal, no address. I think the users should be able to contact each other through either phone or email and then define an address.
Collections.
This means that there will be a OneToMany relationship between items and collections.
There will be a OneToMany relationship between User and Collections as well.

-------------------------
Thoughts while coding:

As of right now, I have made password to just be a string. (this will be changed in the future)
In JPA, I have set the relationship up with cascade all because I want it to be so that if a user is removed, then all of the collections and items the user had are gone.
And I want it so that the same happens if just one collection is deleted, then the items within that collection are also gone.