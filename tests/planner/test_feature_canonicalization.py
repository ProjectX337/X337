from collections import Counter

from core.planner.project_planner import ProjectPlanner


def test_feature_slugs_are_unique_in_project_spec():
    spec = ProjectPlanner().plan(
        """
        Build a beautiful AI productivity application with
        dashboard, AI chat, analytics, authentication,
        search, settings, responsive navigation,
        interactive cards, and polished modern UI
        """
    )

    slugs = [
        feature.slug
        for feature in spec.feature_models
    ]

    duplicates = {
        slug: count
        for slug, count in Counter(slugs).items()
        if count > 1
    }

    assert not duplicates, (
        f"Duplicate canonical FeatureSpec slugs: {duplicates}"
    )
