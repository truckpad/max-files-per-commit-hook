# max-files-per-commit-hook

Hook to limit max files on a single commit

> Make sure [pre-commit](https://pre-commit.com) is installed

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://github.com/truckpad/max-files-per-commit-hook
    rev: master
    hooks:
    -   id: max-files-per-commit
        args: ['--limit=5'] # Optional
```
