# Documentation

## Summary

Hello dear anonymous reviewer! I made a short documentation to help you understand the structure of my code and thinking. I would advice you to read most of it before looking at any code. You can leave the last two sections, "Assumptions & Notes" and "Q&A" for after you have had a look at my code.

**File structure**:

* The description of my task can be found on the only pdf file in the main directory
* I left a copy of the sqlite database file in the main directory
* The folder `air_quality` contains all the source code for my solution.
* The two jupyter notebooks just contain tests and draft code. You don't have to check those necessarily. I left them there in case you wanted to see my trail of thoughts and reasoning (arguably not always straightforward)
* In the `data_reports` folder you can find some data reports I produced to try and understand the data. They are in the form of HTML files which you can open in a browser (or via the live server externsion if you are using VS code)
* All the code linked to the processing of the data can be found in the `pipeline.py` file
* If you want to launch the pipeline all you need to do is run the `main.py` file

## Why are there so many folders?

I understand that the folder structure might, on first sight, seem unnecessarily complex. The reason why I structured my code like this is to have a layered approach to dealing with the data and handle the interactions between the data and the database. Also this is because I originally wanted to show off by serving the data through an api but I later thought it would be a bit out of scope. But should we want to build an api, the only thing left is a router layer. Happy to discuss this part in more detail should the opportunity be given.


## Why are there only two indicators?

As you will see, the end results contain data for only two indicators this is because after filtering the data according to contrains of the task description, that is the only thing I have left. It could very well be that I have missed something and that is why this happens. Given more time I would have investigated this further.

See the next section for more details on my assumptions.


## Assumptions & Notes

* I can only use the data where the value of `averagingPeriod_value` is `24`  if I want to have the 24 hour roling average. I could have computed it it with the other averaging types data as well but when I filter for the countries and indices we are interested in I only have data for 1 day (<24 hours) making it imposible for this specific use-case to calculate the 24 hours roling average (unless I missed something).
* I am assuming that all negative observations are invalid for simplicity. Normally I would have digged into the API docs to figure it out or asked someone who had treated with this kind of data before.
* I am assuming that we want all values expressed as μg/m3. I googled a formula to convert but not sure if this is the correct one. (PS: int the end I won't need to use it because after filtering I only have μg/m3 units)


## Potential extentions and improvements

* Develop a better structure for the DB optimised for specific use cases. For example, organising the data using a snowflake schema with several dimention tables to capture metadata details and specific aggregated views optimised for analytics and reporting
* Serve the data through an API (FAST API is very good for this kind of things)
* Add more data cleaning and validation based based on bussiness and logical rules.
* Add another layer of abstraction to decouple the DB layer from the operations layer making it easy to switch between different types of databases. This could be achieved for example with the use of protocol classes in `Python`.
* Refactor the code focusing on design principles so it is for example easy to maintain, easy to change and easy to understand.


## Q&A

**Why did you use python?**

This was just personal preference, it is the language that I am most comfortable with at this moment.


**Why did you go for an SQL DB?**

No specific reason since I am not sure what kind of use this DB will serve. I was aware of SQLAlchemy in Python but I had never used it before so I thought it would be an interesting opportunity to learn it. At my current job we use `MongoDB` through `Mongonegine` because it is easier for us to use it with ElasticSearch.


**Why sqlite?**

Easy of portability and reproducability.
