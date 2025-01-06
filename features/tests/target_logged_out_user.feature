# Created by Gregory at 1/4/2025
Feature: Navigation to Sign In

  Scenario: Verify that a logged-out user can navigate to the Sign In page
    Given Open target page
    When  Click sign in
    Given From right side navigation menu, click Sign In
    Then  Verify Sign in form opened
