## 1. Brainstorm a list of features that you'd like the finished product to have. You are not expected to finish all, or even most, of the features you come up with. The goal is just to come up with some fun ideas that you can work towards. Add a docs folder to you repository and include this list as a markdown file.

### Features:

    - A list of all available cards
    - List of currently owned cards
    - List of cards not yet obtained, but that you want to collect (wishlist)
    - Ability to add/remove cards to you collected list and wanted list
    - Ability to share your wanted list as an exported file
    - Persistent data with login credentials
    - Prices shown based on recent ebay sold
    - Sort functionality based on card attributes

## 2. Define the MVP (Minimum viable product) for your project. Out of your list of features select the most important subset. You will be expected to complete implementation of this list so try to keep the set of tasks manageable. Aim for something that you think can be completed in 2-4 weeks. Include the resulting list in your docs directory.

### MVP:

    - Persistent data with login credentials
    - A list of all available cards
    - List of currently owned cards
    - Ability to add/remove cards to you collected list

## For each of the features that are to be included in the MVP, create one or more User stories. You'll estimate these tasks as part of your first sprint, so you don't need to be too precise yet, but try to keep them small. Any story that will take more than a week should be broken into multiple smaller stories if possible. Follow the user stories guidelines discussed in lecture. To track these user stories we'll be using GitHub Issues. Create an Issue for each user story in your project. All group member must create at least one user story.

### Story 1: Full catalog

As a user, I should be able to view every card that is collectable, so that I can make decisions about which cards I want to collect next.

### Story 2: Current collection

As a user, I want to keep track of all the cards in my collection, so that I know which cards I already have and don’t have to worry about getting duplicates accidentally.

### Story 3: Add/Remove

As a user, I want to update my collection in the app whenever I obtain or get rid of cards in real life, so that I can keep track at a glance in the app.

### Story 4: Persistent data with login

As a user I want to be able to have credentials for my account so that my collection is available each time I log in.

## 4. Discuss the overall structure your project will have. It's a good idea to break the project into several files in order to simplify the process of multiple people contributing to the project.

### Python Flask app

    - app.py
    - Templates
        - Layout.html (everything extends)
        - Login.html
        - Index.html
        - collection.html
        - catalog.html

### Database

    - PostgreSQL (tie google credentials to their account)

### External API

    - pokemontcg.io (https://docs.pokemontcg.io/)

### Login Credentials:

    - Flask-o-authlib
