Lalit Lakamsani

**AI DISCLAIMER AT THE BOTTOM**

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


**AI USAGE**
  - ChatGPT (free version) was used to create an outline of the Dockerfile on September 12, 2026
    - I rewrote the Dockerfile/any errors in it by hand, choosing the files that needed to be copied into the docker by looking at error messages
  - ChatGPT (free version) was used to outline the .dockerignore file as well, on September 13, 2026
    - I modified the .dockerignore to follow much of the .gitignore, which was created from the machine
  - The idea to use a .env file was also from ChatGPT (free version) on September 5th, 2026
    - I modified the file, making sure it was properly usable. I also created the .env.example file to help users put their own info in 
  - The code was handwritten. I had most of the knowledge from the previous 520 Class
  - **No code was directly copied from the 520 class projects**
