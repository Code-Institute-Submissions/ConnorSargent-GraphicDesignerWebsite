# Graphic Designer Website

This website has been created to allow a graphic designer to showcase and sell their work/prints and also allows customers to request custom artworks. The deployed site can be viewed [here]()

![Responsive]()

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## UX
This website has been created using Django for the backend. The design is my own inspired by the graphic designers work utilizing bootstrap.

### User Stories

### Viewing/Navigation
| ID 	| AS A/AN 	| I WANT TO BE ABLE TO...                                   	| SO THAT I CAN...                                          	|
|----	|---------	|-----------------------------------------------------------	|-----------------------------------------------------------	|
| 1  	| Shopper 	| View all products and services                            	| Purchase one or more product/service                      	|
| 2  	| Shopper 	| View individual product and service details               	| Identify a product/service: Price, Description, Image     	|
| 3  	| Shopper 	| View owner portfolio                                      	| View owners previous work, before purchasing              	|
| 4  	| Shopper 	| View the total for all products/services in shopping cart 	| View total price of all products/services I wish to order 	|

### Registration/User Accounts
| ID 	| AS A/AN   	| I WANT TO BE ABLE TO...                               	| SO THAT I CAN...                                           	|
|----	|-----------	|-------------------------------------------------------	|------------------------------------------------------------	|
| 1  	| Site User 	| Register an account                                   	| Purchase products/services                                 	|
| 2  	| Site User 	| Have a user profile                                   	| View order history and update payment/shipping information 	|
| 3  	| Site User 	| Log in/Log out                                        	| Keep my personal information safe                          	|
| 4  	| Site User 	| Recover Password                                      	| Recover access to account if password forgotten            	|
| 5  	| Site User 	| Receive email confirmation for registering an account 	| Verify my account was successfully registered              	|

### Sorting And Searching
| ID 	| AS A/AN 	| I WANT TO BE ABLE TO...                          	| SO THAT I CAN...                               	|
|----	|---------	|--------------------------------------------------	|------------------------------------------------	|
| 1  	| Shopper 	| Sort through a list of products/services         	| Identify which product/service I want          	|
| 2  	| Shopper 	| Search for a product/service by name/description 	| Find a specific product/service                	|
| 3  	| Shopper 	| View search results                              	| See all products/services that match my search 	|

### Purchasing And Checkout
| ID 	| AS A/AN 	| I WANT TO BE ABLE TO...                                            	| SO THAT I CAN...                                         	|
|----	|---------	|--------------------------------------------------------------------	|----------------------------------------------------------	|
| 1  	| Shopper 	| Select options and quantities of products/services during checkout 	| Ensure no mistakes were made during purchasing           	|
| 2  	| Shopper 	| View items in cart before purchase                                 	| Identify total items and price before purchasing         	|
| 3  	| Shopper 	| Easily enter payment information                                   	| Checkout easily                                          	|
| 4  	| Shopper 	| View order confirmation after checkout                             	| Ensure no mistakes were made during the checkout process 	|
| 5  	| Shopper 	| Receive order confirmation email after checkout                    	| Easily keep order information for personal records       	|

### Admin and Management
| ID 	| AS A/AN         	| I WANT TO BE ABLE TO...           	| SO THAT I CAN...                                                          	|
|----	|-----------------	|-----------------------------------	|---------------------------------------------------------------------------	|
| 1  	| Owner/Superuser 	| Add new products/services         	| Add new products/services                                                 	|
| 2  	| Owner/Superuser 	| Edit/Update products and services 	| Change all aspects of a product/service eg. Price, Description, Image ... 	|
| 3  	| Owner/Superuser 	| Delete product/service            	| Stop the sale of a specific product/service                               	|
| 4  	| Owner/Superuser 	| View customer orders              	| View customers address and purchased products in order to ship            	|
| 5  	| Owner/Superuser 	| Receive messages for custom orders  | See specifics for custom order requests           	                        |

### Design
- This website uses Django with Jinja templates utilizing built in Django functionality.

- The styling is mostly based upon the Bootstrap with some custom CSS to make the website feel more personal. 
    
- Font Families (Google Fonts):
  - [FontName]()
  - [FontName]()

### Wireframes
Below are the wireframes used to design the app layout.

#### Home
![wireframe for home page](static\wireframes\WireframesHome.png)

#### Log in
![wireframe for login](static\wireframes\WireframesLogin.png)

#### Profile
![wireframe for profile page](static\wireframes\WireframesProfile.png)

#### Contact
![wireframe for  page](static\wireframes\WireframesContact.png)

#### Store
![wireframe for  display](static\wireframes\WireframesStore.png)

#### Product
![wireframe for  display](static\wireframes\WireframesProduct.png)

#### Product Management
![wireframe for  display](static\wireframes\WireframesProductManagement.png)

### Wireframe changes 
 - 
 
### Database
Below is a tabulated representation of the database that i have chosen to use in this application.

![database]()

