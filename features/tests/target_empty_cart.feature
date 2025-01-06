# Created by Gregory at 1/4/2025
Feature: Tests Scenarios for Cart Functionality


  Scenario: User can see cart is empty message when clicked on
    Given  Open target page
    When   Click on cart icon
    Then   Verify Your cart is empty
