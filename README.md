# Python script scheduling on Heroku

This is a template repository for deploying and schedule a Python script on Heroku.

## How to
* Fork this repository, then:
	* set your Python version in `runtime.txt` (e.g. `python-3.6.8`)
	* implement your script into `script.py` *main* function 
	* add your requirements in `requirements.txt`
* Create new Heroku Application, then:
	* In *Settings > Buildpacks > Add buildpack*, select **python**
	* In *Settings > Config Vars > Add*, add a new variable named `CRON_SCHEDULE`, valued with a valid cron string (build your string [here](https://crontab.guru/))
	* In *Deploy > Deployment method*, choose GitHub, connect Heroku with your GitHub account, then select your forked repository
	* In *Deploy > Automatic deploys* click **Enable Automatic Deploys** to have your application automatically deployed at every pushed commit.
* [Download and install]([https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)) Heroku CLI, open your terminal, then:
	* login Heroku CLI via `heroku login`
	* Set Heroku clock dyno type via `heroku ps:scale -a <HEROKU_APP_NAME> clock=1`
	* Display application logs via `heroku logs -a <HEROKU_APP_NAME>`
	* Wait for your scheduled script to start and check the log if it's working correctly.