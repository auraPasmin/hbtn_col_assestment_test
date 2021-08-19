# Orders app


### REQUIREMENTS
To use the Application execute the next commands
<ol>
	<li><code>cat user_and_db.sql | sudo mysql -u root -p</code></li>
	<li><code>mysql -uroot -p orders < exported.sql</code></li>
	<li><code>sudo apt-update</code></li>
	<li><code>sudo apt-get install libmysqlclient-dev</code></li>
	<li><code>pip3 install -r requirements.txt</code></li>
</ol>


"activa el env"
source env/bin/activate
"instala las cositas""

pip install -r requirements.txt

FLASK_ENV=development flask run

### HOW TO USE
Execute the next commands to run the Application
<ol>
	<li><code>python3 api/v1/app.py</code></li>
	<li><code>python3 frontend/app.py</code></li>
</ol>

Then on your browser go to http://localhost:8000 and now you can use the Application.


### 🌼Authors🌼
* Aura Pasmin | [GitHub](https://github.com/auraPasmin) |

### Creator of the hbtn assessment test💻👨‍💻
* Carlos Cárdenas | [GitHub](https://github.com/carcagi) |
