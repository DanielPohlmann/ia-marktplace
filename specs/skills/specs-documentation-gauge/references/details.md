<!-- Part of the specs-documentation-gauge skill. Loaded on demand from SKILL.md. -->

# Gauge — details

## CLI Reference

```bash
# Install Gauge
npm install -g @getgauge/cli
# or: brew install gauge

# Initialize a new project
gauge init js        # JavaScript
gauge init csharp    # C#
gauge init python    # Python
gauge init java      # Java

# Run all specs
gauge run specs/

# Run specific spec file
gauge run specs/checkout.spec

# Run by tags
gauge run --tags "smoke" specs/
gauge run --tags "checkout & !wip" specs/

# Run in parallel
gauge run --parallel -n 4 specs/

# Validate specs (check for unimplemented steps)
gauge validate specs/

# List unimplemented steps
gauge --unimplemented specs/

# Install plugins
gauge install html-report
gauge install xml-report
gauge install json-report
```
