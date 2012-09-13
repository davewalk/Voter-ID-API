Voter ID API
============

This is a simple Voter ID API to be used by hackathons preceding and right after the 2012 U.S. Presidential Election.  More details coming soon!

Data
====

Here is a breakdown of the data that this API currently serves up.

###State Info
* Name, abbreviation, capital name, and 2011 population, taken from Wikpedia.  Thx, Wikipedia!

###Voting Details
(All information taken from the [National Conference of State Legislatures website](http://www.ncsl.org/legislatures-elections/elections/voter-id.aspx#Details))
* **Strict**: According to the NCSL website, strict means that "a voter cannot cast a ballot without first presenting ID."
* **Non-Strict**: Without an ID, voters "may be permitted to sign an affidavit of identity, or poll workers may be able to vouch for them personally."

The `reg_link` field includes the URL to the specific voter ID requirements for each state from the awesome [Cost of Freedom app](http://www.costoffreedom.info)

[Want to help add new data?](#want-to-help)

[Download a .csv here](/tree/master/data/states.csv).

Endpoints
=========

More to come, but for now:

### api.voterid2012.org/states

Returns all data for all states:

    {
        "results": [  
            {  
                "info": {  
                    "pop2011": 4802740,  
                    "capital": "Montgomery",  
                    "votes": 9,
                    "abbr": "AL
                    "},
                "vote": {
                    "strict": false,
                    "photo": false,
                    "id": true,
                    "reg_link": "http://www.costoffreedom.info/state/AL"
                }, 
                "name": "Alabama"
            },
            {
                "info": {"
                    "pop2011": 722718,
                    "capital": "Juneau",
                    "votes": 3,
                    "abbr": "AK"
            },
                "vote": {
                    "strict": false,
                    "photo": false,
                    "id": true,
                    "reg_link": "http://www.costoffreedom.info/state/AK"
                },
                "name": "Alaska"
            },
            ... 

### api.voterid2012.org/states/{state name | state abbr}

Pass a state's name or two-letter abbreviation to get only data for that state.

### api.voterid2012.org/states?require={id | photo | strict}

Returns the state's that require the parameter passed.

JSONP is supported:

### api.voterid2012.org/states?callback={callback}

Want to help?
=============

Whew, glad you're here, this project could use a lot of help!

### 1. More data 
More data is the top priority as what is available here is only intended as a start.  Here are few things that I think would be good to include:

* **Date of voter id change**.  This is vital, but requires some research.  I haven't been able to find one source that compiled this information in an easy format.  I think it's also open to discussion on what this date should pertain to
* **Current and past governors party affiliation per state**
* **Current and past state senate majority party per state**
* **Past Presidential results per state (2000-2008?)**
* **Whatever else folks find useful!**

### 2. Feedback
Is this API useful to developers?  Can it be improved?  Is there something that should be included?

### 3. A Website
A face that communicates what the API is better than a Github readme would be awesome

### 4. A Logo
Because I'm awful with Photoshop.

If you would like to help, please email or tweet below or come out to the [Hacks for Democracy](http://www.azavea.com/a/hacks-for-democracy "Hacks for Democracy hackathon") hackathon!  Thx!

More info
=========

Feel free to submit a pull request to add more!

[Cost of Freedom](http://www.costoffreedom.info)

About
=====

This API was created in early September by Dave Walk ([@ddw17](http://www.twitter.com/ddw17 "ddw17 on Twitter")) originally for the the [Hacks for Democracy](http://www.azavea.com/a/hacks-for-democracy "Hacks for Democracy hackathon") hackathon in Philadelphia.  

Contact
=======

If you have any questions, issues, requests, etc., please open an issue or email Dave at [daviddwalk@gmail.com](mailto:daviddwalk@gmail.com "Email Dave").  You can follow along to updates on Twitter at [@voteridapi](http://www.twitter.com/voteridapi "@VoterIDAPI on Twitter")
