# Project: Review Collector - Author: Enda Monks - Date of Completion: 2022-09-??
# -------------------------------------------------------------------------------
# Milestone 2 - Instantiate connect to elastic search collection via .env file
#             - Prompt user to send data to collection
#             - Load Album data from locally stored JSON file   (loop starts here)
#             - *Try* to POST each collection of json objects to database, *catch* errors
#             - Display success message                         (loop ends here)
# -------------------------------------------------------------------------------

# Tasker Notes:----------------------------------------------------------------------------------
# secret values store in .env get "client = elasticbud.client.get_elasticsearch_client()" to work
# use same username and password to log in to browser based visualization app that sits on top of 
# Elasticsearch (called Kibana), here: https://kibana.ialcloud.xyz

# Random ElasticBud Notes:-----------------------------------------------------------------------
# index_to_elasticsearch func from elasticsearch library https://github.com/z-tasker/elasticbud/blob/bd539e2df4671a762b0f8fd7dce2d922e990174b/tests/test_integration_flow.py#L53
# get_elasticsearch_client func <...client.py>
# line 133 https://github.com/z-tasker/elasticbud/blob/bd539e2df4671a762b0f8fd7dce2d922e990174b/elasticbud/elasticsearch.py
# all https://github.com/z-tasker/elasticbud/blob/bd539e2df4671a762b0f8fd7dce2d922e990174b/elasticbud/client.py 
# -----------------------------------------------------------------------------------------------

