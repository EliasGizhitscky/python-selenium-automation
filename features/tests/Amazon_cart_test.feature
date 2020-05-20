# Created by Elias at 19.05.2020
Feature: Cart test

  Scenario: Verify that the cart is empty
      Given Open Amazon page
      When Click on a cart icon
      Then Verify that the cart is empty