# OREGANO OIL E-COMMERCE, SHOP AND SHARE.
## Purpose of the Website

The purpose of this e-commerence website, is that it is a shop for oregono oil and other infusions. You will be able to buy different types of infused oil, as well as pure oil. 

The purpose of the site is to be a easy understandable purchasing online shop, that will provide information about the health product, as well as a interactive place where a logged in user can add there own testimonial, or like and unlike the information post in the info page. 
The site should provide information about the products through a easy accessible nav bar,that directs the user to the info page. 

The user whilst logged in should be able to create their own testimonials, like or unlike the information post. Any user should be able to access a contact form, which sends messages directly to the admin of the sites' email. 

Primarily being a site to purchase oregano oil and ajoining products, the user logged in or out should be able to add a product to their basket, navigate to the basket and purchase there items, using stripe. If the user is a signed up user, they can save what's in their basket.

Other attribrutes to the site include a useful admin page, where the super user can easily navigate and add/edit or delete products.Update new orders manually, add new products manually, check users, check verified emails, as well as edit testimonials etc. The super user can also see current active orders, current verified emails etc.  As well as a  product management page on the website, which allows the store owner (superusers) to add/edit/delete a product.

The user can perform crud with there own testimonials. The user can save their address and orders.
A star rating is implemented for future use of the site, in the future it will give me feedbck, for now its only color changing.

# Business Plan

* The intention of this e-commerence site is to generate sales for the oregano oil and ajoining products.

* Some things had to be thought out before designing the site, the first is the use of keywords and useful words inside the website. With the intention of improving sales with web optimization, by using certain more popular words inside your website can generate users.

* Here is a list of some key words that were useful and less useful for the website. (with use of the worktracker.com.)

  1. oregano
  2. health
  3. benefits
  4. near me
  5. oregano oil
  6. health products

