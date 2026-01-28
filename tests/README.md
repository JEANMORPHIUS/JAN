# JAN Studio Tests

**Test suite for JAN Studio Oracle SIYEM and Campaign Automation systems.**

---

## Running Tests

### All Tests

```bash
pytest tests/
```

### Specific Test File

```bash
pytest tests/test_oracle_rng.py
```

### With Coverage

```bash
pytest tests/ --cov=SIYEM/services --cov=jan-studio/backend --cov-report=html
```

### Verbose Output

```bash
pytest tests/ -v
```

---

## Test Structure

### Unit Tests

- `test_oracle_rng.py`: Transparent RNG engine tests
- `test_oracle_laws.py`: Laws interpreter tests

**Focus:**
- Deterministic behavior (same input = same output)
- Transparency and verifiability
- Law mapping correctness

### Integration Tests

- `test_oracle_integration.py`: Complete Oracle flow tests
- `test_api_endpoints.py`: API endpoint tests

**Focus:**
- End-to-end Oracle casting
- API response structure
- Success metrics calculation

---

## Test Coverage Goals

- **RNG Engine**: 100% (deterministic behavior critical)
- **Laws Interpreter**: 90%+ (all Laws mapped correctly)
- **Oracle Integration**: 80%+ (main flows covered)
- **API Endpoints**: 70%+ (key endpoints tested)

---

## Writing New Tests

### Test Naming

- `test_<functionality>`: Test specific functionality
- `test_<component>_<behavior>`: Test component behavior

### Test Structure

```python
def test_example():
    """Test description."""
    # Arrange
    component = Component()
    
    # Act
    result = component.method()
    
    # Assert
    assert result == expected
```

---

## Continuous Integration

Tests should run on:
- Pull requests
- Commits to main branch
- Before deployment

---

**PANGEA IS THE TABLE.**
**YOU DON'T BETRAY THE TABLE.**

**Tests verify truth. Tests ensure transparency. Tests honor the Laws.**
