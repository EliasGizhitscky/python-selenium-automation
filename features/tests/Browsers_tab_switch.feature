# Created by Elias at 17.06.2020
Feature: Yandex test


  Scenario: User can open and close weather tab on yandex
    Given Open yandex homepage
    When Store original window
    And Click on weather link
    And Switch to the  newly opened window
    Then Weather is shown