# Created by Gregory at 1/4/2025
Feature: Tests Scenarios for Cart Functionality


  Scenario: User can see cart is empty message when clicked on
    Given   Open target main page
    When    Click on cart icon
    Then    Verify Your cart is empty


   Scenario: User can add any Target’s product into the cart, and make sure it’s there
    Given    Open target main page
     And     Search for coffee
    When     Click on item and add to cart
    And      Confirm add to cart button on side navigation bar
    And      Open the cart page
    Then     Verify that the item is in the cart
