# Documentation

## Summary

Hello to you, dear anonymous reviewer! I wrote a short documentation to help you understand the structure of my code and thinking. Please read the first sections before looking at any code. You can check the last two sections, "Assumptions & Notes" and "Q&A" after reviewing my code.

**File structure**:

* The description of my task can be found on the only pdf file in the main directory
* I left a copy of the sqlite database file in the main directory
* The folder `air_quality` contains all the source code of my solution
* The data was downloaded and stored in the `raw_data` folder
* The two jupyter notebooks just contain tests and draft code. You don't necessarily have to check those. I left them there, should you wish to see my trail of thoughts and reasoning behind the code (arguably not always straightforward)
* In the `data_reports` folder, you can find some data reports I produced to try and understand the data. They are in the form of HTML files which you can open in a browser (or via the live server extension, should you use VS code)
* All the code linked to the processing of the data can be found in the `pipeline.py` file
* If you want to launch the pipeline, all you need to do is run the `main.py` file

## Why are there multiple folders?

I understand that the folder structure might, at first sight, seem unnecessarily complex. The reason why I structured my code like this is to have a layered approach to dealing with the data and handle the interactions between the data and the database. I originally wanted to show off by serving the data through an API but after second thought, this approach would be a bit out of scope. However, should we want to build an API, the only thing left is a router layer. Happy to discuss this part in more detail, should the opportunity be given.

## Why are there only two indicators?

As you will see, the end results contain data for only two indicators. This is because after filtering the data according to contrains of the task description, these are the only ones left. It could very well be that I have missed something and that is the reason why this happens. Given more time, I could have investigated this further.

See the next section for more details on my assumptions.

## Assumptions & Notes

* I can only use the data where the value of `averagingPeriod_value` is `24`  if I want to have the 24 hour rolling average. I could have computed it with the other averaging types data as well but when I filter the countries and indices we are interested in, I only have data for 1 day (<24 hours) making it imposible for this specific use-case to calculate the 24 hours rolling average (unless I missed something).
* I am assuming that all negative observations are invalid for simplicity. I normally would have digged into the API docs to figure it out or asked someone who had treated this kind of data before.
* I am assuming that we want all values expressed as μg/m3. I googled a formula to convert but not sure if this is the correct one. (PS: in the end, I didn't have to use it because after filtering I only have μg/m3 units).
* I am assuming that we want one observation per city so for cities with more than one location, I take the average.

## Potential extentions and improvements

* Develop a better structure for the DB optimised for specific use cases. For example, organising the data using a snowflake schema with several dimention tables to capture metadata details and specific aggregated views optimised for analytics and reporting.
* Serve the data through an API (FAST API is very good for this kind of things)
* Add more data cleaning and validation based on business and logical rules.
* Add another layer of abstraction to decouple the DB layer from the operations layer making it easy to switch between different types of databases. This could be achieved for example with the use of protocol classes in `Python`.
* Refactor the code focusing on design principles so it is for example easy to maintain, easy to change and easy to understand.
* Make a more robust pipeline that is capable of handling bigger datasets and add a scheduler. This could be done for example with technologies like Airflow and PySpark.
* Connect the pipeline to the API.

## Q&A

**Why did you use python?**

This was just personal preference, it is the language that I am most comfortable with at this moment.

**Why did you go for an SQL DB?**

No specific reason since I am not sure what kind of use this DB will serve. I was aware of SQLAlchemy in Python but I had never used it before so I thought it would be an interesting opportunity to learn it. At my current job we use `MongoDB` through `Mongonegine` because it is easier for us to use it with ElasticSearch.

**Why sqlite?**

Easy portability and reproductivity.
