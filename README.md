# Brewnotes -- a demonstration project

I find that in software development, _patterns_ are more important than specific implementations. That said, it's often nice to have a reference implementation for different patterns. In this project, I'm taking the same sample application, and implementing it in various ways. This serves a few different purposes:
- It gives me a chance to practice implementing the same pattern in different languages, honing both my understanding of the pattern and the language I'm doing the implementation in
- It serves as a reference I can easily look up, rather than trying to re-create something I know I did once upon a time for some project back in the day
- It gives me the chance to experiment with different patterns and technologies, and in doing so support both the previous points

The application I'm implementing in this project I've called _Brewnotes -- beers to try and beers I've tried_. It's a browsable and searchable catalog of beers, from which I create a personal library of beers I've tried and add notes. Basically, it's an app that let's me try out different styles of beer and serve as a reference for styles I've tried, which through building it let's me try out different software patterns and technologies and server as a reference for patterns and technologies I've tried...

## Content and Data

In any application, I believe it's important to start with the content. While programming is about looking for patterns that are generally applicable and then getting computers to apply them, no use case is indefinitely generic -- it actually does matter what kind of content you're working with, and what you intend to do with it.

In this case, I'm grounding my application on data from the [Open Beer Database](http://openbeerdb.com/). Although now defunct, when running it provided a database describing beers, noting their breweries, and categorizing the beers by style.

This type of content naturally lends itself to both browsing and searching. That can already be pretty useful. Letting users create their own personal subset -- eg a "library" or "my collections" can add more value still. I've seen these two complementary use cases broadly termed "discovery" and "private curation." Both can get fairly complex. Take, for example, all the investment in machine learning happening in the "discovery" use case -- for instance improving search results, or personalized music or video recommendations.

In this project, I'm keeping things a lot simpler. The data set is finite, and falls along pre-existing, fairly cleanly delineated attributes -- ie while it's possible to get into fun argument over whether a given beer fits into a particular style or not, beer styles are sufficiently well-defined that it makes sense to filter and search on them.

### Persistence Layer

  The database was originally stored in MySQL, with the following tables:
- beers
- breweries
- categories
- styles
- geocodes

Although the database is no longer maintained, its creator has provided links to download the data as SQL and also in CSV format. Poking around in the CSV quickly reveals various challenges, as CSV's tend to do -- records with new lines in the middle of the description fields, too many commas, inconsistent number of columns per row, etc. Rather than spend time cleaning this up, it's easier to just fire up a MySQL database and run the provided SQL to recreate the tables. From there, I can either just use MySQL as the persistence layer (which I will in my initial implementation of the app), or export from there and import into some other persistence layer technology (which I do in later implementation variations).

## UI


