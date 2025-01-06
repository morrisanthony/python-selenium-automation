# Created by Gregory at 12/18/2024
Feature: # Tests for search
  # Enter feature description here

  Scenario: User can search for a product
    Given Open target main page
    When  Search for tea
    Then  Verify search results shown