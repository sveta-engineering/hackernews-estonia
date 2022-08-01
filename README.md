# Hackernews.ee

[hackernews.ee](hackernews.ee) is a space for the _Estonian_ startup ecosystem to discuss the latests news, find out about events, look for a job,...

Built using Django.

## TODO

- [x] Alignment issue on chrome?
- [ ] Calendar year change not working
- [ ] Collect sources (twitter, newsletters, events, jobs, ...)
- [ ] Comment 
  - [ ] Toggle view should collapse children as well

## Future improvements

- [ ] improve GUI ([vue js](https://v2.vuejs.org/v2/examples/hackernews.html))
- [ ] add webassembly "apps" page
  - [ ] WebRTC, WebGL, WebSockets ([tutorial](https://rustwasm.github.io/wasm-bindgen/examples/websockets.html))
  - [ ] Chatroom
  - [ ] Games ([examples](https://madewithwebassembly.com/))
  - [ ] Live video stream from Lift99?
- [ ] Add user profile country flags
- [ ] Add stats page 
  - [ ] Where users visit from
  - [ ] Registered users countries of origin
  - [ ] Daily number of unique visitors
- [ ] JobPost
  - [ ] Have a looking-for-a-job option
- [ ] Add profile links
- [ ] Sort news by
  - [ ] hot
  - [ ] top
  - [ ] new
- [ ] Upvoted arrows should be green
- [ ] News
  - [ ] Add pages


## Getting started

Follow these instructions to setup your development environment:

Create a virtual environment: `python3 -m venv env`

Activate virtual environment: `source env/bin/activate`

Install requirements: `pip3 install -r requirements.txt`

Run: `python3 manage.py runserver`

Website will be server on [`localhost`](http://127.0.0.1:8000/)

## Heroku

Create new app: `heroku create hackernews-estonia`

Push to Heroku: `git push heroku master`

`heroku run python ./manage.py migrate --run-syncdb`

Open: `heroku open`

Show domains: `heroku domains`

Add domain: `heroku domains:add www.hackernews.ee --app hackernews-estonia`

Remove domain: `heroku domains:remove hackernews.ee `

`heroku config:set DJANGO_SECRET_KEY=$$$`

`heroku config:set DJANGO_DEBUG=False `

## Links

[How Hacker News ranking algorithm works](https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d)

[How to create a calendar using Django](https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html)

[MDN: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)



