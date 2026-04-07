@functional @smoke
Feature: Access Management - Login
  As a medical clinic user
  I want to log into the system with my credentials
  In order to manage my appointments and patients

  Scenario: Successful login and session persistence
    Given the user navigates to the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
    And the session state is saved