+++
date = '2026-04-04T16:23:24+02:00'
draft = false
title = 'Week 03 post'
+++

In the third week of the project:

I have created a Book entity, BookDAO, BookDTO, OpenLibraryDTOresponse, and BookService.

Book entity and BookDAO have just been created, I haven't done anything with them yet.
I focused on using and making sure that my BookDTO, OpenLibraryDTOresponse, and BookService are working before I even proceed to map anything to the database.
I have made the methods inside the BookService static for now, so you need to call the class and then the method to use it. I'm using the OpenLibraryDTOresponse as a wrapper to get what is inside "docs", which is an array in the JSON response. Below is the code for OpenLibraryDTOresponse:

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class BookDTO {

    @JsonProperty("title")
    private String title;
    @JsonProperty("author_name")
    private List<String> author;
    @JsonProperty("first_publish_year")
    private int publish_year;

}

For now, it is possible to get a List as a response, now I'm just missing the part where it maps to the user and the database.


Thoughts, ideas, and reflections from the third week:

So I have decided on using the Open Library API, which is an API that is connected to a big book database. I thought it would be a great starting point to bring API into my project.
I will have books integrated into my collection application since, in my opinion, it's quite an area or field that is highly collected. I chose to go with Open Library books since it was literally the first thing I stumbled upon when looking up APIs, and it is free to use. My idea with this API is that the User will be able to put in a book with the ISBN number or the title of the book, and then my code should do the rest of the work with filling out the information needed to create the item. Those are my initial thoughts (might change).

I have a problem regarding ISBN because of the API I'm using. When searching for a book on a keyword, it will produce a result which has 4 ISBNs, and I don't know what is correct and what isn't. So I'm thinking of not using the ISBN in my work. I don't even know if it's relevant to store for me.

I have created a book entity which will have its own database table. I think that is the cleanest way of going about this. It will take more time, but it will be a better way of storing the data, in my opinion.

I now have access to the API and can receive data. I switched which method I wanted to start with to one where the User can search on a keyword, for example, "Harry Potter", and then it will provide a list of 10 results, and the user will then be able to choose which one it is they have, and then it will be placed in the database.