import argparse
import sys

from git import Repo

DEFAULT_LIMIT = 5


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--exit-zero-even-if-changed', action='store_true')
    parser.add_argument('--limit', dest='limit', default=False)
    args = parser.parse_args(argv)

    repo = Repo('.')
    limit = args.limit if args.limit else DEFAULT_LIMIT
    if len(repo.index.diff("HEAD")) <= int(limit):
        print('To unstage file use: "git reset HEAD <file>..."')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
