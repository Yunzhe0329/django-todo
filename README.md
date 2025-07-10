#  Django TODO Project

本專案是一個基於 Django 架構開發的待辦事項（TODO）應用，支援 RESTful API，具備基本任務管理功能與深淺色模式切換介面。專案設計遵循 MVC 模式，具有清楚分離的模型、邏輯與介面層結構。

---

##  專案練習目的

- 待辦事項增／刪／改／查（CRUD）
- RESTful API 設計
- 深色與淺色 UI 模式切換
- 良好遵循 Django MVC 架構
- 模組化：models, views, templates, static, urls

---

##  開發環境與工具版本

| 工具 | 版本 |
|------|------|
| macOS | 14.x |
| Python | 3.11.x |
| pip | 23.x |
| Django | 5.0.x |
| djangorestframework | 3.15.x |
| SQLite | 3.x |
| Git | 2.39+ |
| VS Code | 1.8x+（開發使用） |
| pipenv / venv | 任一虛擬環境工具皆可 |

---

##  架構設計（MVC）

- **Model**：`todo/models.py` 定義任務資料模型
- **View**：`todo/views.py` 處理邏輯與回應，含 CBV 與 APIView
- **Controller（URL Dispatcher）**：`todo/urls.py` 映射 URL 與對應邏輯
- **Templates**：`todo/templates/` 包含所有 HTML 模板
- **Static**：CSS、JS 等靜態資源，支援 UI 切換與互動

---

##  專案結構
todo_project/
├── todo/ # 核心應用（models, views, urls）
├── todo_project/ # Django 設定與主路由
├── manage.py # 執行指令入口
├── .env # 開發環境變數（未追蹤）
├── .github/ # CI/CD 設定（如有）
└── db.sqlite3 # 預設資料庫（開發用）

## 資料庫初始化和啟動伺服器的方式
python manage.py migrate
python manage.py runserver
