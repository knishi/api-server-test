# アーキテクチャ詳細

![Architecture Overview](../docs/images/architecture_hero.png)

本プロジェクトの内部構造と、各コンポーネントがどのように協調して動作するかを説明します。

## 1. システム協調フロー (Coordination Flow)

本システムは Docker Compose によってオーケストレーションされ、Nginx がリバースプロキシとして、Gunicorn が WSGI サーバーとして機能します。

```mermaid
graph TD
    User((ユーザー/クライアント)) -->|HTTP 8080| Nginx[Nginx Container]
    
    subgraph "Docker Compose Network"
        Nginx -->|Proxy Pass| Gunicorn[Gunicorn / WSGI]
        Gunicorn -->|Load App| App[apibase.app]
        App -->|SQLAlchemy| DB[(Database / SQLite)]
    end
    
    subgraph "Logic Layer"
        App -->|Dispatch| Controllers[Controllers]
        Controllers -->|Access| DBApi[DB API]
        DBApi -->|Query| Models[Models]
    end

    style App fill:#f9f,stroke:#333,stroke-width:2px
    style Nginx fill:#bbf,stroke:#333,stroke-width:2px
    style Gunicorn fill:#dfd,stroke:#333,stroke-width:2px
```

## 2. ディレクトリ構造

```text
├── etc/                   # 設定ファイル類
│   ├── apibase/
│   │   └── config.py      # アプリケーション設定 (Pecan config)
│   └── nginx/
├── build/                 # ビルド・デプロイ関連ファイル
├── bin/                   # 運用補助スクリプト (manage.sh 等)
├── public/                # 静的ファイル (API docs, etc.)
├── apibase/               # アプリケーション・パッケージ
│   ├── app.py             # WSGIエントリポイント
│   ├── api/               # Webレイヤー
│   ├── db/                # DBレイヤー
│   └── ...
├── pyproject.toml         # プロジェクトメタデータ・設定集約
└── docker-compose.yml     # コンテナオーケストレーション
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
