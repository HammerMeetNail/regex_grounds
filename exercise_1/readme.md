Add baby names from Social Security Card Applications-National Level Data to MongoDB. Parses 134 years of data and adds
to the collection in the following format:

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

/names directory is pulled from:

https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data

HOW TO RUN
Navigate to regex_grounds and execute the following:

python exercise_1/add_to_mongo.py 

REQUIREMENTS
1) Make sure MongoDB is running on localhost
2) Run pip install -r requirements.txt to install relevant modules

