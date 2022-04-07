# Midterm Personal Lab

## General Information

Course: CSC13002 - Introduction to Software Engineering

Student: 19120454 - Bui Quang Bao

Commit History: https://github.com/buiquangbao/CSC13002-MidtermPersonalLab/commits/main

Django Videos Playlist: https://youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO

## Deployment

### Heroku

Heroku Deployment: https://buiquangbao-crm1.herokuapp.com (free deployment - slow, not stable, sometimes not load properly)

**Account for testing (already registered):**

* Admin Account:
  * username: admin
  * password: 1

* Customer Account:
  * username: customer
  * password: semidterm

### Local

⚠️ Note: The project with the latest commit is configured for Heroku deployment, can cause errors and problems when trying to deploy locally.

1. Clone repository
2. Install Python
3. Install libraries/packages in `crm1/requirements.txt`
4. Terminal:
   1. `cd` to crm1
   2. `python manage.py runserver`
5. Open `localhost` port `8000` (http://127.0.0.1:8000)