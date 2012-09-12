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

About
=====

This API was created in early September by Dave Walk ([@ddw17]("http://www.twitter.com/ddw17" "ddw17 on Twitter")) originally for the the [Hacks for Democracy]("http://www.azavea.com/a/hacks-for-democracy" "Hacks for Democracy hackathon") hackathon in Philadelphia.  It's a simple Flask app exposing a MongoDB instance on Heroku being served by Gunicorn.

Contact
=======

If you have any questions, issues, requests, etc., please open an issue or email Dave at [daviddwalk@gmail.com]("mailto:daviddwalk@gmail.com" "Email Dave").  You can follow along to updates on Twitter at [@voteridapi]("http://www.twitter.com/voteridapi" "@VoterIDAPI on Twitter")
