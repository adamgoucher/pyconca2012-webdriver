### A Really, Really, Really, Fast Tour of WebDriver ###

Wow. 20 minute time slots are hard... so this repo illustrates the 3 things that I tried to hammer home in my talk at Pycon.ca.

1. _Use Page Objects!_ - There are a lot of examples (even in Python). This repo has one take on the pattern, but there are lots of other ones. Explore to find the that resonates most with you. And hen adapt it to your own needs.

2. _Javascript Executor_ - This is how we are going to have to automate the flood of JS Widgets and ... canvas. Ugh. Canvas. The cool thing about the executor is that it can take a WebDriver element as an argument and the 'right' thing happens to morph it to a native JS object. Get used to this folks...

3. _Proxy all the things_ - A good idea is to run your automation through a scriptable proxy to be able to do things like blacklist Facebook and Twitter integrations (and thus drastically improve the speed of your app)