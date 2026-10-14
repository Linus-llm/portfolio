+++
date = '2026-10-13T17:06:24+01:00'
draft = false
title = 'Security-tech reflections'
+++

Security and tech reflections:

In this project we have mainly used the same tech stack as other previous projects. 
Java, Hibernate, JPA, postgreSQL, Vite, React. We do have a mail service SMTP which is new for me. This touches upon credentials as well. 

There isn't too much to it we have placed credentials away from our source code and placed it .env-files and they are placed inside of our .gitignore so that they aren't posted on github. But this doesnt ensure that the agent hasn't read them since the files are still on our local machines. But at the same time as long as we make sure to not make these files publically available it isn't that big of a deal. I highly doubt that the Anthropic or OpenAi are going to start leaking data from its users/agents. 

Though there is another scenario where your agent reads the .env and then generates code containing that. It could put these important credentials somewhere it shouldn't like in a log, or a commit. 

We have tried to avoid ai reading this by limiting what it can read through our tickets but we can't guarantee that it hasn't read it.