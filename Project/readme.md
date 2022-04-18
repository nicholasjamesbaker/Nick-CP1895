# Recipe Flask App

## Installation

Open the hello.py in an IDE of your choice.

Open the Terminal and cd to the correct directory

When you reach project, you must arm the hello file:

```
$env:FLASK_APP = "hello"
```

From there you run Flask

```
python - m flask run
```

Once this is done, you copy your local URL into the browser!

That is it!

### Notes

I know this doesn't amount to much, but I had an incredibly difficult time with this project.
Starting from uploading and displaying images. I troubleshooted for hours but could not make it work with my program.
I think the main issue was writing a lot in JS and not referencing it in Python. I did not know
how to access static files within the list elements I created in my JS file. This was incredibly frustrating.
From there I moved on to try to implement the login system. I absolutely could not get python-sqlalchemy to install
for the registration element of the process. I spent countless hours trying to debug this, yet to just remove it from the system.
The last issue was with AWS. Of course this would be too difficult as well. I registered with my credit card to get my own
EC2 instance, so I didn't have to run it through the tutorial. I managed to host a default index through 
/var/www/html -- however, I could not link my Flask app through this no matter how much I tried. Again, countless hours of debugging
and a million command line inputs in putty, to amount to nothing. I am very displeased with my work, there are a lot of issues
I absolutely could not figure out how to fix. Thanks. - Nick
