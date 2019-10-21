# max-files-per-commit-hook

Some out-of-the-box hooks for [pre-commit](https://pre-commit.com).

Add this to your .pre-commit-config.yaml

```yaml
repos:
-   repo: https://gitlab.com/TruckPad/opensource/max-files-per-commit-hook.git
    rev: master
    hooks:
    -   id: max-files-per-commit
        args: ['--limit=5'] # Optional
```
