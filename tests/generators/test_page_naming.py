from core.generators.react.page_naming import page_filename


def test_page_filename_canonicalization():
    cases = {
        "AI": "ai",
        "Dashboard": "dashboard",
        "User Settings": "user-settings",
        "AISettings": "ai-settings",
        "AccountOverview": "account-overview",
        "Recent Transactions": "recent-transactions",
        "API": "api",
        "API Settings": "api-settings",
    }

    for value, expected in cases.items():
        assert page_filename(value) == expected
