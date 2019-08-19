# Blue Hills, MA Climate Data
## What is this project?
As one of the oldest weather stations in the nation, the Blue Hills climate data can tell us a lot about the patterns and the changes in New England weather. This collection of data was taken from the NOAA API using the Insomnia REST client, focusing on monthly data from the last 100 years. By sifting through this information, we can get insight on temperature extremes, average amounts of snow, and much more.  

## What technology does this use? And why?
Similarly to my planetary atmospheres project, which you can see [here](https://github.com/eliza-jane/dashing-planets), I used Plotly Dash. I chose Plotly Dash as it is in an accessible, readable language (Python) and because it also utilizes ReactJS.

## How do I look at the data?
* Clone the repo to your machine.
* If you have a Mac, you can run the code quickly with this: `python app.py` in your terminal, and then copy the local server address it provides you when it boots up. For a Windows machine, follow the link provided [here](http://pythoncentral.io/execute-python-script-file-shell/).

**Note**: If you brew Python, you might need to use `python2` or `python3` instead of just `python` depending on how you've set up your dev environment. You may also have to make sure you have the appropriate packages installed (see `requirements.txt`).