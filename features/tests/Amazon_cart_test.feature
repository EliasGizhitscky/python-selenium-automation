# Created by Elias at 19.05.2020
Feature: Cart test

  Scenario: Verify that the cart is empty
      Given Open Amazon page
      When Click on a cart icon
      Then Verify that the cart is empty

   Scenario: Verify an item added to the cart
      Given Open Amazon page
      When Searh for Wi-Fi router in searh menu
      And Add the first result to cart
      Then Verify that the number of cart items is 1
