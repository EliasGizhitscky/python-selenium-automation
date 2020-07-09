
Feature: Test for check autorization

  Scenario: Logged out user sees Sign in page when click on Start selling button
    Given Open Amazon page
    When Click on Sell button
    And Click on Sign Up button
    Then Verify Sign in page is opened

