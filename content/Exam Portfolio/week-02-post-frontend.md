+++
date = '2026-05-03T17:06:24+01:00'
draft = false
title = 'Week 02 post frontend'
+++

The weeks work:

This week I started creating React components based on the structure I had planned for the project. I placed my reusable components in a general components folder.

Some of the components I created were:

- GeneralButton.jsx
- Homesection.jsx
- ImagePlaceholder.jsx
- LoginCredentialBox.jsx
- Navbar.jsx

I started with the components I expected to reuse in multiple places. At first, I tried to make some of them quite generic. For example, my GeneralButton component took text and showIcon as props:

function GeneralButton({ text, showIcon = false })

I also created a pages folder. This folder holds the larger page components that are responsible for combining smaller components. For example, Homepage.jsx uses multiple smaller components such as Homesection.jsx.

Later, I realized that some of my components were too generic. I expected to reuse the same building blocks more than I actually did. Because of that, I changed some of the smaller components so they better fit the specific pages where they are used.

I also got multiple views working by using React Router.


Thoughts and reflections:

After a meeting with Thomas, I realized that I still needed App.jsx to hold all of my routes and pages. Then only App.jsx should be rendered inside main.jsx.

I also learned that React Router is needed to create the feeling of multiple pages in a single-page application.

The main takeaway from this week was that it is not always best to make components too generic from the beginning. Sometimes it is better to first build the specific pages and then refactor repeated patterns into reusable components afterwards.