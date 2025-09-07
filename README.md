# Portfolio Website Deployment on AWS EC2

## Table of Contents
- [Project Overview](#project-overview)
- [Architecture Diagram](#architecture-diagram)
- [Deployment Steps](#deployment-steps)
- [Technologies Used](#technologies-used)
- [Screenshots](##screenshots)
- [Learnings](#learnings)


## Project Overview
The project demonstrates how to host a secure, production-ready website on AWS. Key responsibilities included:
- Provisioning an **EC2 instance** for hosting.
- Installing and configuring **Nginx** as a reverse proxy.
- Securing the website with **Let’s Encrypt SSL certificates**.
- Managing domain DNS settings for a custom domain using **Cloudflare**.
- Leveraging **Bash** scripting for automating new changes to the site. 
- Ensuring website availability and uptime using **Lambda** and **EventBridge**.

## Architecture Diagram
-- add here 

**Description** 
- Visitors access the portfolio website through a custom domain.
- Requests hit the EC2 instance, which serves content via Nginx.
- Let’s Encrypt provides HTTPS for secure communication.

## Technologies used
- **AWS EC2**, t3.micro – Virtual server hosting
- **Elastic IP** - To assign a static IP to the instance
- **Cloufare** - DNS domain registar for my custom domain records
- **Nginx** – Web server and reverse proxy
- **Let’s Encrypt** – Free SSL certificates
- **Bash** – Basic automation for setup
- **Loveable AI** – Original website creation

## Deployment Steps
1.  Purchased a custom domain name from **Names.co.uk** and transferred the domain to **Cloudfare.com** with its dedicated DNS records. 
1.1. Ensured to remove old previous DNS providers NS records to avoid DNS conflicts. 
2.  Launched EC2 and securely stored Public Key certificate (.pem) in a S3 bucket. 
3.  Configured network security groups for inbound traffic through 443 (HTTPS) and 80 (HTTP). 
4. Installed and checked status of Nginx in the instance as follow: 
```sh
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemclt status nginx 
```
4.1 Created a new server blocked , enabled it using hard links and tested connection
```sh
sudo nano /etc/nginx/sites-available/stanagh
sudo ln -s /etc/nginx/sites-available/stanagh.com /etc/nginx/sites-enabled/ 
sudo nginx -t
sudo systemctl reload nginx
```
4.2 Added website content under path below: 
```sh
/var/www/stanagh.com
```
4.3. Cloned repo into the new created directory and assigned permission
```sh 
sudo git clone https://<username>:<token>@github.com/<username>/<repo>.git        potfolio-website
sudo chown -R ubuntu:ubuntu potfolio-website
```
4.4 Built the project by installing dependencies
```sh
cd potfolio-website
npm install
npm run build 
```

5. Set up Let’s Encrypt SSL certificates.
```sh 
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
```
5.1 Ran Certbot with Nginx plugin
```sh 
sudo certbot --nginx -d stanagh.com -d www.stanagh.com
```
6. Configured Lambda and EventBridge automate the start & stop time of the EC2 instance. Screenshot are available in the [`deployment/`](deployment/) folder. Steps are as follows: 
6.1 Created a IAM policy that defined operation to run on the EC2 instance. 
6.2 Assigned the policy to Lambda AWS service. 
6.3 Created Python script to manage the EC2 instances.
    6.4 Added EventBridge as a trigger, with a defined JSON function to stop the instance based on a CRON daily time schedule.  

## Screenshots
![Homepage](screenshots/homepage.png)

## Troubleshooting steps 
dig - Looks up DNS records to see what IP address a domain points to
```sh
dig stanagh.com
```

nslookup - Similar to dig, finds IP addresses for domain names (used on my Windows OS)
```cmd 
nslookup -type=ns stanagh.com
```

curl -vk - Downloads web content with verbose output, ignoring SSL certificate errors
```sh
curl -vk https://stanagh.com
```






