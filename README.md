# Telegram PDF Bot 

[![Typing SVG](https://mdtype.herokuapp.com?font=Righteous&color=253AF7&size=31&center=true&vCenter=true&width=500&height=38&lines=A+Powerful+Telegram+PDF+Bot.....+;Deployable+On+Heroku+%F0%9F%9A%80+....+;Repo+Modified+%E2%9C%85+By;%40MrBotDeveloper;Show+Your+%E2%9D%A4%EF%B8%8F;%E2%AD%90+the+repo;Follow+%40MrBotDeveloper+Now...+;For+More+%F0%9F%A5%B0)](https://github.com/MrBotDeveloper)

[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://github.com/MrBotDeveloper/PDF-Bot)
[![MIT License](https://img.shields.io/github/license/MrBotDeveloper/telegram-pdf-bot.svg)](https://github.com/MrBotDeveloper/PDF-Bot/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Crowdin](https://badges.crowdin.net/telegram-pdf-bot/localized.svg)](https://crowdin.com/project/telegram-pdf-bot)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-blue.svg)](https://t.me/NACBots)

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=MrBotDeveloper&repo=PDF-Bot&theme=flag-india)](https://github.com/MrBotDeveloper/PDF-Bot)


A Telegram bot that can:

- Compress, crop, decrypt, encrypt, merge, preview, rename, rotate, scale and split PDF files
- Compare text differences between two PDF files
- Create PDF files from text messages
- Add watermark to PDF files 
- Multiple languages support
- Add text layers to PDF files to make them searchable with text
- Extract images and text from PDF files
- Convert PDF files into images
- Beautify handwritten notes images into PDF files
- Convert webpages and images into PDF files

# Repo Special 😅
## What's Special in this repo & To-Do's ???

- [x] ~~Make It Heroku Deployable~~
- [x] ~~Add Detailed Guide to get GCP Credentials~~
- [ ] Add Private Use Feature
- [ ] Add Password feature 🔑 for private use
- [ ] Remove GCP and use another free Cloud Storage.
  - [ ] Add Broadcasting Feature
- [ ] Make it more stable and fast

## Mandatory Vars....

```vars.html
DEV_TELE_ID - Your Telegram ID.
TELE_TOKEN - Telegram Bot Token get from @BotFather
GOOGLE_APPLICATION_CREDENTIALS - Your GCP Credentials get from Google Cloud 
```

## Where To Get The Mandatory Vars..

```DEV_TELE_ID``` - Get it from [Thunder ⚡ Bot](https://t.me/Thunder_GMBot) by sending ```/id```

```TELE_TOKEN``` - Get it from [@BotFather](https://t.me/BotFather)

```GOOGLE_APPLICATION_CREDENTIALS``` - Get it from [Google Cloud ☁️](https://console.cloud.google.com/freetrial)

## Optional Vars....

```vars.txt
STRIPE_TOKEN - Stripe.com token for receiving Donations.
SLACK_TOKEN - slack.com api token to recieve Feedbacks on Slack.com if not entered you will recieve in your Telegram 
```

## Where To Get The Optional Vars...

```STRIPE_TOKEN``` - Get it from [stripe.com](https://stripe.com)

```SLACK_TOKEN``` - Get it from [slack.com](https://api.slack.com/tokens)

## Installation [ ⚠️ Click On Any Topic To Get it's Detailed Information ⚠️]

<details>
  <summary> Getting GCP Ceredinials ⚠️ Important ⚠️ </summary>

## Getting Started

These instructions will get you a copy of the project up. 

### Setup Database

The bot uses [Datastore](https://cloud.google.com/datastore) on Google Cloud Platform (GCP). 

**Sir/Ma'am, Kindly 🤗 follow the below steps to create a valid GCP Credentials File :-**

1. Firstly Go to https://console.cloud.google.com/project
2. Create a Project.
3. Open http://console.developers.google.com/project/_/apiui/credential And Click on Create Ceredinials then Click on Service Account.
4. Enter all the required values. [At the Service Accounts, enter a Service account name and click Create. For Service account permissions, select Project, Owner.]
5. Select a service account. Click the 3 skewer bar and select Create Key. Select JSON, click Create.
6. Click Create. The credential file will be downloaded to your local computer or Any Device your are Using. 
7. Upload the Project Credential file to the bots private repo. 
8. Then Open https://console.cloud.google.com/datastore/setup .
9. And enable the FireStore Database. 
10. Now open https://console.cloud.google.com/iam-admin/iam .
11. And set the service account's role to owner. **Note: If you can't see your service account in the list click on Add and add your service account with Owner as Role.**
12. Now Deploy your bot and set ```GOOGLE_APPLICATION_CREDENTIALS``` var with value as the File Name of the Ceredinials Json you uploaded in the repo in Step 7.
13. Congratulations 🎉 your bot has been Successfully Started 😊 So enjoy 🤗.

```alert.txt
⚠️ I will Recommend you to Use Only Google Chrome for generating Ceredinials Json as some browsers will not start the Download of the Json file in the Step 6 ⚠️
```

**Don't Forget to Star 🌟 Repo if ❤️ The Repo and Follow [Me](https://github.com/MrBotDeveloper) to show your ❤️.**

</details>
<details>
<summary> The Easy Way (Heroku) </summary>

## Follow these steps for a successful deployment.....
  - Star ⭐ the repo 😅 and import it as Private.
  - Upload your GCP Credentials in the root directory with name `GCP_FILE.json`
  - Click on the Below Deploy Button ✅

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/MrBotDeveloper/PDF-Bot/tree/master)
  
  - Enter the Ceredinials and Click in deploy.
  - After Deployment Completed Click on Manage App & Turn on the Dynos....
  - Booyah!! Your PDF Bot is successfully started.
  - Enjoy the Bot 🥳.
## Deploy using GitHub Workflows.....
  - Star ⭐ the repo 😅 and import it as Private.
  - Upload your GCP Credentials in the root directory with name `GCP_FILE.json`
  - Go to Project->Settings->Secrets and Click *New repository secret* and Add All the following Vars as the Repository Secrets.
  
  ```HEROKU_API_KEY```: Your Heroku Account API 
  
  ```HEROKU_APP_NAME``` : Heroku App Name 
  
  ```HEROKU_EMAIL``` : Your Heroku Email 📨 Id 
  
  ```DEV_TELE_ID``` : Your Telegram ID.

  ```TELE_TOKEN``` : Telegram Bot Token get from @BotFather

  ```GOOGLE_APPLICATION_CREDENTIALS``` : Your GCP Credentials get from Google Cloud

  - Go To The Actions Tab and Choose ```Manually Deploy To Heroku``` and click on run workflow.

### Follow [me](https://github.com/MrBotDeveloper) if Love ❣️ the repo.
  

</details>

<details>
<summary> Local Host </summary>

### OS Requirements

Ubuntu

```sh
apt-get install poppler-utils libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

macOS
```sh
brew install libxml2 libxslt poppler cairo pango gdk-pixbuf libffi
```

### Setup Virtual Environment

Create a virtual environment with the following command:

```sh
virtualenv venv
source venv/bin/activate
```

### Bot Requirements

Run the following command to install the required packages:

```sh
pip install -r requirements.txt
```

### Compile the translation files

Run the following command to compile all the translation files:

```sh
pybabel compile -D pdf_bot -d locale/
```

### Setup Your Environment Variables

Copy the `.env` example file and edit the variables within the file:

```sh
cp .env.example .env
```

### Running The Bot

You can then start the bot with the following command:

```bash
python bot.py
```

### Follow [me](https://github.com/MrBotDeveloper) if Love ❣️ the repo.

</details>


## Follow [me](https://github.com/MrBotDeveloper) if Love ❣️ the repo.

## Found a Bug 🐛

```Feel free to create a pull or create a issue now and describe your issue freely.```

<p align="center">
  <a href="https://github.com/MrBotDeveloper/PDF-Bot">
     <img src="https://github.com/MrBotDeveloper/PDF-Bot/blob/master/pdf-bot.metrics.svg">
  </a>
</p>

## Credits 

- [Me 🥰](https://github.com/MrBotDeveloper) For making Deployable To Heroku
- [@zeshuaro](https://github.com/zeshuaro) for his amazing Creation [Telegram PDF Bot](https://github.com/zeshuaro/telegram-pdf-bot)
