class FuriganaInfoError(Exception):
    """furigana_info ライブラリで発生する一般的なエラー."""
    pass

class FuriganaInfoParseError(FuriganaInfoError):
    """HTML 解析が失敗した場合などに使う."""
    pass