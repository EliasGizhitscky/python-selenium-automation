
Feature: Test for check autorization

  Scenario: Logged out user sees Sign in page when click on Start selling button
    Given Open Amazon page
    When Click on start selling button
    Then Verify Sign in page is opened

