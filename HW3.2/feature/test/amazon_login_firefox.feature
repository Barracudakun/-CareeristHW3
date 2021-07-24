Scenario: User can login Amazon account from Firefox
    Given Launch Firefox browser
    When Open Amazon page
    And Click Amazon sign in section
    And  Enter Email "yingxukun@gmail.com"
    And Click Continue button
    And Enter Password "Wanghong1959"
    And Click Sing-in button
    Then User must successfully login the your account page