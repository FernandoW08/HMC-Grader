import os
basedir = os.path.abspath(os.path.dirname(__file__))

#
# Settings for WTForms
#
CSRF_ENABLES=True
SECRET_KEY="Grutors <3 SPAM"


#Mongo settings
MONGODB_SETTINGS = {'DB': 'submissionsite'}

DATABASE_QUERY_TIMEOUT = 0.5

#
# Settings for file storage
#
STORAGE_HOME="/home/plenk/GroodyGrader"
