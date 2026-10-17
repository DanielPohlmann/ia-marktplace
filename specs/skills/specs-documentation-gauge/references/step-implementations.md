<!-- Part of the specs-documentation-gauge skill. Loaded on demand from SKILL.md. -->

# Step Implementations

## JavaScript / TypeScript
```javascript
const { Step, BeforeSuite, AfterSuite } = require('gauge-ts');
const { openBrowser, closeBrowser, goto, click, write, into, textBox, text } = require('taiko');

Step('Navigate to the login page', async () => {
    await goto('https://app.example.com/login');
});

Step('Enter username <username>', async (username) => {
    await write(username, into(textBox({ id: 'email' })));
});

Step('Enter password <password>', async (password) => {
    await write(password, into(textBox({ id: 'password' })));
});

Step('Click the login button', async () => {
    await click('Login');
});

Step('Verify the dashboard is displayed', async () => {
    assert.ok(await text('Dashboard').exists());
});
```

## C# (.NET)
```csharp
using Gauge.CSharp.Lib.Attribute;
using FluentAssertions;

public class LoginSteps
{
    [Step("Navigate to the login page")]
    public void NavigateToLogin()
    {
        // navigate to login page
    }

    [Step("Enter username <username>")]
    public void EnterUsername(string username)
    {
        // type username into field
    }

    [Step("Enter password <password>")]
    public void EnterPassword(string password)
    {
        // type password into field
    }

    [Step("Verify the error message <message> is displayed")]
    public void VerifyErrorMessage(string message)
    {
        // assert error message
    }
}
```

## Python
```python
from getgauge.python import step, before_suite, after_suite

@step("Navigate to the login page")
def navigate_to_login():
    # navigate to login page
    pass

@step("Enter username <username>")
def enter_username(username):
    # type username into field
    pass

@step("Enter password <password>")
def enter_password(password):
    # type password into field
    pass

@step("Verify the dashboard is displayed")
def verify_dashboard():
    # assert dashboard is visible
    pass
```

## Java
```java
import com.thoughtworks.gauge.Step;

public class LoginSteps {
    @Step("Navigate to the login page")
    public void navigateToLogin() {
        // navigate to login page
    }

    @Step("Enter username <username>")
    public void enterUsername(String username) {
        // type username into field
    }

    @Step("Enter password <password>")
    public void enterPassword(String password) {
        // type password into field
    }

    @Step("Verify the dashboard is displayed")
    public void verifyDashboard() {
        // assert dashboard is visible
    }
}
```
