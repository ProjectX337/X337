from core.graph.graph_builder import GraphBuilder
from core.graph.models import (
    EdgeRelation,
    NodeKind,
)
from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.models.feature_spec import FeatureSpec


def build_fixture():
    ui = UISpec(
        page_models=[
            UIPage(
                name="Dashboard",
                route="/dashboard",
                components=[
                    UIComponent(
                        name="Header",
                        component_type="header",
                        states=["loading", "ready"],
                    ),
                    UIComponent(
                        name="Card",
                        component_type="card",
                    ),
                ],
            ),
            UIPage(
                name="Settings",
                route="/settings",
                components=[
                    UIComponent(
                        name="Header",
                        component_type="header",
                    ),
                    UIComponent(
                        name="Card",
                        component_type="card",
                    ),
                ],
            ),
        ]
    )

    feature = FeatureSpec(
        name="Analytics",
        slug="analytics",
        description="Analytics dashboard",
        routes=["/dashboard"],
        pages=["Dashboard"],
        components=["Header", "Card"],
        state=["metrics", "loading"],
        api_contracts=["GET /metrics"],
    )

    return ui, feature


def test_application_graph_preserves_architecture_layers():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    kinds = {
        node.kind
        for node in graph.nodes.values()
    }

    assert NodeKind.FEATURE in kinds
    assert NodeKind.PAGE in kinds
    assert NodeKind.COMPONENT in kinds
    assert NodeKind.STATE in kinds
    assert NodeKind.API in kinds
    assert NodeKind.ROUTE in kinds


def test_application_graph_uses_page_safe_component_identity():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    component_ids = {
        node.id
        for node in graph.nodes.values()
        if node.kind == NodeKind.COMPONENT
    }

    assert component_ids == {
        "page.dashboard.component.header",
        "page.dashboard.component.card",
        "page.settings.component.header",
        "page.settings.component.card",
    }


def test_pages_render_their_own_component_instances():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    dashboard_components = {
        edge.target
        for edge in graph.edges
        if (
            edge.source == "page.dashboard"
            and edge.relation == EdgeRelation.RENDERS
        )
    }

    settings_components = {
        edge.target
        for edge in graph.edges
        if (
            edge.source == "page.settings"
            and edge.relation == EdgeRelation.RENDERS
        )
    }

    assert dashboard_components == {
        "page.dashboard.component.header",
        "page.dashboard.component.card",
    }

    assert settings_components == {
        "page.settings.component.header",
        "page.settings.component.card",
    }


def test_feature_page_relationship_is_preserved():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    assert any(
        edge.source == "feature.analytics"
        and edge.target == "page.dashboard"
        and edge.relation == EdgeRelation.IMPLEMENTS
        for edge in graph.edges
    )


def test_page_route_is_materialized():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    route_nodes = [
        node
        for node in graph.nodes.values()
        if node.kind == NodeKind.ROUTE
    ]

    assert len(route_nodes) == 2

    route_names = {
        node.name
        for node in route_nodes
    }

    assert "/dashboard" in route_names
    assert "/settings" in route_names


def test_feature_state_is_materialized():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    state_nodes = [
        node
        for node in graph.nodes.values()
        if node.kind == NodeKind.STATE
    ]

    state_names = {
        node.name
        for node in state_nodes
    }

    assert "metrics" in state_names
    assert "loading" in state_names


def test_feature_api_contracts_are_materialized():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    api_nodes = [
        node
        for node in graph.nodes.values()
        if node.kind == NodeKind.API
    ]

    api_names = {
        node.name
        for node in api_nodes
    }

    assert "GET /metrics" in api_names


def test_component_state_is_materialized():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    state_nodes = [
        node
        for node in graph.nodes.values()
        if node.kind == NodeKind.STATE
    ]

    state_names = {
        node.name
        for node in state_nodes
    }

    assert "loading" in state_names
    assert "ready" in state_names


def test_graph_contains_relationships_for_materialized_semantics():
    ui, feature = build_fixture()

    graph = GraphBuilder().build(
        ui,
        [feature],
    )

    relations = {
        edge.relation
        for edge in graph.edges
    }

    assert EdgeRelation.IMPLEMENTS in relations
    assert EdgeRelation.RENDERS in relations
    assert EdgeRelation.CONTAINS in relations
    assert EdgeRelation.NAVIGATES_TO in relations
    assert EdgeRelation.PROVIDES in relations
