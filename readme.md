This is an in progress collection of exercises for improving knowledge of regular expressions.
----------------------------------------------------------------------------------------------

EXERCISE_1
----------
Assemble 134 years of baby names pulled from Social Security Card Applications-National Level Data. The data is split by
year into 134 different text files and should be added to MongoDB in the following format:

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

HOW TO RUN
Navigate to regex_grounds and execute the following:

python exercise_1/add_to_mongo.py 

REQUIREMENTS
1) Make sure MongoDB is running on localhost
2) Run pip install -r requirements.txt to install relevant modules

MISC
/names directory is pulled from:
https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data
