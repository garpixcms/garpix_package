# Garpix Pack

Create and upload packages to pypi.org.

## Quickstart

Install with pip:

```bash
pip install garpix_qa
```

Add the `garpix_pack` to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'garpix_pack',
]
```

Create new package in your project.

```bash
python manage.py startpackage <app_name>
```

Upload package to pypi.org.

```bash
python manage.py pack <app_name>
```

### Example

```
python manage.py startpackage my_app
python manage.py pack my_app
```

# Changelog

See [CHANGELOG.md](CHANGELOG.md).

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)