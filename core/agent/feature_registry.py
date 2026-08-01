from __future__ import annotations


class FeatureRegistry:
    """
    Knowledge base of product capabilities.
    Maps user language to project features.
    """

    FEATURES = {

        "analytics": {
            "keywords": [
                "analytics",
                "reporting",
                "reports",
                "metrics",
                "growth",
                "insights",
                "charts",
                "dashboard",
                "statistics",
            ],
            "routes": [
                "/analytics"
            ],
            "pages": [
                "AnalyticsPage"
            ],
            "components": [
                "AnalyticsPage",
                "ReportCard",
                "MetricsChart",
            ],
            "state": [
                "analytics_metrics"
            ],
            "api_contracts": [
                "GET /reports"
            ],
            "dependencies": [
                "authentication",
                "dashboard",
            ],
        },


        "dashboard": {
            "keywords": [
                "dashboard",
                "overview",
                "admin",
                "monitor",
                "control panel",
            ],
            "routes": [
                "/dashboard"
            ],
            "pages": [
                "DashboardPage"
            ],
            "components": [
                "DashboardPage",
                "AnalyticsCard",
            ],
            "state": [
                "dashboard_metrics"
            ],
            "api_contracts": [
                "GET /analytics"
            ],
            "dependencies": [
                "authentication",
            ],
        },


        "billing": {
            "keywords": [
                "billing",
                "payment",
                "invoice",
                "subscription",
                "checkout",
                "stripe",
            ],
            "routes": [
                "/billing"
            ],
            "pages": [
                "BillingPage"
            ],
            "components": [
                "BillingPage",
                "InvoiceTable",
            ],
            "state": [
                "billing_status"
            ],
            "api_contracts": [
                "GET /billing",
            ],
            "dependencies": [
                "authentication",
            ],
        },


        "authentication": {
            "keywords": [
                "auth",
                "login",
                "signup",
                "signin",
                "password",
                "oauth",
                "google login",
            ],
            "routes": [
                "/login"
            ],
            "pages": [
                "LoginPage"
            ],
            "components": [
                "LoginForm",
                "AuthGuard",
            ],
            "state": [
                "current_user"
            ],
            "api_contracts": [
                "POST /auth/login",
            ],
            "dependencies": [],
        },
    }


    def match(
        self,
        message: str,
    ) -> list[str]:

        text = message.lower()

        scores = {}


        for feature, data in self.FEATURES.items():

            score = 0

            for keyword in data["keywords"]:

                if keyword in text:

                    score += len(keyword.split())

                    if keyword == feature:

                        score += 5


            if score:

                scores[feature] = score


        ranked = sorted(
            scores,
            key=scores.get,
            reverse=True,
        )


        return ranked



    def get(
        self,
        feature: str,
    ) -> dict:

        return self.FEATURES.get(
            feature,
            {}
        )
