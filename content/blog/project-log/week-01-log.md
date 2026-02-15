+++
date = '2026-02-15T17:06:24+01:00'
draft = false
title = 'week 01 log'
+++

From the 6/02-8/02 I began working on the actual code base of my collection tracker application. 

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