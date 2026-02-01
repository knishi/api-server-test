# アーキテクチャ詳細

本プロジェクトの内部構造と設計方針について説明します。

## 1. ディレクトリ構造

```text
├── apibase/               # 基盤パッケージ
│   ├── api/               # APIレイヤー
│   │   ├── controllers/   # 各バージョンのコントローラー（ビジネスロジック入口）
│   │   └── root.py        # ルートコントローラー（ディスパッチ制御）
│   ├── common/            # 共通モジュール
│   │   ├── exception.py   # カスタム例外クラス
│   │   └── hooks.py       # Pecan Hook（エラーハンドリング等）
│   ├── db/                # データベースレイヤー
│   │   ├── api.py         # DB CRUDロジック
│   │   └── models.py      # SQLAlchemyモデル定義
│   └── middleware.py      # WSGIミドルウェア（認証等）
├── app.py                 # アプリケーションのエントリポイント
└── config.py              # アプリケーション設定
```

## 2. 認証フロー

1. クライアントが `X-Auth-Token` を付けてリクエスト。
2. `FakeAuthMiddleware` がトークンを検証（現在は模倣実装）。
3. 検証成功時、`X-User-Id` などのヘッダーを付与して後続へ渡す。
4. アプリ側は、既に認証されたものとしてヘッダーから情報を取得。

## 3. エラーハンドリング (Global Error Hook)

- 開発者は、コントローラー内で `raise exception.ItemNotFound()` のように例外を投げるだけでOK。
- `ErrorHook` が自動的に捕捉し、以下のフォーマットでクライアントに返却します。
  ```json
  {"error": {"code": 404, "message": "Item not found"}}
  ```

## 4. データベース管理

- `oslo.db` を利用し、トランザクション管理やコネクションプールを最適化しています。
- 設定ファイル (`config.py`) を編集するだけで、SQLite, MySQL, PostgreSQL等へ切り替え可能です。