![Skärmbild (561)](https://github.com/hnjw-png/oregano-oil/assets/120515252/02293e71-1f74-4bb2-a97f-6ba4faedb399)


* A robots.txt and sitemaps.xml was added to make the site more truthworthy to the browser, and therefore more likely to appear higher in the search engine.

* The site uses using interactivity to make it more than just a shop, its a place where you can leave your own testimonial, and read others. A place to find out information about oregano oil and even be redirected to a official informational website for more information.

* As a store owner its easy to keep track on all site activity by logging in to the admin panel. This panel gives the administator oppurtunity to add whatever they like to the site. As well at the power to remove or add users. Add or delete testomonials, keep track of orders and add products..amoung a few other features.

* A store owner is given a product management page on the site, where he/she can freely add new products. This is a place only the admin can see and use. The procuts are automatically added to the database and to the webpage.

* The site provides the option for the shopper to open a profile and save there order and address information. This is a way to make it easier for the customer to come back and buy whatevers in his/her bag.  Without needing to add it again, which promotes sales. 

* The website has a secure way to make payments through stripe, this is a secure way customers can pay and order a product. Being connected to a payment platform, makes it much payment process much smoother.

* Once the product has been ordered the store owner will be able to see the order in the admin page.

* Confirmation emails are intended to be used for confirmed orders.

* A user must verify their email to sign up for a users account, this to keep the site secure and check these users are humans. Anyone can register for a account. for a employee for example; to be added to admin, the admin must do use in the admin panel.

* The customer can toggle how many of each product they want on the product details page and on the bag. The ability to remove a item exists within the shopping bag. This functionality makes the shopping process smooth, and there raises likelihood of sales.

* The user can use on CRUD on the site, they can add, edit or remove their own testimonials. Unregistered users will be redirected to log to be able to perform CRUD to testimonials, but can view published ones. This keeps the user on the site longer and raises the likelihood of a purchase, through screen time on the website.

* The admin can delete any testimonial he/she wishes through the admin panel, this is to maintain quality for the site. That only informative and 'beyond the doubt to be true' testionials will be able to stay. This will be stated on the site for the user to see.

* The logged in user can LIKE the info page,or take back their LIKE. Whilst a user who is not registered cannot like it and will be prompted to sign up or log in. The user can see they liked the post by 1 like appearing and can remove there like and see it go down to 0.

* The likes are registered in the sql database, this can be used as a tool for the store owner so they can keep a even better check on website activity and interest. You can also sees if a user has likes the post on the admin, is go and click on the user.

* A contact form, that is intended to be send directly to the store owners email. The contact form is important so that users can really feel connected the to site, that they can comminicate with a customer service and ask any questions they need. Which is important for purchases and especially for health products.

* A inclusion of a info page is important to give the iser a really good idea of what they are buying.

* The footer, includes a link to a bespoke facebook webpage for the Oregano Oil Shop. The facebook page keep shoppers connected the shop and all its news and updates, which is turn ca generate sales, due to extra engagement. As well as a oppurtunity to sign up for the newsletter through mail chimp; this is intented to keep customer engagaed with the busniness, and in the future a letter will be send out each week.

* A function that is appealing and helps the overall interactivity of the site is the star rating system. I have added a 5 star rating system. It is a color changing button that the user can click. This is intended as a future improvement, and is showcases in the ux and with javascript functionialty to so the store owner potential to add more functionality to the site, to raise interaction.

# User Experience/User Interface (UX/UI)

## First Time user goals:

When the visitor first visits the restaurant booking system:

* The homepage should be clear of what the websites goals are.
* The webpage will clearly show you what you can buy, with various ways to access the products list.
* When you chose a item, you should be able to pick how many you would like to pick. You can do this on click of the product, or at the bag/checkout.
* The header and footer should be clear and easy for the customer to navigate.
* The customer should be able to make a account.
* The logged in user should be able to create testimonials.
* The user should be able to toggle the shopping basket, if they wish to add or delete.
* There should be clear pictures and information of the uses of the oil.
* The customer should be able to securely pay for a item.
* The customers log in information and payment information is protected.
* The customer can fill out a contact form and contact the website.
* The customer while logged in should be able to 'like' and then 'dislike' the info pages post.
* The customer can navigate to a bespoke facebook page, directly through the site.
* The customer should be able to sign up to a newsletter.
* A logged in customer will be able to edit, update, create and delete there own testimonials.
* A star rating is visable next to each product which is interactive.

## Frequent Visitor goals:

* There should be a place where customers can sign up and/or log in, if they wish.
* The customer should be able to browse, shop and pay for items on the site securely.
* The site should be accessible, with or without a account.
* The site should promote business and give explanantion on what the product is and why it promotes health, this should generate more sales.
* The site works as a information site as well as a shop. 
* The website linking to social media and newsletters promotes business and sales.
* The site should be a place where customers can find out information about the product.
* The customer should trust the product, due to the information provided in the site.
* Customer contact should be smooth, the website should receive all messages, through a contact page 
* A logged in user should be able to create, update and delete there own testimonials.
* The store ownwer should able to add a product through the site interface and the private admin.
* The user should be able to update the bag by adding or removing products.
* The user should be able to log in and the bag remember its contents.
* The logged in user should be able to save its delivery information.
* The shopper should be able to read testimonials and the info page, but cannot add testimonial or like the article.
* The logged in user should be able to like the info article, then these likes will be registered in sql database, for use of the store owner, for  a extra avenue to look at site productivity.
* The user should get feedback from the site that there message has been send through the contact page. 
* The store owner through the admin should be able to delete irrevalent testimonials.
* The store owner should be able to see all orders through the admin page.
* The store owner will be able to see all listed profiles in the admin.
*  

## Website owner goals:

* Provide a place the website owner can freely edit at anytime(admin page)
* Provide health advice to customers.
* Provide a affordable product.
* Provide a product and a sharing network.
* Promote the uses of herbal oils.
* Generate sales through trust and pricing.


# Color Scheme

The colour scheme is that of a white background to keep things professional and then pops of colour in the site. The colours will be based upon more natural hues, such as:

* blue in some places, but mostly green as a base color of the site.
* normal shade of white
* basic shade of black

  The reason for the colour choice is a health product, so it made sense to use more natural colours from nature.

# Typography

I choose the font 'lato' this font has a nice clear look, which is a little bit like clear fancy handwriting, this stands out well and fits the style of the restaurant.

# User Story

 ## Section 1

 ![Skärmbild (500)](https://github.com/hnjw-png/oregano-oil/assets/120515252/6ac45ee8-e4b7-43fe-854b-215833ebd49e)

 ## Section 1

 ![Skärmbild (502)](https://github.com/hnjw-png/oregano-oil/assets/120515252/5e8328fe-d1c8-4c0f-bf03-20c5e5eb1e7c)

 ## Section 2

 ![Skärmbild (501)](https://github.com/hnjw-png/oregano-oil/assets/120515252/a9579eb5-de83-41c3-bfcc-203d41e74051)

 ### Section 2
 
![Skärmbild (503)](https://github.com/hnjw-png/oregano-oil/assets/120515252/01e38a38-8ca7-4628-85c8-2d13c2b1811c)

# Diagram of Website Structure

![Skärmbild (504)](https://github.com/hnjw-png/oregano-oil/assets/120515252/3a3872a4-06ef-4b77-a8d1-1e2740d16e28)



# Wireframes
![Skärmbild (505)](https://github.com/hnjw-png/oregano-oil/assets/120515252/7a119086-8eb1-4839-b7ef-9ad5aaba5acc)

![Skärmbild (506)](https://github.com/hnjw-png/oregano-oil/assets/120515252/df6ecc05-d301-4f37-9303-19877bcdf7bc)

![Skärmbild (508)](https://github.com/hnjw-png/oregano-oil/assets/120515252/60c863bf-c13e-4e8c-b83b-4e3b9abfa691)

![Skärmbild (509)](https://github.com/hnjw-png/oregano-oil/assets/120515252/f7de9bfd-6725-4d0a-8e4c-a0a116d1ea47)

![Skärmbild (510)](https://github.com/hnjw-png/oregano-oil/assets/120515252/999116dd-37c3-42a1-adc3-3df575cba4c2)

![Skärmbild (511)](https://github.com/hnjw-png/oregano-oil/assets/120515252/e60d8179-54e9-49d6-abb1-9b202846f7d8)

![Skärmbild (512)](https://github.com/hnjw-png/oregano-oil/assets/120515252/88c0b62f-327e-4728-91ac-861965357efe)

![Skärmbild (513)](https://github.com/hnjw-png/oregano-oil/assets/120515252/9f521dbd-560f-44e3-b1b0-2498afa882ef)

![Skärmbild (515)](https://github.com/hnjw-png/oregano-oil/assets/120515252/fd6e67c2-7adf-479c-82fc-b93d20593b67)

![Skärmbild (516)](https://github.com/hnjw-png/oregano-oil/assets/120515252/863ac89c-8805-4e3d-bef7-529a770dbf45)

![Skärmbild (517)](https://github.com/hnjw-png/oregano-oil/assets/120515252/eab31038-c7d8-47dc-9b98-72b0e1af5f62)

![Skärmbild (518)](https://github.com/hnjw-png/oregano-oil/assets/120515252/ae1e22bf-39f8-4575-a86c-a45c6128b16c)



## Features

# Responsiveness:

This website fits to size on all types of devices. From laptop to mobile phone. 

![Skärmbild (523)](https://github.com/hnjw-png/oregano-oil/assets/120515252/51c26dc1-56b7-45c0-bce2-0fa8c67c0ffe)


# Features:

## Sign up Page:

![Skärmbild (524)](https://github.com/hnjw-png/oregano-oil/assets/120515252/aff6cc6f-06c2-4b8f-a72e-8b58d2803897)



# Log in Page:

![Skärmbild (556)](https://github.com/hnjw-png/oregano-oil/assets/120515252/d218214f-4b73-40cc-aa30-cc54b1d52fdf)


## Verify email 

![Skärmbild (557)](https://github.com/hnjw-png/oregano-oil/assets/120515252/716d7aa5-a5a1-4001-bfaf-fb22bbce8f56)

## Sign out message

![Skärmbild (555)](https://github.com/hnjw-png/oregano-oil/assets/120515252/c9470936-36c1-4be2-8d78-fc148b3cbf0a)

# Sign out 

![Skärmbild (554)](https://github.com/hnjw-png/oregano-oil/assets/120515252/860b4b95-3e95-4531-a19a-60aaaa22e1bd)

# Profile

![Skärmbild (553)](https://github.com/hnjw-png/oregano-oil/assets/120515252/a8881c12-e95b-44e2-a293-a65a28c89115)

# Product Manaagement

![Skärmbild (552)](https://github.com/hnjw-png/oregano-oil/assets/120515252/c75e0135-b50e-4771-a9a9-e9d5e238d5f9)

# Account Options

![Skärmbild (551)](https://github.com/hnjw-png/oregano-oil/assets/120515252/9efc492a-a526-41fe-9183-38ba8132796f)

# Search Bar

![Skärmbild (550)](https://github.com/hnjw-png/oregano-oil/assets/120515252/a6f4d6ad-43e2-44d8-93e5-ee0aee11a6e2)

# Nav Bar

![Skärmbild (549)](https://github.com/hnjw-png/oregano-oil/assets/120515252/e9810830-8f3e-4c64-878f-c9c14dabf9d5)


### Shop now button


![Skärmbild (548)](https://github.com/hnjw-png/oregano-oil/assets/120515252/778b6635-4a5d-4eaf-a06b-16e5c3966234)



### Homepage:

![Skärmbild (528)](https://github.com/hnjw-png/oregano-oil/assets/120515252/cc504bde-b752-4c36-be73-7a0fb98de884)



# Basket:

![Skärmbild (534)](https://github.com/hnjw-png/oregano-oil/assets/120515252/af08fced-d47a-43b8-8004-e1d47e0c9699)

## Empty Basket

![Skärmbild (536)](https://github.com/hnjw-png/oregano-oil/assets/120515252/c874901e-8b31-4af6-b2ed-3454220dfe0f)


# Info

![Skärmbild (537)](https://github.com/hnjw-png/oregano-oil/assets/120515252/2bf1d2f6-777c-48b9-9b8d-19ac9db1c4d1)

## Likes feature

![Skärmbild (538)](https://github.com/hnjw-png/oregano-oil/assets/120515252/468ba0b8-ce92-4939-9d57-a24537026a5b)


# Admin page:

![Skärmbild (558)](https://github.com/hnjw-png/oregano-oil/assets/120515252/36afa22b-25b8-457f-83c2-7a0a87649333)

![Skärmbild (527)](https://github.com/hnjw-png/oregano-oil/assets/120515252/f8ee2ed0-5340-4c12-bd5b-ac0a551679db)

![Skärmbild (526)](https://github.com/hnjw-png/oregano-oil/assets/120515252/78893928-b82f-4304-ba70-9e53ca19fc11)


# Contact Us Form

![Skärmbild (539)](https://github.com/hnjw-png/oregano-oil/assets/120515252/26487133-346c-4f53-8f7d-865a4d0cee76)

## Successful Contact page

![Skärmbild (540)](https://github.com/hnjw-png/oregano-oil/assets/120515252/891cc2c4-ccfe-4625-ae64-8a809cfc3853)


# Testimonials details

![Skärmbild (533)](https://github.com/hnjw-png/oregano-oil/assets/120515252/0db53efd-7d57-43de-9ae8-86f6eb618654)

## Testmonial Form

![Skärmbild (532)](https://github.com/hnjw-png/oregano-oil/assets/120515252/97b1441d-db5e-4c28-847a-1ae9d8434783)


# Testimonials Page

![Skärmbild (559)](https://github.com/hnjw-png/oregano-oil/assets/120515252/bc540b91-7ea9-4a0e-8555-cafea9b695c9)


# Product Details Display

![Skärmbild (542)](https://github.com/hnjw-png/oregano-oil/assets/120515252/1f1f4526-7195-4c0b-ad7a-6a938f0ba94f)

## Product Star Rating ux 

![Skärmbild (541)](https://github.com/hnjw-png/oregano-oil/assets/120515252/bc6cd6b9-c4c8-45ca-ae21-fe3b44c161bf)


# Product Shopping bag

![Skärmbild (544)](https://github.com/hnjw-png/oregano-oil/assets/120515252/681bf75c-40db-4bd3-98fc-829976ff91b9)

# Added Product to Bag

![Skärmbild (543)](https://github.com/hnjw-png/oregano-oil/assets/120515252/b8d6f8a1-9951-4ab1-93f1-f5055f947025)

# Footer/ Mail Chimp Newsletter Sign up

![Skärmbild (547)](https://github.com/hnjw-png/oregano-oil/assets/120515252/d4cdacda-81f1-4dc1-aa6f-8da31e2afb4c)


# Techologies used

Languages used:

* HTML
* CSS
* PYTHON
* DJANGO
* JAVASCRIPT

# Applications used:

* Google Fonts fonts downloaded from Google Fonts.
* Fontawesome icons downloaded from Font Awesome.com.
* GitHub to store the projects code.
* Gitpages to deploy the site.
* Chrome Developer Tools for layout and responsive testing.
* W3 Validator to test html and css code.
* In future a favicon can be added.

## Sources
Django help sheet, code institute material, stack overflow and tutoring advice. I had help from a tutor to set up my env.py file. And I go advice on heroku, and he helped me fix a bug as I duplicated my app.

# Testing
* See below table of tests:

# Section 1 ( what it should do, and results, the first half)
![Skärmbild (562)](https://github.com/hnjw-png/oregano-oil/assets/120515252/ef22f8d2-71a8-4ef6-8889-815c8193e1ed)

![Skärmbild (572)](https://github.com/hnjw-png/oregano-oil/assets/120515252/135c1d56-af59-4366-b837-1918541b618e)

## Section 2 (the second half)
![Skärmbild (563)](https://github.com/hnjw-png/oregano-oil/assets/120515252/b7aee9c0-3782-480d-bddc-1413b587dea5)

![Skärmbild (573)](https://github.com/hnjw-png/oregano-oil/assets/120515252/92236bde-2c35-4246-99b3-8e574e5692e3)

# Lighthouse: 

* Lighthouse app does not work on my laptop, but from own testing the website fulfils all needs for the store owner, customer, and logged in user. The website is set to change when used on smaller mobile screens etc. Does not take a long time to load and all images and functions are working. A later improvement would be to check with lighthouse.

# CSS and HTML Validator:

* There are some errors inside the html validator but it does not effect the overall effectivity of the site. These error things like aria labels , but they effectively in the website. These errors in the future can be fixed, but its made slighty difficuly by there being some mnay pages, ad the validator does not specify which file. To fix these errors would be a future improvement to the site.

* There are 15 errors in the html, which do no effect the functionailty of the site, in the future these coud be fixed, to keep good work manner.

* There is one error inside the css validator, but this small error certainly effect the overall functionality of the site.

* ![Skärmbild (582)](https://github.com/hnjw-png/oregano-oil/assets/120515252/f9dbd7eb-aa01-419f-9116-608ffac36ee8)


# DEPLOYMENT

* I have deployed my project to heroku, I did this using the heroku to connect to github repository. I have set heroku to automatic deploy so it automatically uodates when the website is the git push command is written within the project.
*  Here is the link: https://oreganooil1-2ce75722cde3.herokuapp.com/.

* In order to deploy e-commerence website I needed to fill out some config vars. I have added links and passwords for email hosting, hosting, the sql database, the cloudinary storage for static files, the secret key etc.

* During development disable collect static was on and debug was set to true for the purposes of editting the website and viewing errors. But when the site is deployed to heroku, diasble collect needs to be removed and debug set to false in the settings.py inside the project. This is also insures the 404 page appears too  if there was a error.

* A env.py file has been added. Containing the cloudinary url, the database url, the secret key and lastly the devolopment set to 1.

* A Procfile has been added, where the gunicore, wsgi link has been added.

* I deployed the site manually through heroku, by connecting it to my guthub repository.


# Bug fixes

* In the future, the star rating system will be more than just a interactive color changing addition to the product details.  In the future the star rating system will give feedback to the user that they have rated the product.

* Another addition could be instead of a direct message, the logged in user could be directed to a review page, where the user has the option to file out a form with a review, as well or leave a star rating.

* This the star rating ux using javascript, is used to showcase a potential new feature to the site.

* The likes mmodel seems to forget its amount of likes until clicked by a logged in user.

* Though the likes model gives the store owner the oppurtunity to view the amount of likes given by a user or many users through the sql database or through clicking the user in the admin panel.

* In the future update the likes model wil be improved so that its more easily accessible in the admin panel. In the website the likes section will be improved by it remembering its amount of likes before being cliked by the user.

* The confirmation email should be improved by adding companies details instead of saying 'example'.

* The heroku link is : 
https://oreganooil1-2ce75722cde3.herokuapp.com/

## images pixabay (credits)

https://pixabay.com/sv/photos/oregano-%C3%A4ng-n%C3%A4rbild-blomning-rosa-7317396/

https://pixabay.com/sv/photos/oregano-l%C3%B6v-gr%C3%B6n-h%C3%A4lsa-gr%C3%B6n-h%C3%A4lsa-4338622/

https://pixabay.com/photos/oil-garlic-food-fresh-spices-cook-1382420/

https://pixabay.com/sv/photos/oregano-l%C3%B6v-%C3%B6rter-l%C3%B6vverk-f%C3%A4rsk-2662890/

https://pixabay.com/sv/photos/tr%C3%A4dg%C3%A5rd-jorden-golv-sten-%C3%B6rtsten-731561/

https://pixabay.com/sv/photos/familj-grundl%C3%A4ggande-utrustning-5227815/

https://pixabay.com/sv/photos/%C3%B6rter-oregano-timjan-salvia-2126283/
