# Django: Commerce

### Sigrid van Klaveren - 14080702

### Minor Programmeren

An implementation of an auction website. On this website people can create an account and log in. When logged in people can do several things:
- View active listings
- Create new listings
- Place a bid or comment on a listing
- Add or remove items to/from watchlist
- Owner of a listing can close this listing


## Getting Started

Run the following command in your terminal:
`python -m pip install -r requirements.txt`


## Screen Designs

### Default screen
![Default page](/auctions/design_document/sketches/Default%20screen%401x.png)

### Create Listing screen
![Create Listing](/auctions/design_document/sketches/Create%20Listing%401x.png)

### Active Listing screen
![Active Listing](/auctions/design_document/sketches/Active%20Listing%401x.png)

### Categories screen
![Categories](/auctions/design_document/sketches/Categories%20screen%401x.png)


## Navigation between screens

### Navigation bar
These buttons are almost (always) present, depending on if the user is logged in or not
- 'Active listings' button: always returns to the default page
- 'Categories' button: takes the user to a page with all the available categories
- 'Log Out' button: logs out a user 
- 'Create Listing' button: takes the user to a page where they can make a new listing
- 'Watchlist' button: takes the user to their watchlist

### Default screen
- 'Log in' or 'Log in here' button: a log in form appears on the default screen where the user can fill in their username and password
- 'Register' or 'Register here' button: a register form appears on the default screen where the user can give a username, email address and password
- If the user clicks on one of the active listings on the page, they are taken to the page of that specific listing.

### Active Listing Screen
- 'Place Bid' button: confirms the bid the user filled in. The user stays on the page.

### Create Listing Screen
- 'Save' button: saves the filled in information from the new listing and takes the user to the active listing screen of that listing.

### Categories Screen
- Every category is a button. --> TO WHAT PAGE?

## Models - Class Diagram
Underneath is the Class Diagram for this project. All the models used in this project are shown in the diagram. Underneath the names of the models, all the information we want to save in our database is listed. The arrows show the relationships between the different models.

![Class Diagram](/auctions/design_document/sketches/Schermafbeelding%202022-05-10%20om%2014.47.51.png)

## Database information usage
This section explains per model in the database which page uses this information

### User
This information is needed on every page to see which user is logged on. When no user is logged on, it is needed to log in. It is also used to display current or previous bids by whom they are done and also to show who posted a certain comment.

### Auction Listing
This information is used on the default page, the page of a specific listing. The page where the user creates a listing add to this part of the database as well. Also the categories page uses this information to list all the categories.

### Comments
This information is used on the page of one specific auction listing.

### Bid
This information is used on the default page and the page of a specific auction listing.










