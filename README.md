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
- [Balsamiq](https://balsamiq.com/) for creating wireframes.
- [dbdiagram](https://dbdiagram.io/) for creating a database diagram of Veggie Time.
- [Lucid](https://lucid.app/) for creating an overview of how the user can navigate the site.
- [Microsoft Paint](https://support.microsoft.com/en-us/windows/get-microsoft-paint-a6b9578c-ed1c-5b09-0699-4ed8115f9aa9) for resizing images.
- [Am I Responsive](http://ami.responsivedesign.is/), a tool that views the site on various devices.
- [CompressJPEG](https://compressjpeg.com/) was used to compress jpeg files.
- [PurePNG](https://purepng.com/) was used to download images of vegetable chopper and a broccoli image. 
- [Favicon](https://favicon.io/) was used to create a favicon for this project.

## Libraries:
- [jQuery](https://jquery.com/) a JavaScript library.
- [Materializecss](https://materializecss.com/) for a quick page structure, components and colours.
- [Font Awesome](https://fontawesome.com/) as a provider of icons.
- [Google Fonts](https://fonts.google.com/) as a provider of fonts.

## Languages:

[HTML5](https://en.wikipedia.org/wiki/HTML5),  [CSS3](https://en.wikipedia.org/wiki/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

## Frameworks and Packages
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a microframework that was used to provide libraries, technologies and tools for the app.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) was used as a templating language for Python.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) was used for password hashing, authentication and authorization.
- [Heroku](https://heroku.com/) was used as a platform to deploy the app.
- [MongoDB](https://mongodb.com) was used as a cloud database.


# Testing
The testing of this project can be found as a separate [TESTING.md](TESTING.md) file.
# Deployment
### Requirements
- Heroku account
-MongoDB account
- Github account
- Python3
### How to clone this project
In order to make a local clone of this project:
1. Log in to Github and go to the repository.
2. Click on the button with the text "Code".
3. Click on the field with the text "Open with Github Desktop".
4. Follow the steps provided by Github Desktop Application or follow the instruction from this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).
## Working with the local copy
Once you have performed the steps above do the following in your IDE:
1. Make sure you install all the requirements in a requirements.txt file. In the terminal window, type: 
```
pip3 install -r requirements.txt.
```
2. Create a MongoDB database.
3. Sign up to your MongoDB account, and create a cluster and a database.
4. Create these four collections in the database: categories, recipes, users and difficulties.
5. Add keys and values for the collections, copy the projects <a href="#information-architecture">Information architecture</a> so you get the same keys and values.
6. Create environment variables:
- Create a .gitignore file in the root directory to hide confidential files.
- Create a env.py file that will contain all environment variables
```
    Import os
    os.environ.setdefault("IP", "Added by developer")
    os.environ.setdefault("PORT", "Added by developer")
    os.environ.setdefault("SECRET_KEY", "Added by developer")
    os.environ.setdefault("MONGO_URI", "Added by developer")
    os.environ.setdefault("MONGO_DBNAME", "Added by developer")
```
- Add the env.py file in the .gitignore file.
7. Now run the app. In your terminal window, type:
``` 
python3 app.py.
```
### Heroku Deployment
1. Set up the local workspace for Heroku
- Make sure Heroku know which files to  install by typing the following in your terminal: 

```
pip3 freeze --local > requirements.txt
```
- You also need a Procfile, which is a list of the process types Heroku looks for. Type the following: 
```
python app.py > Procfile
```
2. Sign up to Heroku
-Sign up to Heroku, select your region and create a new app.
3. Deployment using the Github deployment method
- Click on the deploy  tab, and then click on "connect to Github".
- Search for your repository and connect to it.
- Go to the settings tab and click on Reveal Config Vars further down the page.
- Enter the variables that are contained in your env.pr file. Your env.py file should contain the info mentioned above (IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME).
4. Now you can add, commit and push the Procfile and requirements.txt.
```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"

    $ git add Procfile 
    $ git commit -m "Add Procfile"
```
5. Finally, click on the deploy tab in Heroku. Scroll down and click on Automatic Deployments. Choose Enable Automatic Deploys. For manual deployment, see the field "Manual deploy" and click on Deploy Branch.
# Credits
## Contents
[SANwebCORNER](https://www.sanwebcorner.com/2017/02/dynamically-generate-form-fields-using.html) for helping me to create a new field when clicking the add ingredient and add instruction step in add recipes page.
[JorisPaarde's app My Vegan Recipies](https://my-veganrecipes.herokuapp.com/) for how to make flash messages appear for a short while.
[mozillazg](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) for how to implement pagination on my all recipes page.
## Media
The vegetable chopper is an image downloaded from [PurePNG](https://purepng.com/). A broccoli image was also downloaded from this site, used as a favicon. 
Default recipe image by Engin Akyurt from [Pexels](https://www.pexels.com/photo/flat-lay-photography-of-variety-of-vegetables-1435904/)
Background image of product by Mark Stebnicki from [Pexels](https://www.pexels.com/photo/selective-focus-photo-of-plants-2749165/)
Background image on desktop by Yaroslav Shuraev from [Pexels](https://www.pexels.com/photo/fresh-vegetables-and-fruits-on-the-table-8844888/).
Background image on mobile and tablet by Nadine Primeau from [Unsplash](https://unsplash.com/photos/wpoKpJqOsKE)

## Acknowledgements
My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for guiding, supporting and pointing me in the right direction.

The Code Institute [Slack](https://slack.com/) channel for having discussion, questions and answers that contribute to my project. Also a lot of similar projects are posted in the slack channel, which contributed to the planning of my project. 

Thanks to Sean from tutor support. He helped me with the add to favorite function.

[Stack Overflow](https://stackoverflow.com/) for helping me understand and solving issues along the way.

# Disclaimer

This project is meant for educational purposes only. Please contact me if there are any problems or issues.

- When adding a recipe, the user can choose to insert the image url. These images might not be royalty free.

<a href="#veggie-time">BACK TO TOP</a>