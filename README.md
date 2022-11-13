# Goldeneye Simulation

This is a simple web server written in Flask that is used to test the `goldeneye` tool. 

# Usage 

1. Go to the Web Server directory

```
cd '.\Web Server\'
```

2. Install the required packages

```
pip install -r requirements.txt
```

3. Run the flask app

```
python app.py
```

4. Run the goldeneye tool
```
./goldeneye.py http://172.19.22.25:8080/api/hit -w 4 -s 4 -m "random"
```

To test multi-processing, set `threaded` to `False` and set the `processes` parameter to the number of proccesses you want in the `app.run()` in *app.py* file.




