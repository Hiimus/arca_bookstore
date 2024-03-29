# Arca Bookstore

![Am I responsive image](readme/images/amiresponsive.JPG)

### Arca Bookstore is a web store that sells mainly books, but also arts & crafts, games and puzzles. On this site the user can search, read about and buy products, while also having the opportunity to rate and write reviews on them. The user can also comment on blog posts written by the admin. 
To visit the deployed website, click [here](https://hiimus-arca-bookstore.herokuapp.com/).

Disclaimer: This project is meant for educational purposes only. The images for arts & crafts and games are not my own, see the credits. Please contact me if there are any problems or issues. 
# Table of Contents
 - <a href="#ux">1. User Experience (UX)</a>
    - <a href="#project-goals">1.1. Project goals</a>
    - <a href="#user-journey">1.2 User Journey</a>
    - <a href="#user-stories">1.2 User stories</a>
    - <a href="#design">1.3 Design</a>
    - <a href="#information-architecture">1.4 Information architecture</a>
    - <a href="#database-schema">1.4 Database Schema</a>
    - <a href="#wireframes">1.5 wireframes</a>
- <a href="#features">2. Features</a>
    - <a href="#existing-features">2.1 Existing features</a>
    - <a href="#features-left-to-implement">2.2 Features left to implement</a>
- <a href="#technologies-used">3. Technologies used</a>
    - <a href="#tools">3.1 Tools</a>
    - <a href="#languages">3.2 Languages</a>
    - <a href="#frameworks-and-libraries">3.3 Frameworks and Libraries</a>
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

Note: for the user journey I have chosen desktop view.
### Home

- When accessing this website, the user will see a navbar on the top where they can search for products, check the shopping bag, view the profile account or navigate through all the other pages the store provides.

<details>
  <summary>Navbar</summary>
  <img src="readme/images/navbar.JPG">
</details>

- The homepage will show a purple container with two sections. The top section has three images, with text related to the images. When hovering the text will become larger and the cursor will turn into a pointer, giving the user a good idea that these images are links to these different products.

<details>
  <summary>Category Images</summary>
  <img src="readme/images/category-images.JPG">
</details>

- In the next section of the container the user will be presented with a sample of products the store provides. These are randomized so everytime the page reloads, there will be new products. On each of the product samples there is a hyperlink the user can click on in order to see all products within that genre.

<details>
  <summary>Sample Products</summary>
  <img src="readme/images/random-products.JPG">
</details>

- On the bottom of the home page, and on every page, there is a footer. This footer is simple, displaying the three social links for twitter, instagram and facebook.


<details>
  <summary>Footer</summary>
  <img src="readme/images/footer.JPG">
</details>

### Product Pages

The products are separated into their respective genre. The genres are books, arts & crafts and games. The user may access products from the navbar, from searching or simply clicking the images or hyperlinks on the home page. 

- If the user clicks the "All Products" link in the navbar, there will be a randomized sample, similar to the home page.

<details>
  <summary>All Products Page</summary>
  <img src="readme/images/all-products.JPG">
</details>

- If the user accesses the products with the other methods mentioned, the genre will appear as a heading, with all the available categories underneath. Here the user can see how many products there are and a sorting selector.


<details>
  <summary>Books Page</summary>
  <img src="readme/images/books-page.JPG">
</details>
<details>
  <summary>Arts & Crafts Page</summary>
  <img src="readme/images/arts-and-crafts-page.JPG">
</details>
<details>
  <summary>Games Page</summary>
  <img src="readme/images/games-page.JPG">
</details>


### Product Details Page

- When clicking on a product, the product details page for that product will open. Here, the user can read more about the product, such as description, format and pages. 

<details>
  <summary>Product Details Page</summary>
  <img src="readme/images/product-details-1.JPG">
</details>

- If the user wishes to buy the product, the user can easily choose the amount, and add the product to the shopping bag. This action will be displayed in the top right corner of the page. 

<details>
  <summary>Adding to Bag</summary>
  <img src="readme/images/product-details-2.JPG">
</details>

- There is also a section for customer reviews, where the user can see reviews and ratings. If the user wishes to write a review themselves, they would need to register first.

<details>
  <summary>Review</summary>
  <img src="readme/images/review.JPG">
</details>

### Blog Page

- The blog page also uses the purple container to organise a blog image in the top, a heading and the blog posts below. 

<details>
  <summary>Blog Page</summary>
  <img src="readme/images/blog-page.JPG">
</details>

Only superusers/admin can add blog posts. However, registered users can comment on these blog posts. By clicking on a post, the user can read all its content and comment.


### Help Pages

The site has three help pages; FAQ, Contact and Policies. All these pages can be accessed from the navbar.

- The FAQ page displays questions with answers, organised in their category. If the user wishes to ask a question, the user can click on the email link below the header (this link only opens a gmail page).

<details>
  <summary>FAQ Page</summary>
  <img src="readme/images/faq.JPG">
</details>

- The Return and Refund Policy page can also be accessed from the FAQ page under the Return and Delivery section. Note: This is just a downloaded template where some fields have been modified.

<details>
  <summary>Policies Page</summary>
  <img src="readme/images/policies.JPG">
</details>

- The contact page is a simple page with contact information.

<details>
  <summary>Contact Page</summary>
  <img src="readme/images/contact.JPG">
</details>

### Registration Pages
- In order to use all features, the user needs to register. This page can be accessed from the "My account button"

<details>
  <summary>Registration Page</summary>
  <img src="readme/images/sign-up.JPG">
</details>

- On this page the user must provide an email, username and password.


- When clicking on the "Sign Up" button, the user will then have to click on the link that was sent to the registered email and verify the account 

<details>
  <summary>Verifying Email</summary>
  <img src="readme/images/confirm-email.JPG">
  </details>
<details>
  <summary>Email Confirmation</summary>
  <img src="readme/images/confirm-email2.JPG">
</details>

### Login and Forgot Password Page 

- After registering, the user can sign in. Here the user must provide either the username or the registered email address and their password. If the user has forgotten their password, they can click the link on the bottom left corner. A "remember me" practical checkbox is available if the user wants the login information to be remembered.

<details>
  <summary>Forgot Password</summary>
  <img src="readme/images/reset-password.JPG">
</details>


### Profile Page

After registering and logging in the user can access their own account page. This page contains their default delivery information and their order history. 

- This will be blank, since they haven't filled it out yet, but the first time they fill it out, there will be an option to save this information so that they don't need to do it again. From the profile page the user can update this information by clicking on the "Update Information" button.

<details>
  <summary>Profile Page</summary>
  <img src="readme/images/profile-page.JPG">
</details>

### Shopping Bag Page

- There are two ways the user can access the shopping bag. One way is to just click the shopping bag icon in the navbar or dropdown, the other way is by clicking the "Checkout" button in the message box that appears when adding items in the bag.



- Once on the shopping bag page, the user will see an overview of the items that the bag contains, with costs. From here the user can either keep shopping by clicking the "Keep Shopping" button, or proceed to checkout by clicking the "Secure Checkout" button.

<details>
  <summary>Shopping Bag</summary>
  <img src="readme/images/shopping-bag.JPG">
</details>

### Checkout Page

- On the checkout page the user will see the products in the order summary with total costs. The user can choose to click the "Adjust Bag" button to make changes to the order, or continue the checkout by filling out the delivery information form. As mentioned earlier, the delivery information can be saved, but only if the user is registered. 

<details>
  <summary>Checkout Page</summary>
  <img src="readme/images/checkout.JPG">
</details>

- After filling in necessary card information, the user can complete the order by clicking the "Complete Order" button. Then, an order confirmation page with an overview of the order and delivery information will be displayed. On this page there is a "Back to Home" button that will send the user back to the home page.

<details>
  <summary>Checkout Success</summary>
  <img src="readme/images/checkout-success.JPG">
</details>

## User Stories

Users of this site will be non-registered users, registered users and superusers. 
### Non-Registered Users
- As a non-registered user I want to browse multiple products so that I can look without narrowing down a search.
- As a non-registered user I want to view more details of a product so that I can get more information about the product.
- As a non-registered user I want to be able to do a search so that I can find the product I am looking for.
- As a non-registered user I want to add products to a shopping bag/cart so that I can select multiple products and view them in the bag.
- As a non-registered user I want to view the total price of the products in the bag so that I can have control of my spendings.
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
I have just about used five different colors, and the "Maximum Yellow Red", "Dark Purple" and white color make up most of the site. I decided on these colors by just clicking on the color palette generator from [coolors](https://coolors.co/). When I landed on these colors I just liked them, and I figured I would go with those.

<details>
  <summary>Color Palette</summary>
  <img src="readme/images/color-palette.JPG">
</details>



### Fonts
There are two different fonts used on this site: 'Gloria Hallelujah' from google fonts and 'Verdana'. 
Due to the fact that the store sells books, crafts and games, I felt the store needed a font that is playful, artistic and almost as if it was written by hand with a thin brush. That is why I landed on the 'Gloria Hallelujah' font. Considering readability, this font works best when the text isn't too small, so that's why I have used 'Verdana' on smaller text. Also, the pages that display things like order history, grand total or return policy should have a more formal font than 'Gloria Hallelujah', and so 'Verdana' have been used here also.

<details>
  <summary>Gloria Hallelujah Font</summary>
  <img src="readme/images/font.JPG">
</details>

## Icons
All icons used on this project are provided by [Font Awesome](https://fontawesome.com/). The icons serve as buttons or links that have functions, see below for examples of some icons used.


<details>
  <summary>Footer Icons</summary>
  <img src="readme/images/icons-1.JPG">
</details>
<details>
  <summary>Contact Icons</summary>
  <img src="readme/images/icons-2.JPG">
</details>
<details>
  <summary>Product Category Icons</summary>
  <img src="readme/images/icons-3.JPG">
</details>


## Images
Most of the images used on this website are product images. 

- All the book images have been downloaded as a dataset from [Kaggle](https://www.kaggle.com/lukaanicin/book-covers-dataset). This dataset provides 33 book categories and each contains close to 1k images. I have just picked a few categories, and some of the images from them.

Note: Regarding the product images for arts & crafts and games, I struggled to find good images from royalty free sites, so I found them on other web stores. These will be mentioned in the acknowledgments and on the top of this readme. Since this project is only for educational purposes, I think mentioning this as a disclaimer and acknowledging them is okay. that Those I could not find on royalty free sites, so those are downloaded from [The Works](https://www.theworks.co.uk/).

- All product images for the arts & crafts, and games pages are from [The Works](https://www.theworks.co.uk/).

Other than having product images, I also have category images on the homepage, a blog image on the blog page, 404 and 500 error images, FAQ and contact images. I also have a red book next to the logo and as a favicon. 

<details>
  <summary>Red Book beside logo and as favicon</summary>
  <img src="readme/images/red-book.JPG">
</details>

- The category images and blog image are from [pexels](https://www.pexels.com/).

- Images for 404, 500, FAQ and contact are downloaded from [freepik](https://www.freepik.com/).

<details>
  <summary>404 Image</summary>
  <img src="readme/images/404.jpg">
</details>
<details>
  <summary>500 Image</summary>
  <img src="readme/images/500.jpg">
</details>

## Defensive design

- Products can only be reviewed and rated if a user is registered. The same goes with commenting on blog posts. Trying to access these pages in the url will only redirect the user to the login page, because I have added the "@login_required" decorator on the view.

- Only superusers can add/edit/delete products. If a normal user tries to access the "products/add", "products/edit" or "products/delete" page, a message will let the user know that only store owners can do that. 

<details>
  <summary>Defensive Design</summary>
  <img src="readme/images/not-allowed.JPG">
</details>

- Only superusers can write a blog post. A normal user simply will not see the "Add Blog Post" button.

<details>
  <summary>Blog Page for normal users</summary>
  <img src="readme/images/blog-normal-user.JPG">
</details>
<details>
  <summary>Blog Page for superusers</summary>
  <img src="readme/images/blog-superuser.JPG">
</details>

- When registering, there are certain requirements that have to be met, and this is provided by django allauth. An example is choosing a password that is too similar to the username. Another example is that django allauth requires that the user must change the account via email.

<details>
  <summary>Validation Feedback</summary>
  <img src="readme/images/example-password.JPG">
</details>

- Allauth will let the user know if the username or password is wrong.

- All accounts pages are made with allauth. Trying to access "accounts/logout" when not logged in, will only render the user back to the home page. Trying to "accounts/signup" when already signed in, will just render the user to the homepage.


- When adding items to the bag, the user will not be able to use anything else than whole numbers. 


- If the user tries to access a page that doesn't exist, a custom 404 page will appear with a link back to home.

- If the site experiences a 500 error, a custom 500 error page will appear, with a link back to home.



## Information architecture

Heroku PostgreSQL is used to host the backend database for this site.

Arca Bookstore contains these Django apps:

- Blog
- Bag
- Checkout
- Help
- Home
- Products
- Profiles

## Database Schema

Note: I could not manage to make the connections where I wanted them so I just drew them myself.

<details>
  <summary>Database Schema</summary>
  <img src="readme/images/database-schema.png">
</details>



## Wireframes
To make [wireframes](readme_img/wireframes), I used [Balsamiq](https://balsamiq.com/).

<details>
  <summary>Wireframes for desktops</summary>
  <img src="readme/images/wireframes/desktop-1.JPG">

  <img src="readme/images/wireframes/desktop-2.JPG">

  <img src="readme/images/wireframes/desktop-3.JPG">

  <img src="readme/images/wireframes/desktop-4.JPG">

  <img src="readme/images/wireframes/desktop-5.JPG">

  <img src="readme/images/wireframes/desktop-6.JPG">
</details>
  
<details>
  <summary>Wireframes for tablets</summary>
  <img src="readme/images/wireframes/tablet-1.JPG">

  <img src="readme/images/wireframes/tablet-2.JPG">

  <img src="readme/images/wireframes/tablet-3.JPG">

  <img src="readme/images/wireframes/tablet-4.JPG">

  <img src="readme/images/wireframes/tablet-5.JPG">

  <img src="readme/images/wireframes/tablet-6.JPG">
</details>
<details>
  <summary>Wireframes for mobiles</summary>
  <img src="readme/images/wireframes/mobile-1.JPG">

  <img src="readme/images/wireframes/mobile-2.JPG">

  <img src="readme/images/wireframes/mobile-3.JPG">

  <img src="readme/images/wireframes/mobile-4.JPG">

  <img src="readme/images/wireframes/mobile-5.JPG">

  <img src="readme/images/wireframes/mobile-6.JPG">
</details>


<a href="#arca-bookstore">BACK TO TOP</a>

# Features

Note: In order to not duplicate images I will not be attaching images to every single feature in this section. Please refer to the images in the user journey.

## Existing Features:

- Navbar with links to all pages on the site, including the logo, a search bar, "My account" icon and the shopping bag. On smaller devices the main navigation is a hamburger menu.

<details>
  <summary>Navbar</summary>
  <img src="readme/images/navbar.JPG">
</details>

<details>
  <summary>Hamburger menu</summary>
  <img src="readme/images/hamburger-menu.JPG">
</details>

- A Back to top button

<details>
  <summary>Back to Top button</summary>
  <img src="readme/images/back-to-top.JPG">
</details>

- Footer with social links to twitter, instagram and facebook.

- Messages/toasts that appear on the top right when the user performs actions such as logging in and out, adding and removing products from the shopping bag, completing a transaction, and for superusers actions like adding and editing products/blog posts.

### Page Specific Features

### Home page

- Category images with hovering effect and links to the category mentioned.

- A randomized product samples section that displays products of different categories and subcategories.

- Links to show all products within the category.

- Product cards with hover effect that display product image, product title, price, subcategory, and rating.


### Products Page

All the product pages(books, arts & crafts, games) are the same, except for the actual products.

- The products page has a heading, stating what category is being viewed, and all the subcategories listed below the heading. These subcategories can be clicked, to view all products within that subcategory.

- On the products pages there is a sort selector on the right side that has different options for sorting, and a product counter to the left side, with a link to all products next to it.


- Edit/Delete buttons for superusers to edit or delete products.

### Product Details

When clicking on a product, the user will be directed to the product details page.

- Edit/Delete buttons for superusers.

- On the product details page there is a larger image of the product, and a full description of the product, including pages and format. 

- A quantity selector to select the amount of items

- Button for "Keep Shopping" that directs to all products pages.

- Button for "Add to bag" that adds the amount selected in the quantity selector.

- A hyperlink for "Add Review" for logged in users to add a review of the product.

- A Customer Reviews section with reviews displaying the date it was added, the username of the author, the rating and the review.


### Shopping Bag 

- Quantity selector with remove and update icon buttons 

- A free delivery notice below the grand total

- Buttons for "Keep Shopping" and "Secure Checkout" where the latter directs to the checkout page.

### Checkout

- Order summary

- Button for "Adjust Bag" that reverses the user to the shopping bag.

- A delivery details form with a save option.

- A button for "Complete Order" that initiates a full screen loading spinner.


### Profile page 
- Order history with a hyperlink on the order number that directs to a more informative order info page.

- Delivery information with saved information if used.

- An "Update Information" button that updates the delivery information.

### Blog Page

When clicking on the Blog link in the navbar/main nav, the blog page will appear. This page has the following features:

- Blog image

- "Back to Home" hyperlink that directs to the homepage.

- "Add Blog Post" button that opens a model where a blog post can be written. (Only for superusers)

- Blog posts with a limited amount of the post displayed, small version of the blog image, date added, the creator and edit/delete buttons (Only accessible for superusers).


### Blog Info Page

When clicking on a post, the blog info page for that post will open. The blog info page has the following features:

- A blog image in the top of the container that can be clicked and will reverse the user back to the blog page.

- A "Back to blog" button that reverts the user back to the blog page.

- The actual posts heading, body, image and date added.


- A comment form that all registered users can use to comment on the blog post.


- Comment section that displays all comments with name, comment and date created. Superusers are able to delete posts and comments.


### FAQ Page

When clicking on the Help link in the navbar/main nav, there are three options: FAQ, Policies and Contact. This is the features on the FAQ page:

- A link to Arca Bookstore's email address (Opens up a link to gmail).

- A "Back to Home" button.

- FAQ sections with different categories that display hyperlinked questions. Clicking a hyperlink will reveal an answer.


- An FAQ image at the bottom.

### Policies Page

By clicking on the second option; Policies, the Return and Refund Policy page opens.

- A return and refund policy email addresses where necessary and a link to the contact page at the bottom.

### Contact Page

The third Help option is the Contact page.

- Icons that help to explain the contact method of email, phone and address.

- Contact Image


## Features Left to Implement:

This is the features I would like to implement in the future:

- Let registered users have the option to edit and delete their own reviews and comments. For now that is only possible for the superuser. This is a high priority as this is an important feature.

- Pagination. As more products are added, it will be poor user experience to not have pagination when there are alot of products. This will also reduce loading time.

- More content on pages that look too empty, i.e an empty shopping bag, or when no results are found after searching. The same goes with styling. More use of containers or images could fill up the page, making it more appealing.

- Currently there are no warnings when the superuser deletes a product, a blog post, review or a comment. This is an easy fix, it's just that I didn't have time to implement it. An important feature which will be high on the priority list.

- Breadcrumbs. I really like when websites provide links to the path you have taken, so you can easily click yourself back to where you want to.

- In general just more product reviews and quality blog posts.

- Let the registered users have the option to choose a profile image that will also appear when commenting or reviewing.


<a href="#arca-bookstore">BACK TO TOP</a>

# Technologies Used
## Tools:
- [Gitpod](https://www.gitpod.io/) used as an IDE.
- [GitHub](https://github.com/) used to store and share repositories.
- [Git](https://git-scm.com/) for version control.
- [Stripe](https://stripe.com/) - Used for card payments
- [Balsamiq](https://balsamiq.com/) for creating wireframes.
- [dbdiagram](https://dbdiagram.io/) for creating a database diagram of Arca Bookstore.
- [Microsoft Paint](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9) for resizing images.
- [Am I Responsive](http://ami.responsivedesign.is/), a tool that views the site on various devices.
- [CompressJPEG](https://compressjpeg.com/) was used to compress jpeg and png files.
- [PurePNG](https://purepng.com/) was used to download the red png image that is used next to the logo and as a favicon. 
- [Favicon](https://favicon.io/) was used to create a favicon for this project.
- [Djecrety](https://djecrety.ir/) was used to make a Django secret key.


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

<a href="#arca-bookstore">BACK TO TOP</a>


# Deployment

This will be an explanation of the process involved in how to deploy the site using [Heroku](https://heroku.com), and to set up and store images and static files using [Amazon Web Services](https://aws.amazon.com/).

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

•	Then, in your `settings.py` file, comment out the database that's currently being used as a default(sqlite) and instead add the following;
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

1. After you click the "Create Bucket" button, you will be directed to your bucket dashboard. One here, click on the “Properties” tab and scroll down to the bottom of the page. Once on the “Static website hosting” section, click on the edit button.

2. On the top section, "Enable" static website hosting. 

3. In the section below, select “Host a static website” and scroll down to the “Index Document” inputs. 

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

5. Copy the policy into the bucket policy editor, adding `/*` To the end, click “Save Changes”.

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


<a href="#arca-bookstore">BACK TO TOP</a>


# Credits
## Code

- The walkthrough project Boutique Ado from Code Institute helped me alot. I coded along, and learned many things about how to use the Django framework, how to implement Stripe payment system, and many other things. My checkout app heavily relies on the code from this walkthrough project. Since I made an e-commerce store similar to the one in Boutique Ado, I had the perfect resources to help me through my own project.

- I learned how to add line breaks in forms from this [stack overflow](https://stackoverflow.com/questions/20095936/add-rich-text-format-functionality-to-django-textfield) thread.

- The underline text decoration I got from this [stack overflow](https://stackoverflow.com/questions/30352431/css-transition-not-working-with-underline) thread.



## Contents

- I downloaded a return and refund policy from [termsfeed.com](https://www.termsfeed.com/blog/sample-return-policy-ecommerce-stores/#Sample_Return_Refund_Policy_Template_Full_Text_Download
)

- I copied text and an image from [A Little Blog of Books](https://alittleblogofbooks.com/2012/08/28/the-rise-of-ebooks-evil-or-essential/) that I used as a blog post.


## Media

- As mentioned in the Image section of this README, images for Arts & Crafts and Games were downloaded from [theworks.co.uk](https://www.theworks.co.uk/). 

- All product images for the books were downloaded from [Kaggle](https://www.kaggle.com/lukaanicin/book-covers-dataset).

- All other images were downloaded from [Pexels](https://pexels.com/) and [freepik](https://www.freepik.com/).

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

