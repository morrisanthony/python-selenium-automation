# Created by Gregory at 1/7/2025
Feature: Test for 10 benefit cells

  Scenario: User can open target circle page and see 10 benefit cells
    Given Open target circle page
    When  Inspect page for the element that shows 10 benefit cells
    Then  Verify at least 10 benefit cells

