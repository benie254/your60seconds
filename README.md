# thePitcher

A pitch CRUD (Create,Read,Update,Delete) app, generated with [Python](https://www.python.org/) version 3.8.13 && [Flask](https://flask.palletsprojects.com/en/2.1.x/) version 1.1.4 

# thePitcher
#### This repo creates an app that utilizes a database connection to save posted pitches and comments, besides update user information.
## Author
[Benson Langat](https://github.com/benie254)

## Description

thePitcher is built on a database, which helps us store user data and information. Users have the initial option to view all pitches. To create a pitch, users must log in or create a new account. Once logged in, users can share pitches, commment on them, or update their profiles.

## Screenshot

<img src="https://user-images.githubusercontent.com/99865051/168407909-9fe76430-7b5c-442f-b76e-f75d1ba6af1e.png" >

## Screenshot #2

<img src="https://user-images.githubusercontent.com/99865051/168407922-023079e5-1e2e-4d51-b66a-079099abfe22.png">

## Behavior Driven Development--BDD

**1. Home Page**
   - OUTPUT: 'Navbar, Welcome message, Sidebar, Home page content'
   
**2. User Action:** 
   - INPUT:  Click : Navbar : 'thePitcher', 'HOME'
   - OUTPUT: Home page
   - OUTPUT: All Pitches
   - OUTPUT: Sidebar--News Sources
   
**3. User Action:**
   - INPUT:  Click : Navbar : 'Create pitch'
   - OUTPUT: Pitch--create pitches page
   - OUTPUT: Pitch form
   
**4. User Action:**
   - INPUT:  Click : Navbar : 'Sign in'
   - OUTPUT: Login page
   - OUTPUT: Login form + user message to 'Sign up'
   
**5. User Action:**
   - INPUT:  Click : user message : 'Sign up'
   - OUTPUT: Sign up page
   - OUTPUT: Sign up form 
   - OUTPUT: Redirect to 'Login' page.
   
**6. Login Form:**
   - OUTPUT: 'Email:','Password:','Login'
   - INPUT:  user's email address, user's password, click/ENTER
   - OUTPUT: Home page
   
**7. User Action:**
   - INPUT:  Click : Navbar : 'Profile'
   - OUTPUT: User profile page
   - OUTPUT: User photo upload areas
   - OUTPUT: User bio section_name
   - OUTPUT: User's pitches
   
**8. User Action:**
   - INPUT:  Click : 'Edit Profile' 
   - OUTPUT: Profile update page
   - OUTPUT: profile update form--on submit, redirect to home page
   
**9. User Action:**
   - INPUT:  Click : Browser Page : Close
   - Exits


## Setup/Installation Requirements

* To use this open-source repo, clone it; to contribute, fork it. 
* Open your Terminal (CTRL + ALT + T on Ubuntu/Linux). 
* Make a destination directory in your preferred path (where you would like to clone the repo into.)
* Run the command ``` cd yourDestinationDirectory ```
* Run the command ``` git clone https://github.com/benie254/your60Seconds.git ``` to clone the repo into your destination directory. 
* Run the command ``` cd your60seconds ``` to move you into this repo's directory.
* Run the command ``` atom . ``` for Atom or ``` code . ``` for VSCode --opens the directory in your preferred code editor. (it is okay if you use something different.)
* Happy coding!

## Known Bugs

No known bugs. Please report any issues or encountered bugs! 

## Technologies Used

* [Python](https://www.python.org/) 
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)

## Other Resources 

* [Bootstrap](https://getbootstrap.com/) -- page designs
* [Adobe Color Wheel](https://color.adobe.com/) -- color palette 
* [Coolors](https://coolors.co/ -- color paletter)
* [Google Fonts](https://fonts.google.com) -- stylized fonts


## Support and contact details

Reach out with any issues, concerns, or contributions to [Benie-throughMail](davinci.monalissa@gmail.com)

### License

*Copyright (c) 2022* ***Benson Langat***

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.*

###
Copyright (c) 2022 **Benson Langat**

[Python](https://www.python.org/) version 3.8.13
