
Feature: Test loops


  Scenario: Check for color selection opportunity
    Given Open product B07RL5Z29Z page
    Then Check for color selection of product


  Scenario: Test case to verify, every product on the page has a text ‘Regular’ and a product name
    Given Open Amazon Wholefoodsdeals page
    Then Verify that every product has name and regular price


   Scenario: Test case for links in top nav menu
     Given Open Amazon page
     Then Verify that every link in top nav menu leads to appropriate page