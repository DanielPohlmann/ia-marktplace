<!-- Part of the specs-documentation-gherkin skill. Loaded on demand from SKILL.md. -->

# Step Definitions

Step definitions bind Gherkin steps to executable code. Each runner has its own syntax.

## Cucumber (Java)
```java
import io.cucumber.java.en.*;

public class LoginSteps {
    @Given("a registered user with email {string} and password {string}")
    public void aRegisteredUser(String email, String password) {
        // arrange: create or look up user
    }

    @When("the user submits the login form")
    public void theUserSubmitsTheLoginForm() {
        // act: submit credentials
    }

    @Then("the user should be redirected to the dashboard")
    public void theUserShouldBeRedirectedToDashboard() {
        // assert: verify redirect
    }
}
```

## SpecFlow / Reqnroll (C#)
```csharp
[Binding]
public class LoginSteps
{
    [Given(@"a registered user with email ""(.*)"" and password ""(.*)""")]
    public void GivenARegisteredUser(string email, string password)
    {
        // arrange
    }

    [When(@"the user submits the login form")]
    public void WhenTheUserSubmitsTheLoginForm()
    {
        // act
    }

    [Then(@"the user should be redirected to the dashboard")]
    public void ThenTheUserShouldBeRedirectedToDashboard()
    {
        // assert
    }
}
```

## Behave (Python)
```python
from behave import given, when, then

@given('a registered user with email "{email}" and password "{password}"')
def step_given_registered_user(context, email, password):
    # arrange
    pass

@when('the user submits the login form')
def step_when_submit_login(context):
    # act
    pass

@then('the user should be redirected to the dashboard')
def step_then_redirected_to_dashboard(context):
    # assert
    pass
```

## Cucumber.js (JavaScript/TypeScript)
```javascript
const { Given, When, Then } = require('@cucumber/cucumber');

Given('a registered user with email {string} and password {string}', function (email, password) {
    // arrange
});

When('the user submits the login form', function () {
    // act
});

Then('the user should be redirected to the dashboard', function () {
    // assert
});
```
