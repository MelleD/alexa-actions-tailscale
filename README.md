# Alexa-actions with Tailscale

[alexa-actions](https://github.com/keatontaylor/alexa-actions) shipped in a docker image with [Tailscale](https://tailscale.com/)

It allows to use Alexa Smart Home Skill without exposing your Home Assistant instance to the internet (except <a href="user-content-account-linking">during setup</a> )

If you fork this repo and setup **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY** as Github encrypted secrets, a Github workflow will build and publish a docker image to your AWS ECR own account on eu-west-1 that you then can use for your "HomeAssistant-SmartHome" Lambda function

Currently it uses a fork of haaska in order to use environnment variables instead of the config.json for the home assistant url and token

**Requirement**: The [HA Tailscale Add-on](https://github.com/hassio-addons/addon-tailscale) installed and configured

The lambda function needs the 3 env vars:
- **HA_TOKEN**
- **HA_URL**
- **TAILSCALE_AUTHKEY** (see https://tailscale.com/kb/1113/aws-lambda/)