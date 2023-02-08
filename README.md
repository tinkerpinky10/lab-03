# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Karla Vasquez
- Gila Kohanbash

## Lab Question Answers

*Question 1: Why are RESTful APIs scalable?*

RESTful APIs are scalable because client-server interactions are optimized by REST (Representational State Transfer). Features such as removing server load when retaining prior client request information is unnecessary or caching support scalability. 

*Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?*
The resources the mail server is providing to clients consist of the following: list of dictionaries representing mail entries, saves the path of file of the mail, lets the client know whether the mail has been deleted, and gets the user’s sent email information. 

*Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?*

One common REST Method not used in our mail server is the PUT method. We could extend our mail server to use this method by creating a function that oversees whether an email has been sent or not. This could prevent the client from writing an email that has already been sent. 

*Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!*

API Keys are used for many RESTful APIs because it assigns a unique key to a first time client for. Although it does make it vulnerable, it provides project authorization and identification. Additionally, it rejects calls from projects not yet granted access, controls number of calls made to APIs, and blocks anonymous traffic. 

Source: 
https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API. 


...
