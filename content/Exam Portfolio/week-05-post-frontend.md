+++
date = '2026-06-04T17:06:24+01:00'
draft = false
title = 'Week 05+ post frontend'
+++

The week's work:

During this week I implemented a ranking system for my searchbar so that it knows what to display at the top of my content box. Initially I had a problem where it wouldn't rank the items after pressing my sort by newest button, but that is fixed now.

On the create item page I made dropdowns for status, condition and type, which makes it more user friendly to use. The user has no idea what my enums are.

On the item page where the items are displayed, there is now both an edit and a delete button for every item. When the edit button is pressed, it displays a pop-up window where you can change the information of the item with a done or cancel button. The delete button just deletes.

The book page is now functioning. The search function works and book choices are now being displayed. I had to make a new method on my backend called handleSearchBooks. The function takes the input keyword from the user, checks if it is null or blank, and if not, then it runs my BookService method that I made earlier. That method sends a request to the external API and returns a list in the form of a DTO response. That DTO response is then sent back as JSON. That JSON is now utilized by my frontend.

When you press choose on one of the displayed book items, you are taken to the item creation page where you finish the remaining needed information in order to create the item/book.

I have made an Enumformat function that formats the enums from the backend into something more pleasing for the eyes on the item page.

I fixed a backend issue where users could be created without username, email and password. The issue was that my backend didn't have a check for a blank post request.

I have split some of my item page up. I have made EditItemPopup and ItemCard. The EditItemPopup handles the popup that you get when you click edit, and it handles the submitting and cancelling. ItemCard's main job is just to display the items in the collection. This means that ItemCard is used inside a map function where I send the necessary props to the React component. The two newer components still use the CSS file for Itempage. This means that Itempage is now responsible for the state and the API calls.

I have refactored the way I send messages to the user via the frontend. Instead of inconsistent use of error and success messages, it is now more organized. If there is no error message or success message, then I have replaced it with a navigate so it feels like a natural success.

During deployment I had to open the roles of the admin register for a short while in order to create a functioning admin user.

While I tested my deployed frontend, I had lots of trouble with my server being overloaded and thus creating weird problems on my frontend in the browser. With the inspect tool open, it said it was a CORS problem, but it turned out to be that my server was so slow that it caused weird bugs. After stopping old projects on my droplet, everything seems to be working fine. I do still have one remaining bug that I can't immediately get rid of. The bug is that when I try to create a book using my external API, once I press done, it fails to fetch the items in the collection that I had been redirected to. If I then create a "normal" item and press done, then the fetching of items in the collection happens without error.

Thoughts and reflections:

During the work on the book creation page, I had to change the route to include the collectionId because of the same problem with the item creation page. It needs to know the collection, so that the user doesn't have to fill that information out manually in the form. I find this to be the better design choice.

I mentioned in the previous week that I had made a searching/ranking system or function for my search bar that was initially placed in the apiFacade.js file, but I have decided to make a utils folder and place it in a new file there. This is the same for the Enumformat function, which formats the enum into something more pleasing on the item page.

With the work on the book creation page, after you have chosen a displayed book choice, you have to fill out the remaining needed item information. My first thought was to just make it preset to something and then the user could edit the information afterwards on the item page.






