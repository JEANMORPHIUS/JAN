# Contributing to JAN Studio

Thank you for your interest in contributing! This document outlines how to contribute effectively.

---

## Development Philosophy

**THE CHOSEN ONE**
**Spiritual Alignment Over Mechanical Productivity**

**THE FOUNDATION:**
We are born a miracle.
We deserve to live a miracle.
Each and every one of us under the Lord's word.

**THE MISSION:**
THIS IS STEWARDSHIP AND COMMUNITY WITH THE RIGHT SPIRITS
LOVE IS THE HIGHEST MASTERY
ENERGY + LOVE = WE ALL WIN
PEACE, LOVE, UNITY

---

## How to Contribute

### 1. Reporting Issues

**Before reporting:**
- Check existing issues
- Verify it's a bug (not a feature request)
- Include reproduction steps

**Issue Template:**
```markdown
**Description:**
[Clear description of the issue]

**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Environment:**
- Python version: [e.g., 3.11]
- OS: [e.g., Windows 10]
- Docker: [Yes/No]
```

### 2. Feature Requests

**Before requesting:**
- Check if feature exists
- Consider if it aligns with project philosophy
- Explain use case clearly

**Feature Template:**
```markdown
**Feature Description:**
[What you want to add]

**Use Case:**
[Why this is needed]

**Proposed Solution:**
[How you'd implement it]

**Alternatives Considered:**
[Other approaches you thought about]
```

### 3. Code Contributions

#### Setup Development Environment

```bash
# Fork and clone
git clone https://github.com/your-username/JAN.git
cd JAN

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
cd jan-studio/backend
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If exists

# Run tests
pytest tests/
```

#### Code Style

- **Format**: Use Black formatter
- **Lint**: Follow PEP 8, use flake8
- **Type Hints**: Add type hints to all functions
- **Docstrings**: Document all public functions

```bash
# Format code
black jan-studio/backend/

# Lint code
flake8 jan-studio/backend/
```

#### Commit Messages

Follow conventional commits:

```
feat: Add Oracle SIYEM integration
fix: Resolve database connection issue
docs: Update API documentation
test: Add unit tests for RNG engine
refactor: Simplify campaign automation
```

#### Pull Request Process

1. **Create Branch**: `git checkout -b feature/your-feature`
2. **Make Changes**: Follow code style guidelines
3. **Write Tests**: Add tests for new features
4. **Update Docs**: Update relevant documentation
5. **Submit PR**: Clear description, link issues

**PR Template:**
```markdown
**Description:**
[What this PR does]

**Related Issues:**
Closes #[issue-number]

**Changes:**
- [Change 1]
- [Change 2]

**Testing:**
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

**Documentation:**
- [ ] Updated README
- [ ] Updated API docs
- [ ] Added code comments
```

---

## Areas for Contribution

### High Priority

1. **Tests**: Unit and integration tests
2. **Documentation**: API reference, tutorials
3. **Examples**: More persona examples
4. **Performance**: Optimization opportunities

### Medium Priority

1. **Features**: New Oracle modes, campaign features
2. **Integrations**: More scheduler support
3. **UI**: Frontend improvements
4. **Localization**: Multi-language support

### Low Priority

1. **Refactoring**: Code cleanup
2. **Tooling**: Development tools
3. **Examples**: More use cases

---

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for our community guidelines.

**Key Principles:**
- Respect all contributors
- Welcome diverse perspectives
- Focus on constructive feedback
- Honor the mission and philosophy

---

## Testing Guidelines

### Unit Tests

Test individual functions:

```python
def test_seed_generation():
    rng = TransparentRNG()
    seed = rng.generate_seed("test", "2026-01-01", "context", "user1")
    assert seed["seed"] is not None
    assert seed["verifiable"] is True
```

### Integration Tests

Test API endpoints:

```python
def test_oracle_cast(client):
    response = client.post(
        "/api/oracle-siyem/cast",
        json={"user_intent": "test", "creative_context": "test"}
    )
    assert response.status_code == 200
    assert "oracle_interpretation" in response.json()
```

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_oracle.py

# With coverage
pytest --cov=jan-studio/backend --cov-report=html
```

---

## Documentation Guidelines

### Code Documentation

- **Module Docstrings**: Purpose and usage
- **Function Docstrings**: Parameters, returns, examples
- **Type Hints**: All function signatures

### User Documentation

- **Clear Examples**: Real-world use cases
- **Step-by-Step**: Detailed instructions
- **Troubleshooting**: Common issues and solutions

---

## Review Process

1. **Automated Checks**: CI/CD runs tests and linting
2. **Code Review**: At least one maintainer reviews
3. **Testing**: Reviewer may test changes
4. **Approval**: Maintainer approves and merges

**Review Criteria:**
- Code quality and style
- Test coverage
- Documentation completeness
- Alignment with project philosophy

---

## Questions?

- **GitHub Issues**: For questions and discussions
- **Documentation**: Check `/docs` endpoint
- **Community**: [Specify channels]

---

**Thank you for contributing! Together we build something meaningful.** 🙏

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**
