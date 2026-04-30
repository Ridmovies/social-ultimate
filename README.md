```
app/
│
├── main.py
├── core/
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│   └── logging.py
│
├── api/
│   ├── router.py
│   └── v1/
│       ├── endpoints/
│       │   ├── auth.py
│       │   ├── users.py
│       │   ├── posts.py
│       │   ├── comments.py
│       │   └── notifications.py
│       └── deps.py
│
├── models/
│   ├── base.py
│   ├── user.py
│   ├── post.py
│   ├── comment.py
│   └── notification.py
│
├── schemas/
│   ├── user.py
│   ├── post.py
│   ├── comment.py
│   └── notification.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── post_service.py
│   ├── comment_service.py
│   └── notification_service.py
│
├── repositories/
│   ├── base.py
│   ├── user_repo.py
│   ├── post_repo.py
│   ├── comment_repo.py
│   └── notification_repo.py
│
├── db/
│   ├── session.py
│   ├── base.py
│   └── migrations/
│
├── utils/
│   ├── datetime.py
│   └── pagination.py
│
└── tests/
    ├── conftest.py
    ├── test_users.py
    └── test_posts.py
```