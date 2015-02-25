# Question of the Day #

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Question of the Day</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/BruceEckel/Question-Of-The-Day/" property="cc:attributionName" rel="cc:attributionURL">https://github.com/BruceEckel/Question-Of-The-Day/</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



Getting Started with Python on Heroku
=====================================
(Adapted from [https://github.com/jamesward/hello-python-flask](https://github.com/jamesward/hello-python-flask))

First, make sure you have the latest version of **pip**:

		python -m pip install -U pip

Next, make sure you have virtualenv installed:

		virtualenv --version

If this gives you an error message, run:

		pip install virtualenv

Run Locally
-----------

1. Setup virtualenv

        virtualenv venv --distribute

2. Activate virtualenv:

    Mac/Linux:

		source venv/bin/activate

	Windows (you can also just type "go"):

        venv\Scripts\activate.bat

3. Get the deps:

        pip install -r requirements.txt

4. Start Flask Server

        python main.py

5. Test out the app

    [http://localhost:5000](http://localhost:5000)


Run on Heroku
-------------

1. Create the app

        heroku create -s cedar
 
2. Deploy the app

        git push heroku master

3. Open the app in your browser

        heroku open

### Nicer alternative: ###
Log onto Heroku.com, then follow the instructions to connect to your github repository and launch your app. This can include auto-deployment every time you update your Github repository!

Notes
-------------
* When you change **main.py**, Flask's automatic refresh doesn't work. You have to kill it and restart it to see the results. The refresh only seems to work on templates.

