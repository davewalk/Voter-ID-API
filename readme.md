Voter ID API
============

This is a simple Voter ID API to be used by hackathons preceding and right after the 2012 U.S. Presidential Election.  More details coming soon!

Endpoints
=========

More to come, but for now:

### api.voterid2012.org/states

Returns all data for all states.

### api.voterid2012.org/states/{state name | state abbr}

Pass a state's name or two-letter abbreviation to get only data for that state.

### api.voterid2012.org/states?require={id | photo | strict}

Returns the state's that require the parameter passed.  See above for definitions (coming soon).

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

If you would like to help, please email or tweet below or come out to the [Hacks for Democracy]("http://www.azavea.com/a/hacks-for-democracy" "Hacks for Democracy hackathon") hackathon!  Thx!

About
=====

This API was created in early September by Dave Walk ([@ddw17]("http://www.twitter.com/ddw17" "ddw17 on Twitter")) originally for the the [Hacks for Democracy]("http://www.azavea.com/a/hacks-for-democracy" "Hacks for Democracy hackathon") hackathon in Philadelphia.  It's a simple Flask app exposing a MongoDB instance on Heroku being served by Gunicorn.

Contact
=======

If you have any questions, issues, requests, etc., please open an issue or email Dave at [daviddwalk@gmail.com]("mailto:daviddwalk@gmail.com" "Email Dave").  You can follow along to updates on Twitter at [@voteridapi]("http://www.twitter.com/voteridapi" "@VoterIDAPI on Twitter")
