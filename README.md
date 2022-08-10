### 
About

    2FA for rest api. in these days we need to be sure that data which we use and share can be trusted and are shared 
    among intended partners. in this approach Django REST framework with JWT protected using twilio sms
    
    for referencing.
    [Django REST framework](https://www.django-rest-framework.org/)
    [Django]( https://www.djangoproject.com/)
    [Simple JWT] (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

###

Stack
    
- git
- python3.9
- Django3.0
- and more on the pipfile

Running the project

- make sure you have twilio account and credentials or go sign up [https://www.twilio.com/]()
- first create | copy .env file at the root of the project 
        
         .env file must contain the following variables with values
        
            - DEBUG=True
            - ACCESS_TOKEN_LIFETIME_MINUTES=5
            - REFRESH_TOKEN_LIFETIME_DAYS=1
            - TWILIO_ACCOUNT_SID=AC575a5213bdeadxxxxxxxxx
            - TWILIO_AUTH_TOKEN=fbe1d0710cxxxxxxxxba255
            - TWILIO_PHONE_NUMBER=+2459898989
            - TIME_OTP_DURATION_SECONDS=300

- Running with docker
  
  - add local .env file and update it to align with above variables
         
        - cp .env.sample .env

  - build project from docker images
  
        - make build
    
  - run project
    
        - make up

- Running locally
    
    clone the project https://github.com/ramawakil/otp_auth_backend.git
    
    install pipenv

    run migrations "python manage.py migrate"
    
    run project "python manage.py runserver"


Project Usage

    - for log in or register use the url below then you will receive sms on mobile with code
        /api/v1/get-code/

    - then use the code on the following url to receive JWT credentials (access,refresh) tokens
        /api/v1/verify/

    - verify tokens validity
        /api/token/verify/

    - renew the access token with refresh tokens
        /api/token/refresh/


ToDo

      - Unit tests
      - Update Readme File  
      - Postman test collection
      - cURL examples
      - rest api flows
      - link to video example


Issue

      - psycopg2-binary library might bring some error if not tied to the version specified on pipfile (if expect to deploy on heroku)

License
    
    [MIT] (https://opensource.org/licenses/mit-license.html)

Disclaimer

No warranty expressed or implied. Software is as is.