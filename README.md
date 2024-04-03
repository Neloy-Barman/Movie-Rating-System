<h1>Movie Rating System</h1>


<h2>Project Development Journal</h2>


<h3><code style="color:blue">Assumptions</code></h3>
<ul>
    <li><strong>A SQL database is already created by an admin.</strong></li>
    <li><strong>The database is deployed on a cloud service server.</strong></li>
    <li><strong>The admin already added some data to the database.</strong></li>
    <li><strong>The operations are designed based on the user-side viewpoint.</strong></li>
    <li><strong>Only the logged in users can perform the operations.</strong></li>
    <li><strong>Unregistered users can't view or perform operations.</strong></li>
    <li><strong>For the limitations in the mentioned requirements, only the selected tasks are designed.</strong></li>
</ul>

<h3><code style="color:blue">How to use</code></h3>

1. <strong>Clone the repo</strong>
```
git clone https://github.com/Neloy-Barman/Movie-Rating-System.git
```
2. Create & activate virtual Environment
```
virtualenv --no-site-packages venv
source venv/bin/activate
``` 
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
flask run 
or 
python app.py 
```

