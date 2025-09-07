#!/bin/bash
set -e  # stop if any command fails
APP_DIR="/var/www/stanagh.com/potfolio-website"
WEB_ROOT="/var/www/stanagh.com/html"
echo "Pulling latest changes from GitHub..."
cd $APP_DIR
git pull
echo "Installing dependencies"
npm install
echo "Building project..."
npm run build
echo "Deploying build to NGINX web root..."
sudo rm -rf $WEB_ROOT/*
sudo cp -r dist/* $WEB_ROOT/
echo "Reloading NGINX..."
sudo systemctl reload nginx
echo "Deployment complete! Visit http://stanagh.com"