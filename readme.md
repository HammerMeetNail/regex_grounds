This is an in progress collection of exercises for improving knowledge of regular expressions.
----------------------------------------------------------------------------------------------

**Table of Contents**

- [exercise_1](https://github.com/DJO3/regex_grounds/blob/master/readme.md#exercise_1)
- [exercise_2](https://github.com/DJO3/regex_grounds/blob/master/readme.md#exercise_2)


# exercise_1
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


# exercise_2
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


