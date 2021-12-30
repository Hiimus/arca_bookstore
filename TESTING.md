# Taylor Brookes - Milestone Project 4
## Above Board Testing Document

# Table Of Contents

1. [Code Validation](#code-validation)
2. [Functionality](#functionality)
    * [Security Testing](#security-testing)
    * [Responsiveness](#responsiveness)
    * [General Functionality Testing](#general-functionality-testing)
3. [User Stories Testing](#user-stories-testing)
4. [Resolved Issues](#resolved-issues)
5. [Unresolved Issues](#unresolved-issues)

# Code Validation

## HTML5
#### How:
- I used the [W3C Html Validator](https://validator.w3.org/) I validated via URI, to prevent errors from template language. I added the deployed site's link and tried to validate all my urls.

- Results:
    - No errors.

## CSS3
#### How:
- I could propably do it the same way as I did with the html validation, but there where no templating language I had to consider, so I just found all my css files, copied the css and pasted it via direct input with the [W3C CSS Validation](https://jigsaw.w3.org/css-validator/#validate_by_input).
- Results:
    - No errors.

## JavaScript
#### How: 
- I used [JSHint](https://jshint.com/) and found all scripts and js files and copied and pasted the JavaScript code. 
- Results: 
    - No erros.

## Python
#### How:
- I used flake8 in the IDE. I typed the command `flake8 --count` in the terminal and it counts all the errors. I then went through all of them and corrected as many as possible.
- Results:
- Almost all the error where line too long, and this was mostly on the migration files. The errors on the migration files I choose to ignore. Other than the migration files, I had a couple of errors I will talk more about:
- env.py errors: These I choose to ignore.
- vscode/arctictern.py errors: These I will ignore since I can't see them and I they are most likely generated from a Code Institue template.
- settings.py errors: line too long, these I can't really fix due to long strings so I will ignore them.
- /bag/urls.py:2:20: W291 trailing whitespace: This I have tried to fix, but even though I have removed the trailing whitespace, the error will not go away. I have even copied and pasted a file that is identical, yet the error is still there. I choose to ignore it.
- /checkout/apps.py:8:9: F401 'checkout.signals' imported but unused: This I choose to ignore because it was added by following Boutique Ado, and I think removing this will break the site. Also, I checked it with the [PEP8](http://pep8online.com/), and it was fine.
checkout/webhooks.py:33:5: F841 local variable 'e' is assigned to but never used: This I choose to ignore because I can't seem to fix it and [PEP8](http://pep8online.com/) says it's fine.  



## Responsiveness
Responsiveness was tested with [Responsive Design Checker](https://responsivedesignchecker.com/) and [Google Devtools](https://google.com/). Various devices and screen sizes was tested. Note:

- Throughout the project I have adjusted the screen size in one of the window corners for a quick responsiveness check. See below for an overview of responsiveness testing:

#### Testing for smartphones:
![user-journey1](readme_img/user_journey/user-journey1.JPG)
#### Testing for tablets:
![user-journey1](readme_img/user_journey/user-journey1.JPG)
#### Testing for desktops:
![user-journey1](readme_img/user_journey/user-journey1.JPG)

## Browser Compatibility and Functional Testing

The site's features such as adding products, ordering, buying products, adding reviews, commenting, deleting, editing was tested on all browsers. Registering, logging in, signing out and forgot password was also tested. All links, 404 and 500 pages were also tested. 

Browser test:
![user-journey1](readme_img/user_journey/user-journey1.JPG)



# User Stories Testing

## Common User Stories

*To be able to easily navigate through the site on any size screen*
-	Full responsiveness has been tested thoroughly and all screen sizes are fully working

*Search for products*
-	Search bar can be used for searching by product name, category or keyword
-	This has been tested by using all of the above to search for set products. All products came up as expected

*Sort products by Price, Name etc.*
-	Sort By dropdown works and correctly displays products in the order the user has selected

*View product details*
-	Each product has a set product detail page. This shows all product information including description of product, and product reviews left by users

*Ability to choose quantity of items, and size if applicable*
-	Size dropdown displayed on all relevant products, and works correctly when product is added to the shopping bag
-	Product quantity works correctly and when product is added to the shopping bag, quantity is reflected

*Able to purchase products without an account*
-	Users are allowed to go through the entire site purchase process without the need for an account, although it is suggested at different stages to create an account

*View their shopping bag and amend their order*
-	Shopping Bag icon is always displayed on the navbar, even on a collapsed view so that users have easy access to the shopping bag at all stages of the site

*View Posts in Help & Guidance section*
-	Posts are displayed in the Help & Guidance section, and are displayed from newest post to oldest. Pagination is put to use here in case there are many posts to save users from having to scroll through many posts without knowing when they end

*Contact the company with any queries or if an issue occurs*
-	Contact number, email and address are provided in the footer of the site which is displayed on every page

## First Time Users

*Understand the purpose of the site*
-	Users are shown an About Above Board section on the home page 
-	There is a brief version of this in the footer

*See the reasons behind registering for an account*
-	This is also explained in the About Above Board section on the home page

*Being able to easily sign up for an account*
-	Sign in flows easily and it takes very little time to set up a secure account

## Returning Users

*Ability to securely log into their account*
-	Account log in is set up by Django and is extremely secure
-	Log in process is very quick, and allows a user to save their log in details for next time

*View their past orders and order confirmations*
-	When a user is logged in, if they navigate to the profile page they will be given their Order History
-	It will be a brief overview of the users past orders, but if they click on the order number it will take them to the order confirmation page
-	This is a historic order confirmation page, but displays all the necessary information that a user would need

*Purchase products and have their orders saved to their profile*
-	All users, regardless of logged in status, will be able to purchase products through the site
-	If a user is logged in when they process an order, it will be displayed on their profile order history

*Receive their order confirmations directly to their email inbox*
-	When a user completes an order, they will receive an email to confirm said order
-	This goes directly to the email address provided
-	I have tested this by using different email addresses from different providers, and all worked

*Leave reviews of products*
-	Logged in users are able to leave product reviews
-	On the product details page, reviews are displayed below the main product information display
-	User reviews are displayed at the top, and the review form is below them

## Site Owner/Admin

*Provide a clean, simple e-commerce store so that users can easily find what they’re looking for*
-	I have tested this by asking friends and family to view the site with no direction, and the feedback I have received has been positive
-	Users were easily able to search for what they wanted, find from product lists what they wanted, and successfully purchase products

*Have the ability to add, edit/update and delete products/posts*
-	Add, Edit/Update and Delete functions all work correctly with no errors
-	After editing, correct information is displayed on the site
-	Deleting a product deletes it from the site entirely, including reviews that have been left, and removing it from the admin view

*Keep the site secure by only allowing authorised users access certain areas of the site*
-	Full site authorisation has been implemented by using Djangos `@login_required`
-	This has been tested extensively to make sure no unauthorised access is given at any stage of the site

*Securely store user information in case an error occurs*
-	User information is stored securely using Django. Only information provided is kept, but does not include passwords for security reasons

# Resolved Issues

## Migrations

After I had deployed my project to Heroku, I was getting issues with my migrations not being pushed to Heroku correctly. I reset my migrations, but I didn't do this correctly the first time which lead to me needing to do it twice. 

To successfully reset my migrations, I deleted all previous migrations and the `db.sqlite3` file from GitPod. I then re-ran migrations on GitPod and Heroku, and this fixed the issue I was having. 

# Unresolved Issues

## Product reviews linked to product ratings

I have implemented product reviews on my site, however I was unable to figure out a way to link these up to display as an average rating for the product the reviews are for. I attempted this by following tutorials but was unable to make this work.

## Product Fixtures

As I wanted to display each shoe brand separately I created them as separate categories. This made some future developments rather difficult to navigate on my site as I essentially need to rebuild my fixtures, but did not want to edit them at a late stage in my project.
-	Pagination :- This was not something I could implement on Products pages due to the set up of my fixtures. I followed a few tutorials (which successfully worked for my Help & Guidance section) but they were not successful on my product pages

## Keep Shopping buttons

I would like these buttons to take the user back by one page, but could not find a fix for this.

## 500 Error

If a new product is added to the site, added to the basket then deleted, it causes an error and the entire site crashes. If the cookies are cleared, the site works again as expected. I'm not 100% sure what is causing this error or how to fix it, so it is being left as unresolved. 