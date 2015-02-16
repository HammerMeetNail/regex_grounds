This is an in progress collection of exercises for improving knowledge of regular expressions.
----------------------------------------------------------------------------------------------

**Table of Contents**

- [Exercise 1: Find Baby Names](#exercise-1---find-baby-names)
- [Exercise 2: Find Email Addresses](#exercise-2---find-email-addresses)
- [Exercise 3: Find Twitter Usernames](#exercise-3---find-twitter-usernames)


# Exercise 1 - Find Baby Names
Assemble 134 years of baby names pulled from Social Security Card Applications-National Level Data. The data is split by
year into 134 different text files and should be added to MongoDB in the following format:

```json
{
	"_id" : "1948",
	"info" : [
		{
			"name" : "Linda",
			"num_occurrence" : "96210",
			"sex" : "F"
		},
        {
			"name" : "Zell",
			"num_occurrence" : "5",
			"sex" : "M"
		}
	]
}
```

###### Basic Usage 
Navigate to regex_grounds and execute the following:

`python exercise_1/add_to_mongo.py`

###### Requirements  
1) Make sure MongoDB is running on localhost  
2) Run `pip install -r requirements.txt` to install relevant modules  

###### Misc  
/names directory is pulled from:  
https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data  


# Exercise 2 - Find Email Addresses
Parse https://www.data.gov/contact and return a list of all email addresses. Do not return any duplicates. 

###### Basic Usage 
Navigate to regex_grounds and execute the following:

`python exercise_2/find_addresses.py "url"`

Multiple urls are accepted and can be passed as such:

`python exercise_2/find_addresses.py "url" "url2" "url3"`

###### Requirements
1) Run `pip install -r requirements.txt` to install relevant modules

###### Misc
https://www.data.gov/contact should only return one email address.  
http://www.fightthescams.com/2014/12/04/fake-job-postings-on-craigslist/ should return 4498 email addresses.  


# Exercise 3 - Find Twitter Usernames
Take a look at at the Twitter username creation guidelines and return a list of all twitter usernames on the page.
 
https://support.twitter.com/articles/101299-why-can-t-i-register-certain-usernames

As in Exercise 2, do not return any duplicates.

###### Basic Usage 
Navigate to regex_grounds and execute the following:

`python exercise_3/find_usernames.py "url"`

Multiple urls are accepted and can be passed as such:

`python exercise_3/find_usernames.py "url" "url2" "url3"`

###### Requirements
1) Run `pip install -r requirements.txt` to install relevant modules

###### Misc
https://support.twitter.com/articles/101299-why-can-t-i-register-certain-usernames should return 4 usernames.
https://www.data.gov/contact should only return 5 usernames.

