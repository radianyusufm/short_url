# Short URL

## Overview

This is a web application that allows users to shorten URLs, generate QR Codes for short URLs, as well as track information about the device used by the user, the user's operating system, browser, and display the total number of clicks from short URLs.

The Short URL web application is designed using the Python Framework Django and SQLite database on the backend. On the frontend, the Short URL application is designed using Javascript and CSS Bootstrap.


## Distinctiveness and Complexity

**Distinctiveness**

- The Short URL Web Application has a feature to take a long URL entered by the user and generate a related short URL.

     On the "Create URL" page, there is a "Destination URL" input form that the user uses as a destination link when the user clicks on a short URL.

- Password addition option that allows users to restrict direct access to shortened URLs.

     On the "Create URL" page, there is a "Link with password" checkbox. When the check box is checked, an input for entering the password will be displayed. This feature allows users to create passwords. which is used to limit access to a short URL to only those who know the password.

**Complexity**

- There is also a feature to generate a QR Code for each short URL generated.
    
     On the "Link" page, there is a button to generate a QR Code from a short URL. This feature was added so that users can scan links using a QR Code without having to remember the actual URL.

     QR Code is generated using the qrcode.js library.

- There is a tracking feature that records information about the device used by the user such as the operating system, browser, device, and the number of clicks that occur.

     On the "Details" page, there is a user tracking feature. Every time a URL is visited, Web Short URL will record the number of times the URL was visited. By utilizing the "user agent" HTTP header, each URL visited will record information about the browser used by the user, the device used, and the operating system used.


## Contained in every file I create.

**Frontend (template/capstone)**

- `404.html` page: This is a landing page that indicates that the Short URL visited by the User does not exist.

- `create_url.html` page : This is a page that displays a form for creating a short URL.
     - There is one mandatory input to fill in the URL location to be visited.
     - There is a checkbox to show or hide the password input.
     - There is an optional password input to direct users to enter the password before going to the original destination link.


- `index.html` page: This page displays all short links created by logged in users.
There is a card that displays the following information:
     - Original URL Location
     - Short URLs
     - "Copy Short URL" button
     - Date information
     - Number of Clicks
     - "Generate QR Code" button
     - Link to Details page


- `detail.html` page : This page displays specific details of the short URL based on ID.
There is a card that displays the following information:
     - Original URL Location
     - Short URLs
     - "Copy Short URL" button
     - Information whether the short URL has a password or not
     - Date information
     - Number of Clicks
     - Total usage of each browser used by users to click on links
     - Total usage of each device used by the user to click on the link
     - Total usage of each operating system used by users to click on links
     - "Delete" button to delete short URLs.


**Frontend (static/capstone)**

- file `create_url.js`: this file sets the display of 'input password' in the file `create_url.html`, when the checkbox is clicked, the input password will be displayed by setting `style.display = 'block`

- `index.js` file: this file manages the appearance of the `index.html` page,
     - there is a Jquery bootstrap modal that sets the popup to display a QR code
     - there is a generate_qr_code function to generate QR Code
     - there is a copy text function to be used in the short URL copy button

- `style.css` file: contains appearance adjustments in the form of classes.
     - `#modal-body` : to set the qrCode display to be centered
     - `.button-right` : to set the button to be on the right
     - `.button-center` : to set the button to be in the center

**Backend (capstone)**
- `models.py` file: There are 3 models as follows:
     - User: Record username, email and password information.
     - ShortUrl: Records user information as (foreign key), original URL, short URL, password, date and number of clicks.
     - Analytics: Records urlshort information as (foreign key), operating system type, browser type, and device type.

- `util.py` file: There is a function `generate_slug()` to generate a unique slug used for short URL slugs. This function calls the random library which is used to generate random characters from `[a-zA-Z0-9]` and loops 7 times for random characters, then returns 7 random characters.


- `views.py` file: Contains all view definitions that manage HTTP requests and generate HTTP responses in the Short URL Application

     - `index` function: Displays all short links created by the user in reverse order and renders index.html.

     - `create_short_url` function: Creates a short url by calling the `generate_slug()` function. If the resulting slug is the same as the one in the database, it will regenerate the slug. Once successful, it will be redirected to the `index.html` page.

     - `get_url_short` function: Gets short URL data based on the slug, increments the number of clicks field, and extracts data from the `http user_agent` header, such as user device data, browser and operating system used. After that, check whether there is a password associated with the urlshort. If there is, it will be redirected to `password.html`. If it is not there, it will immediately redirect to the original link.

     - `password` function: Gets a password from user input, then checks whether the password is the same as the one in the database. If the password is the same, it will be redirected to the original link. If not, it will display a `message` indicating that the password is incorrect.

     - `detail` function: Gets all details from shorturl by id, gets data from `Analytics` model, and calculates Device, Operating System, and Browser totals. Then displays them in descending order (DESC).

     - `delete_url` function: Deletes url based on id.



## How to run the application

1. Install the required packages
`pip install -r requirements.txt`

2. Perform database migration
`python manage.py makemigration`

3. Define database migration
`python manage.py migrate`

4. Run the Django server
`python manage.py runserver`

5. visit `http://127.0.0.1:8000/`


## Additional information

To generate a QR code, I use the qrcode.js javascript library
`<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>`