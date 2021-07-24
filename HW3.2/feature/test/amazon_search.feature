#2. Update a test case for support search using BDD
#User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)

Feature: Test Amazon search

  Scenario: User can search for a product
    Given Launch chrome browser
    When Open Amazon page
    When Input Table in search field
    When  Click on Amazon search icon
    Then Verify search worked
    Then  Close browser