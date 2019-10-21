# max-files-per-commit-hook

Hook to limit max files on a single commit

> Make sure [pre-commit](https://pre-commit.com) is installed

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://gitlab.com/TruckPad/opensource/max-files-per-commit-hook.git
    rev: master
    hooks:
    -   id: max-files-per-commit
        args: ['--limit=5'] # Optional
```
