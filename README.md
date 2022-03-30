## General summary of the project ## 

In this project, I built a website that display a simple report of the hashes by querying VirusTotal's public API. The result of hashes will be stored in JSON file and it converts to HTML table format. The application is containerized with Dockerfile so when you build docker image, required dependencies will be installed automatically. You can just follow 2 commands to start the application and execute container to generate more hash input.

## How to run the project ##

Review Dockerfile and select input file and API key before building docker image

Build Dockerfile:

    docker build -t virustotal:latest .

Run Docker container:

    docker run -d -p 5000:5000 virustotal:latest

Running script example:

    docker exec -it <<container_id>> python3 virustotal-search.py -k a3a7c3343f9df2af23b0670af1c8f38b823de2aca940f6417da15c6fd63be9cc -i sample_hash_input.txt

Quick script test example:

    docker exec -it <<container_id>> python3 virustotal-search.py -k a3a7c3343f9df2af23b0670af1c8f38b823de2aca940f6417da15c6fd63be9cc -i quick_hash_input.txt

After hash values are scaned, HTML file will be generated and Flask on port 5000 should be running.

## Demo Video ##

I will set up a demo system accessible from AWS by tomorrow 11AM


## technology stack ## 

Linux, Python, Docker, Terraform


## issues encountered ##

I waste too much time to display HTML table on website because I used inappropriate tool (React). I found Flask would be greate to display simple HTML table and it worked.
I am able to store Virustotal's results locally but wasn't able to filter same hash value which is scaned within 1 day.