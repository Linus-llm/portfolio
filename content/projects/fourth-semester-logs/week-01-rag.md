+++
date = '2026-08-23T17:06:24+01:00'
draft = false
title = 'Week 01 RAG'
+++

Thoughts:

I have been trying out making a very simple rag using Dify.ai together with openai api. 
During the weeks classes it was said to be smart to convert the pdf that we are using as a test to markdown since it is a good file format for llms to work with. 

During the class our teacher showed that we could use "markitdown" which is a python library and command line tool that can convert several file types into markdown. Our teacher said that it was a fast tool and that we could use something called "Marker" which is also a python library but the tool is more extensive in its conversion algorithm/technique and thus use more power/time. 

I decided to give Marker a try and I get my openai api key connected to the RAG I made from blank on Dify.ai. I got it to convert the pdf and it looked relatively good when I opened it in vscode, but for some reason my RAG is not able to read the content properly. When I ask it about specific text under a specific point it says it doesnt have access to it, which is weird because when I open the markdown file the content is there. 
I tried to give the knowledge bank the pdf and then it could chunk it and embed it as a pdf instead of mk but the result is the same which is pretty weird to me. 

I checked how many chunks it had on the pdf (700) and the markdown-file (300 ish).

I dont know if its an embedding problem?
