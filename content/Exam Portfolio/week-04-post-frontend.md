+++
date = '2026-05-17T17:06:24+01:00'
draft = false
title = 'Week 04 post frontend'
+++

The week's work

This week I worked a lot on connecting the frontend to the backend through apiFacade.js.

The apiFacade.js file now contains most of the methods needed by the frontend. This includes methods for logging in, registering users, fetching collections, fetching items, creating collections, creating items, and searching for users as an admin.

I also worked on the admin part of the project. On the frontend, I added logic that checks whether the logged-in user has the ADMIN role. If the user is an admin, extra navigation options become available in the navbar.

The admin page does not have a large amount of functionality yet, but it can currently:

* Search for a user by ID
* Search for a user by username
* Edit selected user details
* Delete a selected user

To make this work, I also had to make changes in the backend. I added admin-specific routes using /api/admin/user as the base route.

During this process, I ran into a problem where some routes did not work for admin users. The issue was that the backend routes were only protected with the USER role. I decided that I would allow the ADMIN role on every route that I have in my backend. This is a design choice that I may change in the future because I am not fully sure if that's what I intend for the ADMIN role.

I also changed the frontend route for the item page. Earlier, the route was just:

/itempage

However, this was not enough because the item page needs to know which collection it belongs to. I changed the route so it includes the collection ID:

/itempage/:collectionId

This allows the frontend to use the collection ID from the URL and fetch the correct items from the backend.

Thoughts and reflections

This week made me realize how much the frontend structure depends on the backend data model.

At first, I thought of pages mostly as visual parts of the application. However, once I started connecting the frontend to real backend data, I had to think more carefully about how data moves through the application. For example, an item does not exist by itself in this project it belongs to the collection which means that the relationshop should be reflected on the frontend side as well.

Adding the collectionId to the URL made the application more logical. It also made it easier to refresh the page or go directly to a specific collection's item page, because the page can fetch the correct data based on the URL. 
To clarify maybe more logical is not the right word but more intuitive that you have to click on a collection to be able to create an item.

I am begging to consider doing something with the apiFacade.js file because it is getting very huge. 

This was probably the week were I could really see everything come together because of the connection between my react components, my javascript in apiFacade and my backend.
