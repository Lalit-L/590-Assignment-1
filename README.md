Lalit Lakamsani

This is my submission for Assignment 1 for CYBERSEC 590

My application is called Bug Fixer. It takes in code, and uses the model to find the errors (if any) in the code and outputs the fix for them, and what was wrong with the code to begin with

**To run it:**

Clone the git repository
Copy the .env.example file into a file called .env

Edit the .env file to add your personal AI Gateway key

Run: sudo docker build -t bug-fixer .
  - This builds the docker image

Run: sudo docker run -it --rm --env-file .env bug-fixer
  - This runs the docker

**When Running:**
  - Type/paste any code you would like
  - Once done, press enter and type END on the newline, by itself
  - Press enter again, and wait for the model to run
