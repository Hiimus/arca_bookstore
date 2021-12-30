# Arca Bookstore

![Am I responsive image](readme_img/veggie-time-devices.JPG)

### Arca Bookstore is a web store that sells mainly books, but also arts & crafts, games and puzzles. On this site the user can search, read about and buy products, while also having the opportunity to rate and write reviews on them. The user can also comment blog posts written by the admin. 
To visit the deployed website, click [here](https://hiimus-arca-bookstore.herokuapp.com/).
# Table of Contents
 - <a href="#ux">1. User Experience (UX)</a>
    - <a href="#project-goals">1.1. Project goals</a>
    - <a href="#user-journey">1.2 User Journey</a>
    - <a href="#user-stories">1.2 User stories</a>
    - <a href="#design">1.3 Design</a>
    - <a href="#information-architecture">1.4 Information architecture</a>
    - <a href="#wireframes">1.5 wireframes</a>
- <a href="#features">2. Features</a>
    - <a href="#existing-features">2.1 Existing features</a>
    - <a href="#features-left-to-implement">2.2 Features left to implement</a>
- <a href="#technologies-used">3. Technologies used</a>
    - <a href="#tools">3.1 Tools</a>
    - <a href="#libraries">3.3 Libraries</a>
    - <a href="#languages">3.4 Languages</a>
    - <a href="#frameworks-and-packages">3.4 Frameworks and Packages</a>
- <a href="#testing">4. Testing</a>
- <a href="#deployment">5. Deployment</a>
- <a href="#credits">6. Credits</a>
    - <a href="#contents">6.1 Contents</a>
    - <a href="#media">6.2 Media</a>
    - <a href="#acknowledgements">7. Acknowledgements</a>
- <a href="#disclaimer">8. Disclaimer</a>


# UX

## Project Goals
- To make a web store that has full CRUD (create, read, update and delete) functionality. 
- To make a full-stack web application using HTML, CSS, JavaScript, Python, using a Django framework.
- Create engagement where users can rate, write reviews and comment.
- Create a book store site where the user can browse books and other related products with ease.
## User Journey
### Home

- When accessing this website, the user will see a navbar on the top where they can search for products, check the shopping bag, view the profile account or navigate through all the other pages the store provides.

![user-journey1](readme_img/user_journey/user-journey1.JPG)

- The homepage will show a purple container with two sections. The top section has three images, with text related to the images. When hovering the text will become larger and the cursor will turn into a pointer, giving the user a good idea that these images are links to these different products.

![user-journey1](readme_img/user_journey/user-journey1.JPG)

- In the next section of the container the user will be presented with a sample of products the store provides. These are randomized so everytime the page reloads, there will be new products. On each of the product samples there is a hyperlink the user can click on in order to see all products within that genre.

![user-journey2](readme_img/user_journey/user-journey2.JPG) ![user-journey3](readme_img/user_journey/user-journey3.JPG)

- On the bottom of the home page, and on every page, there is a footer. This footer is simple, displaying the three social links for twitter, instagram and facebook.


### Product Pages

The products are separated to their respective genre. The genres are books, arts & crafts and games. The user may access products from the navbar, from searching or simply clicking the images or hyperlinks on the home page. 

- If the user clicks the "All Products" link in the navbar, there will be displayed the randomized sample, similar to the home page.

![user-journey4](readme_img/user_journey/user-journey4.JPG)

- If the the user access the products with the other methods mentioned, the genre will appear as a heading, with all the available categories underneath. Here the user can see how many products there are and a sorting selector.

Image of books, arts & crafts and games
![user-journey4](readme_img/user_journey/user-journey4.JPG)
![user-journey4](readme_img/user_journey/user-journey4.JPG)
![user-journey4](readme_img/user_journey/user-journey4.JPG)

Image of sorting selector
![user-journey4](readme_img/user_journey/user-journey4.JPG)

### Product Details Page

- When clicking on a product, the product details page for that product will open. Here, the user can read more about the product, such as description, format and pages. 

![user-journey4](readme_img/user_journey/user-journey4.JPG)


- If the user wish to buy the product, the user can easily choose the amount, and add the product to the shopping bag. This action will be displayed in the top right corner of the page. 

![user-journey4](readme_img/user_journey/user-journey4.JPG)

- There is also a section for customer reviews, where the user can see reviews and ratings. If the user wishes to write a review themselves, they would need to register first.

![user-journey4](readme_img/user_journey/user-journey4.JPG)


### Blog Page

- The blog page also uses the purple container to organise a blog image in the top, a heading and the blog posts below. 

![user-journey4](readme_img/user_journey/user-journey4.JPG)

Only superusers/admin can add blog posts. However, registered users can comment these blogs posts. By clicking on a post, the user can read all its content and comment.


### Help Pages

The site have three help pages; FAQ, Contact and Policies. All these pages can be accessed from the navbar.

- The FAQ page displays questions with answers, organised in their category. If the user wishes to ask a question, the user can click on the email link below the header (this link only opens a gmail page).

![user-journey4](readme_img/user_journey/user-journey4.JPG)

- The Return and Refund Policy page can also be accessed from the FAQ page under the Return and Delivery section. Note: This is just a downloaded template were some fields have been modified.

- Arca Bookstore has a contact page with fake contact information.
![user-journey4](readme_img/user_journey/user-journey4.JPG)


### Registration Pages
- In order to use all features, the user needs to register. This page can be accessed from the "My account button"
![user-journey4](readme_img/user_journey/user-journey4.JPG)

- On this page the user must provide an email, username and password.
![user-journey4](readme_img/user_journey/user-journey4.JPG)

- When clicking on the "Sign Up" button, the user will then have to click on the link that was sent to the registered email and verify the account 
Image of email:
![user-journey4](readme_img/user_journey/user-journey4.JPG)
Image of verification page:
![user-journey4](readme_img/user_journey/user-journey4.JPG)

### Login and Forgot Password Page 

- After registering, the user can sign in. Here the user must provide either the username or the registered email address and their password. If the user has forgotten their password, they can click the link on the bottom left corner. A "remember me" practical checkbox is available if the user want the login information to be remembered.

Image of forgot password:
![user-journey4](readme_img/user_journey/user-journey4.JPG)

Image of login with remember me:
![user-journey4](readme_img/user_journey/user-journey4.JPG)


### Profile Page

After registering and loggin in the user can access their own account page. This page contains their default delivery information and their order history. 

- This will be blank, since they haven't filled it out yet, but the first time they fill it out, there will be an option to save this information so that they don't need to do it again. From the profile page the user can update this information by clicking on the "Update Information" button.

### Shopping Bag Page

- There are two ways the user can access the shopping bag. One way is to just click the shopping bag icon in the navbar or dropdown, the other way is by clicking the "Checkout" button in the message box that appears when adding items in the bag.

![user-journey4](readme_img/user_journey/user-journey4.JPG)

- Once on the shopping bag page, the user will see an overview of the items that the bag contains, with costs. From here the user can either keep shopping by clicking the "Keep Shopping" button, or proceed to checkout by clicking the "Secure Checkout" button.

![user-journey4](readme_img/user_journey/user-journey4.JPG)

### Checkout Page

- On the checkout page the user will see the products in the order summary with total costs. The user can choose to click the "Adjust Bag" button to make changes to the order, or continue the checkout by filling out the delivery information form. As mentioned earlier, the delivery information can be saved, but only if the user is registered. 

![user-journey4](readme_img/user_journey/user-journey4.JPG)

- After filling in necessary card information, the user can complete the order by clicking the "Complete Order" button. Then, an order confirmation page with an overview of the order and delivery information will be displayed. On this page there is a "Back to Home" button that will send the user back to the home page.

![user-journey4](readme_img/user_journey/user-journey4.JPG)


## User Stories

Users of this site will be non-registered users, registered users and superusers. 
### Non-Registered Users
- As a non-registered user I want to browse multiple products so that I can look without narrowing down a search.
- As a non-registered user I want to view more details of a product so that I can get more information about the product.
- As a non-registered user I want to be able to do a search so that I can find the product I am looking for.
- As a non-registered user I want to add products to a shopping bag/cart so that I can select multiple products and view them in the bag.
- As a non-registered user I want to view to see the total prize of the products in the bag so that I can have control of my spendings.
- As a non-registered user I want to select categories so that I can find multiple products within a category.
### Registered Users
- As a registered user I want to view my order history so that I can see my previous orders.
- As a registered user I want to be able to edit my personal information and shipping information so that I can change it if I want to.
- As a registered user I want to reset my password so that I can change it or enter a new one if I forget the old password.
### Superusers
- As a superuser I want to add products so that I can display a product on the site.
- As a superuser I want to edit a product so that I can change or add something if I want to. 
- As a superuser I want to delete a product so that I can remove the product if I want to.

## Design
### Colors
I have just about used five different colors, and the "Maximum Yellow Red", "Dark Purple" and white color make up most of the site. I decided on these colors by just clicking on the color palette generator from [LINK TO https://coolors.co/]. When I landed on these colors I just liked them, and I figured I would go with those.

Color palette:
![colour-scheme](readme_img/colour-scheme.JPG)

Dark purple container:
![colour-scheme](readme_img/colour-scheme.JPG)
(A sentence about why you like this color)

Yellow navbar:
![colour-scheme](readme_img/colour-scheme.JPG)
(A sentence about why you like this color)

Charcoal buttons and back to top button:
![colour-scheme](readme_img/colour-scheme.JPG)
(A sentence about why you like this color)

green buttons:
![colour-scheme](readme_img/colour-scheme.JPG)
(A sentence about why you like this color)



### Fonts
There are two different fonts used on this site: 'Gloria Hallelujah' from google fonts and 'Verdana'. 
Due to the fact that the store sells books, crafts and games, I felt the store needed a font that is playful, artistic and almost as if it was written by hand with a thin brush. That is why I landed on the 'Gloria Hallelujah' font. Considering readability, this font works best when the text isn't too small, so thats why I have used 'Verdana' on smaller text. Also, the pages that display things like order history, grand total or return policy should have a more formal font than 'Gloria Hallelujah', and so 'Verdana' have been used here also.

![Leckerli One Font](readme_img/fonts/leckerli-font.JPG) ![Muli font](readme_img/fonts/muli-font.JPG)

## Icons
All icons used on this project are provided by [Font Awesome](https://fontawesome.com/). The icons serve as buttons or links that have functions, see below for examples of some icons used.

Image of different icons
![colour-scheme](readme_img/colour-scheme.JPG)
![colour-scheme](readme_img/colour-scheme.JPG)
![colour-scheme](readme_img/colour-scheme.JPG)
![colour-scheme](readme_img/colour-scheme.JPG)

## Images
Most of the images used on this website is product images. 

- All the book images have been downloaded as a dataset from [Kaggle](https://www.kaggle.com/lukaanicin/book-covers-dataset). This dataset provides 33 book categories and each contains close to 1k images. I have just picked a few categories, and some of the images from them.

Note: Regarding the product images for arts & crafts and games, I struggled to find good images from royalty free sites, so I found them on other web stores. These will be mentioned in the acknowledgments and on the top of this readme. Since this project is only for educational purposes, I think mentioning this as a disclaimer and acknowledging them is okay. that those I could not find on royalty free sites, so those are downloaded from [The Works](https://www.theworks.co.uk/).

- All product images for the arts & crafts, and games pages are from [The Works](https://www.theworks.co.uk/).

Other than having product images, I also have category images on the homepage, a blog image on the blog page, 404 and 500 error images, FAQ and contact images. I also have a red book next to the logo and as a favicon. 

- The category images and blog image are from [pexels](https://www.pexels.com/).
![colour-scheme](readme_img/colour-scheme.JPG)

- Images for 404, 500, FAQ and contact are downloaded from [freepik](https://www.freepik.com/).
![colour-scheme](readme_img/colour-scheme.JPG)

## Defensive design

- Products can only be reviewed and rated if a user is registered. The same goes with commenting on blog posts. Trying to access these pages in the url will only redirect the user to the login page, because I have added the "@login_required" decorator on the view.
[VIS KODE MED DECORATOR]

- Only superusers can add/edit/delete products. If a normal user tries to access the "products/add", "products/edit" or "products/delete" page, a message will let the user know that only store owners can do that. 
![colour-scheme](readme_img/colour-scheme.JPG)

- Only superusers can write a blog post. A normal user simply will not see the "Add Blog Post" button.
![colour-scheme](readme_img/colour-scheme.JPG)

- When registering, there are certain requirements that have to be met, and this is provided by django allauth. An example is choosing a password that is too similar to the username. Another example is that django allauth requires that the user must very the account via email.
![colour-scheme](readme_img/colour-scheme.JPG)
![colour-scheme](readme_img/colour-scheme.JPG)


- Allauth will let the user know if the username or password is wrong.

![colour-scheme](readme_img/colour-scheme.JPG)

- All accounts pages are made with allauth. Trying to access "accounts/logout" when not logged in, will only render the user back to the home page. Trying to "accounts/signup" when already signed in, will just render the user to the homepage.


- When adding items to the bag, the user will not be able to use anything else than whole numbers. Previously, adding i.e 1.5 to the bag, would break the site. I then added this code, and that prevents the user from breaking the site.

[CODE THAT PREVENTS .,]

- If the user tries to access a page that doesn't exist, a custom 404 page will appear with a link back to home.
![colour-scheme](readme_img/colour-scheme.JPG)

- If the site experience a 500 error, a custom 500 error page will appear, with a link back to home.
![colour-scheme](readme_img/colour-scheme.JPG)


## Interactive Design
- Below is an overview of how the user can navigate this site.

![overview of site](readme_img/overview.JPG)


## Wireframes
To make [wireframes](readme_img/wireframes), I used [Balsamiq](https://balsamiq.com/).
# Features
## Existing Features:

- Navbar with links to all pages on the site, including the logo, a search bar, "My account" icon and the shopping bag. On smaller devices the main navigation is a hamburger menu.

![overview of site](readme_img/overview.JPG)
![overview of site](readme_img/overview.JPG)

- A Back to top button

![overview of site](readme_img/overview.JPG)

- Footer with social links to twitter, instagram and facebook.

![overview of site](readme_img/overview.JPG)

- Messages/toasts that appear on the top right when the user perform actions such as logging in and out, adding and removing products from the shopping bag, completing a transaction, and for superusers actions like adding and editing products/blog posts.

### Page Specific Features

### Home page

- Category images with hovering effect and links to the category mentioned.

- A randomized product samples section that displays products of different categories and subcategories.

- Links to show all products within the category.

- Product cards with hover effect that display product image, product title, price, subcategory, and rating.


### Products Page

All the products pages(books, arts & crafts, games) are the same, except for the actual products.

- The products page have a heading, stating what category is being viewed, and all the subcategories listed below the heading. These subcategories can be clicked, to view all products withing that subcategory.
![overview of site](readme_img/overview.JPG)

- On the products pages there is a sort selector on the right side that have different options for sorting, and a product counter to the left side, with a link to all products next to it.
![overview of site](readme_img/overview.JPG)

- Edit/Delete buttons for superusers to edit or delete products.

### Product Details

When clicking on a product, the user will be directed to the product details page.

![overview of site](readme_img/overview.JPG)

- Edit/Delete buttons for superusers.

- On the product details page there is a larger image of the product, and a full description of the product, including pages and format. 

- A quantity selector to select the amount of items

- Button for "Keep Shopping" that directs to all products page.

- Button for "Add to bag" that adds the amount selected in the quantity selector.

- A hyperlink for "Add Review" for logged in users to add a review of the product.

- A Customer Reviews section with reviews displaying the date it was added, the username of the author, the rating and the review.


### Shopping Bag 

- Quantity selector with remove and update icon buttons 
![overview of site](readme_img/overview.JPG)

- A free delivery notice below the grand total

- Buttons for "Keep Shopping" and "Secure Checkout" where the latter directs to checkout page.

### Checkout

- Order summary
![overview of site](readme_img/overview.JPG)

- Button for "Adjust Bag" that reverse the user to the shopping bag.

- A delivery details form with a save option.
![overview of site](readme_img/overview.JPG)

- A buttton for "Complete Order" that initates a full screen loading spinner.
![overview of site](readme_img/overview.JPG)


### Profile page 
- Order history with a hyperlink on the order number that directs to a more informative order info page.
![overview of site](readme_img/overview.JPG)
![overview of site](readme_img/overview.JPG)

- Delivery information with saved information if used.

- An "Update Information" button that updates the delivery information.
![overview of site](readme_img/overview.JPG)

### Blog Page

When clicking on the Blog link in the navbar/main nav, the blog page will appear. This page has the following features:

- Blog image

- "Back to Home" hyperlink that directs to homepage.

- "Add Blog Post" button that opens a model were a blog post can be written. (Only for superusers)

- Blog posts with a limited amount of the post displayed, small version of the blog image, date added, the creator and edit/delete buttons (Only accessible for superusers).

![overview of site](readme_img/overview.JPG)

### Blog Info Page

When clicking on a post, the blog info page for that post will open. The blog info page has the following features:

- A blog image in the top of the container that can be clicked and will reverse the user back to the blog page.

- A "Back to blog" button that reverse the user back to the blog page.

- The actual posts heading, body, image and date added.

![overview of site](readme_img/overview.JPG)

- A comment form that all registered users can use to comment on the blog post.

![overview of site](readme_img/overview.JPG)

- Comment section that displays all comments with name, comment and date created. The author of the comment will be able to delete their own posts, and superusers are able to delete all posts.

![overview of site](readme_img/overview.JPG)

### FAQ Page

When clicking on the Help link in the navbar/main nav, there are three options: FAQ, Policies and Contact. This is the features on the FAQ page:

- A link to Arca Bookstore's email address (Opens up a link to gmail).

- A "Back to Home" button.

- FAQ sections with different categories that displays hyperlinked questions. Clicking a hyperlink will reveal an answer.

![overview of site](readme_img/overview.JPG)

- An FAQ image at the bottom.

### Policies Page

By clicking on the second option; Policies, the Return and Refund Policy page opens.

- A return and refund policy email addresses where neccesary and a link to the contact page at the bottom.

### Contact Page

The third Help option is the Contact page.

- Icons that helps to explain the contact method of email, phone and address.

- Contact Image

![overview of site](readme_img/overview.JPG)




## Features Left to Implement:

This is the features I would like to implement in the future:

- Pagination. As more products are added, it will be poor user experience to have not have pagination when there are alot of products. This will also reduce loading time.

- More content on pages that looks to empty, i.e an empty shopping bag, or when no results are found after searching. The same goes with styling. More use of container or images could fill up the page, making it more appealing.

- Currently there are no warnings when the superuser deletes a product, a blog post, review or a comment. This is an easy fix, it's just that I didn't have time to implement it. An important feature which will be high on the priority list.

- Breadcrumbs. I really like when websites provide links to the path you have taken, so can easily click yourself back to where you want to.

- In general just more product, reviews and quality blog posts.

- Letting the registered users have the option to choose a profile image that will also appear when commenting or reviewing.


# Technologies Used
## Tools:
- [Gitpod](https://www.gitpod.io/) used as an IDE.
- [GitHub](https://github.com/) used to store and share repositories.
- [Git](https://git-scm.com/) for version control.
- [Stripe](https://stripe.com/) - Used for card payments
- [Balsamiq](https://balsamiq.com/) for creating wireframes.
- [dbdiagram](https://dbdiagram.io/) for creating a database diagram of Arca Bookstore.
- [Lucid](https://lucid.app/) for creating an overview of how the user can navigate the site.
- [Microsoft Paint](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9) for resizing images.
- [Am I Responsive](http://ami.responsivedesign.is/), a tool that views the site on various devices.
- [CompressJPEG](https://compressjpeg.com/) was used to compress jpeg and png files.
- [PurePNG](https://purepng.com/) was used to download the red png image that is used next to the logo and as a favicon. 
- [Favicon](https://favicon.io/) was used to create a favicon for this project.


## Languages:

[HTML5](https://en.wikipedia.org/wiki/HTML5),  [CSS3](https://en.wikipedia.org/wiki/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

## Frameworks and Libraries
- [Django](https://www.djangoproject.com/) was used as the main python framework.
- [Heroku](https://heroku.com/) was used as a platform to deploy the app.
- [jQuery](https://jquery.com/) a JavaScript library.
- [Bootstrap 5](https://https://getbootstrap.com/docs/5.0/getting-started/introduction/) for a quick page structure, components and colours.
- [Font Awesome](https://fontawesome.com/) as a provider of icons.
- [Google Fonts](https://fonts.google.com/) as a provider of fonts.

## Databases

- [SQlite3](https://docs.python.org/3/library/sqlite3.html) - Used as the development database
- [PostgreSQL](https://www.postgresql.org/) - Used as the deployed database
- [AWS S3](https://aws.amazon.com/) - Amazon Web Services, used for hosting images and static files


# Testing
The testing of this project can be found as a separate [TESTING.md](TESTING.md) file.


# Deployment

This will be an explanation of the process involved in how to deploy the site using [Heroku], and to set up and store images and static files using [Amazon Web Services].

Note: Credit to Code Institute Boutique Ado videos on how to deploy using heroku and AWS.

## Heroku

•	Go to [Heroku](https://www.heroku.com)

•	Register a new account, if you already have an account, log in. 

•	Create a new app. When choosing an app name, make sure to use only lower case letters and no spaces.

•	Choose the region closest to you and select “Create App”

---

•	When you have created the app, click on the “Resources” tab to add the Postgres database

•	Type “Heroku Postgres” and select it from the dropdown list

•	By selecting Postgres, Heroku will automatically create a DATABASE_URL variable stored in the Heroku Config Vars. The config variables can be found by clicking on the “Settings” tab, and clicking the “Reveal Config Vars” button.

•	Click on the Deploy tab, and scroll down to the Deployment method. Click on the “GitHub” tab and search for your repository. Click on your repo name.

•	After you have linked the repository, enable automatic deployment by clicking "Enable automatic deployments".

---

•	In order to use the Postgres database, open your IDE and install `dj_database_url` and `psycopg2-binary`.

•	Then, in your `settings.py` file, comment out the database thats currently being used as a default(sqlite) and instead add the following;
```
DATABASES = {
	‘default’ = dj_database_url.parse(‘database_url')
}
```

---

- If you already have data in the sqlite database that you want to store as a JSON file, you can type `python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json`. This will store the data you already have to a db.json file.

•	Now that the settings are set to, login to Heroku via the CLI in your IDE by typing `heroku login –i`

- Provide your email and password, login.

•	Once logged in, you have to run migrations to migrate your models to Postgres.

•	In the CLI, enter `heroku run python3 manage.py migrate --plan`. This will not migrate the models, but will give you the plan of the migration. If you are pleased with this plan, run  `heroku run python3 manage.py migrate` and enter.

•	In order to load data to Postgres and heroku, you need fixtures in JSON format. Either use the data you imported from the existing database and/or load other fixtures you want to use. Note: If you have categories that are related to the products, load these first. This can be done by typing the following in the CLI:

`heroku run python3 manage.py loaddata categories`

`heroku run python3 manage.py loaddata products`

•	You would need to create a superuser in order to access the django admin page. This is done by typing `python3 manage.py createsuperuser` in the CLI. 

- In the CLI install `gunicorn`

•	You will also have to create a `requirements.txt` file and a `Procfile`. Create the requirements.txt file by typing `pip3 freeze > requirements.txt` in CLI and create the Procfile with right click --> new file and simply name it `Procfile`.

- In the Procfile write `web: gunicorn name_of_your_app.wsgi:application`.

• IMPORTANT! Before committing and pushing these changes to GitHub, make sure you uncomment your DATABASES code in settings.py and amend your code to ensure your database url doesn’t get accidentally committed to GitHub!

•	Once this is done, `add`, `commit` and `push` your changes to GitHub

---

IMPORTANT!

You need to make sure you have config variables that are up to date on Heroku such as any secret keys to ensure your app works as intended! Your Config variables should look something similar to the table below. Note: The variables listed also include the ones for AWS which the following section will explain.

| Key                   | Value                    |
| --------------------- |--------------------------|
| AWS_ACCESS_KEY_ID     | `aws_access_key`         |
| AWS_SECRET_ACCESS_KEY | `aws_secret_access_key`  |
| DATABASE_URL          | `auto-generated`         |
| EMAIL_HOST_PASS       | `email_key`              |
| EMAIL_HOST_USER       | `your_email`             |
| SECRET_KEY            | `secret_key`             |
| STRIPE_PUBLIC_KEY     | `your_stripe_public_key` |
| STRIPE_SECRET_KEY     | `your_stripe_secret_key` |
| STRIPE_WH_SECRET      | `stripe_webhook_key`     |
| USE_AWS               | `True`                   |

---

## AWS

### Setting Up

1. Go to [Amazon Web Services] and register for an account if you don’t already have one. You will need to provide credit/debit card details, you should not exceed the free limit, but keep an eye on the usage to avoid any surprises. 

2. Sign in to AWS, and find S3 by searching for it in the search bar.

3. Now you should create a new bucket by clicking on the “Create Bucket” button. 

4. When creating a new bucket, make sure the Heroku name matches the bucket name. Remember to select the region closest to you.

5. Now scroll down to “Block Public Access settings for this bucket”, uncheck the box, and confirm. 

6. Scroll to the bottom of the page and click the "Create Bucket" button. 

---

### Bucket Properties

1. After you clicked the "Create Bucket" button, you will be directed to your bucket dashboard. One here, click on the “Properties” tab and scroll down to the bottom of the page. Once on the “Static website hosting” section, click on the edit button.

2. On the top section, "Enable" static website hosting. 

3. On the section below, select “Host a static website” and scroll down to the “Index Document” inputs. 

4. Specify the home or default page, which should be `index.html`.

5. It will then give you the option of entering an error link for if an error occurs. In the input, type `error.html`

6. Leave the Redirection rules blank, and click the “Save Changes” button. 

---

### Setting Permissions

1. Once you have set the bucket properties, it's time to set permissions. Click on the “Permissions” tab and scroll to the bottom of the page and click edit in the “Cross-origin resource sharing (CORS)” section. 

2. Add in the following code:

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

3. Click on the “Save Changes” button and navigate to the “Bucket Policy” section and click edit.

---

### Bucket Policy

1. After setting permission, you need to generate a bucket policy. Click on the “Policy Generator” button. This will open a new page where you can do this. 

2. First, select “S3 Bucket Policy from the dropdown list.

3. Second, ensure you have these options set:

    - Effect – Allow
    - Principle - *
    - Actions – GetObject, GetObjectAcl, PutObject, PutObjectAcl and DeleteObject
    - Amazon Resource Name (ARN) – This will be found on the previous page, under “Bucket ARN”. Copy this and paste it into this box

4. After these have been entered, click “Add Statement” then “Generate Policy”.

5. Copy the policy into the bucket policy editor, adding `/*` onto the end, the click “Save Changes”.

---

### Access Control List (ACL)

1. Still in the permissions tab, scroll down to the Access control list(ACL) and click the edit button. 

2. From here, navigate to “Everyone (public access)” and tick the left box "List". Make sure to tick the checkbox below that you understand the effects of the changes. Click "Save changes".

---

### IAM - Creating A Group and Policy

1. Next, search for IAM in the search bar at the top, and click on it. You will now set up a group policy.

2. Click on the "User Groups" subcategory, under "Access Management" on the left side.

3. Once on this page, click the create a group button and give the group a name.

4. This will take you back to the IAM dashboard. Go back to the “Access Management” section on the left hand side, and click on “Policies”. 

5. Click “Create Policy” and in the JSON tab, select “Import Managed Policy”. 

6. Search for “AmazonS3FullAccess”, select it, then click on the “Import” button.

7. Copy your ARN and place it in the code so that it looks like the below;

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR-ARN",
                "arn:aws:s3:::YOUR-ARN/*"
            ]
        }
    ]
}
```

8. Click on “Next: Tags”, “Next: Review”, put in a name and click on “Create Policy”. 

---

### Group Policy

1. Next, you will need to attach the AmazonS3FullAccess Policy to the Group created.

2. Go to “User Groups” on the left hand side menu, under “Access Management”.

3. Once on this page, you will find your created group. Click on it and head to the “Permissions” tab.

4. Click on the “Add Permissions” dropdown, and select “Attach Policy”.

5. Search for and tick the checkbox next to the policy you have just created, then click “Add Permissions”.

---

### IAM - Create User

1. Back at the IAM dashboard (you can click on the link in the top left corner), click on “Users” on the left hand side menu, then the “Add User” button.

2. Choose a name i.e "app-name-staticfiles-user" and tick the checkbox to give the user access, then click “Next: Permissions”.

3. Select the group to put the user in and keep clicking the next buttons until the very end and click “Create user”.

4. IMPORTANT: Click on “Download .csv” file and make sure you save this mindfully because you will not have access to this page again! The .csv file will contain information such as your access codes (shown above in the Heroku Deployment section).

---

### **Important!**

Make sure to add this to your settings.py file:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

---

### Saving Images To S3 Bucket

If you need to save images to your S3 bucket, you will need to do the following;

1. Search for S3 in the search bar, click it and access your bucket.

2. Now create a new folder by clicking the "Create folder" button, name the folder name i.e "media", then click the "Create folder" button. 

3. Now you can access the "media" folder you just created, and you can upload images by clicking the "Upload" button, and choosing either to add files or folders. When you have selected the files/folder you want, click the "Upload" button. 


# Credits
## Code

- The walkthrough project Boutique Ado from Code Institute helped me alot. I coded along, and learned many things about how to use the Django framework, how to implement Stripe payment system, and many other things. My checkout app heavily relies on the code from this walktrough project. Since I made an e-commerce store similar to the one in Boutique Ado, I had the perfect resources to help me through my own project.

- I learned how to user from this [stack overflow](https://stackoverflow.com/questions/20095936/add-rich-text-format-functionality-to-django-textfield) thread.

- The underline text decoration I got from this [stack overflow](https://stackoverflow.com/questions/30352431/css-transition-not-working-with-underline) thread.

- In the shopping bag the site would crash if not whole numbers was added, i.e 1.5. This [Stack overflow](https://stackoverflow.com/questions/37043867/how-to-avoid-decimal-values-in-input-type-number) thread helped me solve it by adding some JavaScript that only allow whole numbers.

- For some reason, on some pages the screen was flickering when hovering over elements that had a hover effect. This [Github](https://github.com/jackmoore/autosize/issues/307) thread helped me fix it by adding `overlfow: scroll` to the body in the base.html.



## Contents

- I downloaded a return and refund policy from [termsfeed.com](https://www.termsfeed.com/blog/sample-return-policy-ecommerce-stores/#Sample_Return_Refund_Policy_Template_Full_Text_Download
)


[SANwebCORNER](https://www.sanwebcorner.com/2017/02/dynamically-generate-form-fields-using.html) for helping me to create a new field when clicking the add ingredient and add instruction step in add recipes page.
[JorisPaarde's app My Vegan Recipies](https://my-veganrecipes.herokuapp.com/) for how to make flash messages appear for a short while.
[mozillazg](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) for how to implement pagination on my all recipes page.
## Media

- As mentioned in the Image section of this README, images for Arts & Crafts and Games was downloaded from [theworks.co.uk](https://www.theworks.co.uk/). 

- All product images for the books was downloaded from [Kaggle](https://www.kaggle.com/lukaanicin/book-covers-dataset).

- All other images was downloaded from [Pexels](https://pexels.com/) and [freepik](https://www.freepik.com/).

- The book used in the logo on small devices and as a favicon was downloaded from [PurePNG](https://purepng.com/).

## Acknowledgements
My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for guiding, supporting and pointing me in the right direction.

The Code Institute [Slack](https://slack.com/) channel for having discussion, questions and answers that contribute to my project. Also a lot of similar projects are posted in the slack channel, which contributed to the planning of my project. 

Thanks to Sean, Igor and Kevin from tutor support. They helped me figure out how to work with models, querying, fixtures and to fix the gitpod issue that affected my workspace.

Credit to [taybro23](https://github.com/taybro23/AboveBoard_MS4#deployment)'s MS4 README. I used his section on deployment as inspiration for my own deployment section.

[Stack Overflow](https://stackoverflow.com/) for helping me understand and solving issues along the way.

# Disclaimer

This project is meant for educational purposes only. Please contact me if there are any problems or issues.



<a href="#arca-bookstore">BACK TO TOP</a>