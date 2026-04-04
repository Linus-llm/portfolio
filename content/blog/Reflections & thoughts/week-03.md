+++
date = '2026-04-04T16:27:24+02:00'
draft = false
title = 'Week 03'
+++

So I have decided on using the Open Library API which is API that is connected to a big book database. I thought it would be a great starting point to bring API into my project.
I will have books integrated in to my collection application since in my opinion it's quite an area or field that is highly collected. I chose to go with Open Library books since it was literally the first thing I stumpled upon when looking up APIs and it is free to use. My idea with this API is that the User will be able to put in a book with the ISBN number or the title of the book and then my code should do the rest of the work with filling out the information needed to create the item. Those are my initial thoughts (Might change)

I have a problem regarding ISBN because of the API I'm using. When searching for a book on a keyword it will produce a result which has 4 ISBN's and I don't know what is correct and what isn't. So I'm thinking of not using the ISBN in my work. I don't even know if its relevant to store for me.

I have created a book entity which will have its own database table. I think that is the cleanest way of going about this. It will take more time but it will be a better way of storing the data in my opinion. 

I have now access to the API and can receive data. I switched which method I wanted to start with to one where the User can search on a keyword for example "Harry Potter" and then it will provide a list of 10 results and the user will then be able to choose which one it is they have and then it will be placed in the database. 