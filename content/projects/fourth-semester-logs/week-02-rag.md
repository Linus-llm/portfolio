+++
date = '2026-08-27T17:06:24+01:00'
draft = false
title = 'Week 02 RAG'
+++

Thoughts, work and reflections:

Min umiddelbare tanke til denne problemstilling (opdatering af RAG) er om man ikke kan få GitHub actions til at få fat I Dify på en eller anden måde?
Jeg tænkte at det ville være smart at opdatering skete når man pushede markdown ændringer.



Jeg prompted chatgpt med den information jeg har omkring dify og mit workflow på GitHub samt mine hugo filer. Den foreslog at lave et nyt workflow og bruge et python script til at sende min markdownfiler til deres api sådan at det bliver opdateret over I deres knowledge base. Udover det skrev den også at det ville være en god ide at for at få RAG-botten ind på selve hugo sitet så skal javascript koden placeres under layout/shortcodes/chat.

I løbet af klassen blev der nævnt at hvis man kun sender markdown så skal man skrælle noget af de shortcodes der findes inde i markdown væk, hvilket jeg ikke lige havde tænkt over.
Hvis man kun sender markdown filerne så mister botten også funktionen til at navigere rundt på sitet måske?

Mit site er så simpelt at det giver ikke mening at botten skal hjælpe med at navigere det, så jeg går med kun at den kun skal kunne kende til mine markdown filer. 

Jeg spurgte chatgpt om hvordan den ville fjerne eventuelle shortcodes I markdownfilerne. 


Min python fil startede som chatgpt har designet, startede den ud som at den kun skulle køres når der blev trykket med en knap for at teste om der var forbindelse til Dify api'et. 

on:
  workflow_dispatch: 

Det er blevet ændret til 

on:
  push:
    branches:
      - main
    paths:
      - "content/**/*.md"

det vil altså sige at, det her workflow starter når noget fra content mappen bliver ændret og pushet i main. Det bruger vi I stedet fordi, vi har adgang til:

- name: Find changed Markdown files
        if: github.event_name == 'push'
        run: |
          git diff --name-status \
            "${{ github.event.before }}" \
            "${{ github.sha }}" \
            -- 'content/**/*.md' \
            > changed_files.txt

          echo "Changed Markdown files:"
          cat changed_files.txt

Hvilket finder differencen, altså kun de filer der er blevet ændret. Det gør at jeg ikke løber ind i et rate limit, som jeg gjorde før hvor at den sendte alle filer, hver gang workflowet kørte. 

RAG'en har svært ved større spørgsmål som at opsummere henover flere dokumenter. Hvis jeg spørger den "The exam portfolio blog posts what reflections are in them?", så giver den mig et svagt svar fra de filer den nemmest lige kan finde frem tror jeg. Den kan godt give mig content fra specifikke md filer og skrive det ud til mig, så det er ikke et problem. Den citations den linker til er heller ikke akkurate overhovedet.