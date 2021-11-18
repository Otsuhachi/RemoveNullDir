import argparse as Ap

from pathlib import Path


def rmdir(path: Path) -> None:
    p_str = str(path.resolve())
    if path.is_dir():
        try:
            path.rmdir()
            print(f'{p_str}を削除しました。')
        except Exception as e:
            print(f'{p_str}を削除できませんでした。')
            raise e
    elif path.is_file():
        print(f'{p_str}はファイルです。')


def recursively_rmdir_entry(path: Path, max_depth: int) -> None:
    if max_depth < 1:
        msg = 'max_depthは1以上である必要があります。'
        raise ValueError(msg)
    if not path.is_dir():
        return None
    for dir in filter(Path.is_dir, path.iterdir()):
        recursively_rmdir(dir, max_depth, 1)


def recursively_rmdir(path: Path, max_depth: int, current_depth: int) -> bool:
    if not path.exists():
        return True
    if path.is_file():
        msg = f'{path.resolve()}はファイルです。'
        raise FileExistsError(msg)
    paths = tuple(path.iterdir())
    if not paths:
        rmdir(path)
        return True
    current_depth += 1
    if max_depth < current_depth:
        return False
    is_removable = True
    for dir in filter(Path.is_dir, paths):
        if not recursively_rmdir(dir, max_depth, current_depth):
            is_removable = False
    if not is_removable:
        return False
    if tuple(filter(Path.is_file, paths)):
        return False
    try:
        rmdir(path)
        return True
    except:
        return False


def main():
    parser = Ap.ArgumentParser(description='空フォルダを再帰的に除去します。')
    parser.add_argument('-m', '--max_depth', type=int, default=1, help='再帰する最大階層数です。初期値は1です。また、起点の階層は0です。')
    parser.add_argument('-p', '--path', type=Path, default=Path(), help='起点となるパスです。')
    args = parser.parse_args()
    path = args.path
    max_depth = args.max_depth
    recursively_rmdir_entry(path, max_depth)
