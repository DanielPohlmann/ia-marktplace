<!-- Part of the dev-craftsmanship-clean-code skill. Loaded on demand from SKILL.md. -->

# Functions

## Small Functions
Functions should be small. Then they should be smaller than that. A function should do **one thing**, do it well, and do it only.

## One Level of Abstraction
Statements within a function should all be at the same level of abstraction. Do not mix high-level policy with low-level detail.

```typescript
// Bad — mixed levels of abstraction
function renderPage(data: PageData): string {
    let html = "";
    html += "<html><head><title>" + data.title + "</title></head>";
    if (data.isTestPage) {
        const setup = findInheritedPage("Setup");
        html += setup.getContent();
    }
    html += data.content;
    return html;
}

// Good — consistent abstraction
function renderPage(data: PageData): string {
    const header = buildHeader(data.title);
    const setupContent = includeSetupIfTestPage(data);
    const body = buildBody(data.content);
    return assembleHtml(header, setupContent, body);
}
```

## Command-Query Separation
Functions should either **do something** (command) or **answer something** (query), but not both.

```typescript
// Bad — command and query mixed
function set(attribute: string, value: string): boolean {
    // sets the value AND returns whether the attribute existed
}

// Good — separated
function attributeExists(attribute: string): boolean { /* ... */ }
function setAttribute(attribute: string, value: string): void { /* ... */ }
```

## Function Arguments
The ideal number of arguments is zero (niladic), followed by one (monadic), then two (dyadic). Three arguments (triadic) should be avoided where possible. More than three requires very special justification.

```typescript
// Bad — too many arguments
function createMenu(title: string, body: string, buttonText: string, cancellable: boolean): Menu { /* ... */ }

// Good — use a parameter object
interface MenuOptions {
    title: string;
    body: string;
    buttonText: string;
    cancellable: boolean;
}
function createMenu(options: MenuOptions): Menu { /* ... */ }
```

## Avoid Side Effects
A function that promises to do one thing but also does other hidden things creates temporal coupling and order dependencies.

```typescript
// Bad — hidden side effect (initializes a session)
function checkPassword(userName: string, password: string): boolean {
    const user = findUser(userName);
    if (user && user.passwordMatches(password)) {
        Session.initialize(); // side effect!
        return true;
    }
    return false;
}

// Good — make the side effect explicit
function checkPasswordAndInitializeSession(userName: string, password: string): boolean { /* ... */ }
// Or better, separate the two operations
```
