# Item Catalog Udacity Full Stack Project

## Introduction

Develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.


Learn how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. You will then learn when to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

## Code Samples

1.The Item Catalog project consists of developing a Case Manager application that provides a list of fraud items within a variety of fraud categories, as well as provide a user registration and google authentication system.

2.The homepage displays all current Fraud categories along with the latest added fraud items.

3.Selecting a specific fraud category shows you all the fraud items available for that fraud category.

4.Selecting a specific fraud case item shows you specific information of that case item.

5.After logging in, a user has the ability to add, update, or delete case item info.

6.The application provides JSON endpoints.


## Installation

*Setup application database python /CaseManagement/database_setup.py
*Insert fake data python /CaseManagement/database_init.py
*Run application using python /CaseManagement/app.py
*Access the application locally using http://localhost:9001

##Google Login
*Go to your app's page in the Google APIs Console — (https://console.developers.google.com/apis)
*Choose Credentials from the menu on the left.
*Create an OAuth Client ID.
*This will require you to configure the consent screen, with the same choices as in the video.
*When you're presented with a list of application types, choose Web application.
*You can then set the authorized JavaScript origins, with the same settings as in the video.
*You will then be able to get the client ID and client secret.
*You can also download the client secret as a JSON data file once you have created it.



##JSON Endpoints

Catalog JSON: /CaseManagement/JSON - Displays the whole catalog. Categories and all items.

Categories JSON: /CaseManagement/categories/JSON - Displays all categories

Category Items JSON: /CaseManagement/<path:category_name>/items/JSON - Displays items for a specific category

Category Item JSON: /CaseManagement/<path:category_name>/<path:item_name>/JSON - Displays a specific category item.