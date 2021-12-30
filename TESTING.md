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

#### Non-Registered Users
- As a non-registered user I want to browse multiple products so that I can look without narrowing down a search.
    - A non-registered user can browse multiple product either from the home page, where the user can see a sample of products from different categories. From here the non-registered user have many options on browsing multiple products. The user can either click on the products links in the navbar/main nav, click on the "Click here to see all books" hyperlink, or click on one of the category images.
     ![user-journey1](readme_img/user_journey/user-journey1.JPG)
- As a non-registered user I want to view more details of a product so that I can get more information about the product.
    - A non-registered user can view more details of a product by clicking a product card. Once clicked, the user will be directed to the product details page of that product. Here the user will find much more detailed information about the product.
- As a non-registered user I want to be able to do a search so that I can find the product I am looking for.
    - A non-registered user is able to do a search from the search bar in the navbar/main nav.
- As a non-registered user I want to add products to a shopping bag/cart so that I can select multiple products and view them in the bag.
    - A non-registered user can add products to a shopping bag from the product details page. From here the user can view the shopping bag either from clicking on the message container on the top right corner, or by clicking on the shopping bag icon from the navbar/main nav.
- As a non-registered user I want to view to see the total price of the products in the bag so that I can have control of my spendings.
    - A non-registered user is able to see the total price of the products on the shopping bag page, and also on the checkout page.
- As a non-registered user I want to select categories so that I can find multiple products within a category.
#### Registered Users
- As a registered user I want to view my order history so that I can see my previous orders.
    - A registered user is able to view the order history by clicking on the profiles page from the navbar/main nav. Once on this page the registered user can see all orders. Also, by clicking on the hyperlink order number, the registered user can view all information about the order, including delivery information.
- As a registered user I want to be able to edit my personal information and shipping information so that I can change it if I want to.
    - A registered can edit their personal information from the profile page. The registered user can simply type in the input fields and click on the green "Update Information" button.
- As a registered user I want to reset my password so that I can change it or enter a new one if I forget the old password.
    - A registered user can reset the password by clicking "Log in" in the navbar/main nav and then click the "Forgot Password?" link. Once on this page, the registered user must provide the email address linked to Arca Bookstore and then click on the "Reset My Password" button.
#### Superusers
- As a superuser I want to add products so that I can display a product on the site.
    - A superuser can add products by first logging in, and then click "My Account" in the navbar/main nav, then "Add a Product". From this page, simply fill out the required fields, and click on the green "Add Product" button.
- As a superuser I want to edit a product so that I can change or add something if I want to. 
    - A superuser can edit a product from the homepage, all products page, all product pages and on the product details page. Once the superuser is logged in, an "Edit" link is displayed on each product card. The superuser can click this link and will be directed to the edit page. Once on this page, all the product information currently saved to that product will already be filled out. Once the superuser has made changes, simply click on the "Update Product" button to save the changes.
- As a superuser I want to delete a product so that I can remove the product if I want to.
    - A superuser can delete a product by accessing the same pages as when editing a prodcuct. The only difference is the superuser must click on the red "Delete" link instead.



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