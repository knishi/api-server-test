# APIサーバー・標準テンプレート (Gold Master)

本プロジェクトは、OpenStackの設計思想（Pecan, oslo.*等）を取り入れた、高品質で保守性の高いAPIサーバーを開発するための**標準テンプレート（ゴールドマスター）**です。

## 概要

新しいAPIプロジェクト（例：カロリー管理、場所管理等）を開始するための「足場」を提供します。単なるコードの集まりではなく、開発プロセス、セキュリティ、運用監視のルールが統合されています。

## 主な機能・特徴

- **認証 (Authentication)**: Keystone互換のミドルウェア層。
- **データベース (Database)**: `oslo.db` + SQLAlchemyによる抽象化されたDBアクセス。
- **ログ (Logging)**: `oslo.log` による相関ID付きの運用ログ基盤。
- **例外処理 (Error Handling)**: 統一されたJSONレスポンスを返すグローバルエラーハンドラー。
- **CI/CD**: GitHub Actionsによる自動テストおよびデプロイ (GHCR)。
- **コンテナ**: DockerおよびDocker Composeによるポータブルな実行環境。
- **開発プロセス**: TDD（テスト駆動開発）および「AIインスペクター」による品質監視。

## クイックスタート

### 1. 新しいプロジェクトの開始
1. GitHubの「Use this template」ボタンから新しいリポジトリを作成します。
2. ローカルにクローンします。
3. マスター（本リポジトリ）を `upstream` として登録します：
   ```bash
   git remote add upstream https://github.com/knishi/api-server-test.git
   ```

### 2. 起動
```bash
docker compose up --build
```

## ドキュメント一覧

詳細な仕様については `docs/` ディレクトリを参照してください。

- [アーキテクチャ詳細](docs/ARCHITECTURE.md)
- [運用・デプロイガイド](docs/OPERATIONS.md)
- [AIエージェント開発ガイド](docs/AI_DEVELOPMENT.md)
- [開発プロセス憲法 (SKILL.md)](.agent/skills/api_development/SKILL.md)

## 開発ルール（マネージャー・AIエージェント用）

本プロジェクトには、AIエージェントと人間が安全に協働するための「憲法」が定義されています。詳細は [SKILL.md](.agent/skills/api_development/SKILL.md) を確認してください。
