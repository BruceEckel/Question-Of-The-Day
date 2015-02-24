# Question of the Day #

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Question of the Day</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/BruceEckel/Question-Of-The-Day/" property="cc:attributionName" rel="cc:attributionURL">https://github.com/BruceEckel/Question-Of-The-Day/</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



Getting Started with Python on Heroku
=====================================
(Adapted from [https://github.com/jamesward/hello-python-flask](https://github.com/jamesward/hello-python-flask))

Run Locally
-----------

1. Setup virtualenv

        virtualenv venv --distribute

2. Activate virtualenv:

        source venv/bin/activate

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

