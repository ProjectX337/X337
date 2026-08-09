from core.build.build_plan import BuildPlan


def test_dependency_runs_before_priority():
    plan = BuildPlan()

    plan.add(
        name="AI",
        generator="ai",
        description="AI",
        output_directory="backend/ai",
        priority=1,
        depends_on=["Backend"],
    )

    plan.add(
        name="Backend",
        generator="backend",
        description="Backend",
        output_directory="backend",
        priority=100,
    )

    ordered = plan.ordered_steps()

    assert [step.name for step in ordered] == [
        "Backend",
        "AI",
    ]


def test_independent_steps_use_priority():
    plan = BuildPlan()

    plan.add(
        name="Slow",
        generator="slow",
        description="Slow",
        output_directory="slow",
        priority=20,
    )

    plan.add(
        name="Fast",
        generator="fast",
        description="Fast",
        output_directory="fast",
        priority=10,
    )

    ordered = plan.ordered_steps()

    assert [step.name for step in ordered] == [
        "Fast",
        "Slow",
    ]


def test_missing_dependency_fails():
    plan = BuildPlan()

    plan.add(
        name="AI",
        generator="ai",
        description="AI",
        output_directory="ai",
        depends_on=["Backend"],
    )

    try:
        plan.ordered_steps()
    except ValueError as exc:
        assert "missing dependencies" in str(exc)
    else:
        raise AssertionError(
            "Expected missing dependency failure"
        )


def test_dependency_cycle_fails():
    plan = BuildPlan()

    plan.add(
        name="A",
        generator="a",
        description="A",
        output_directory="a",
        depends_on=["B"],
    )

    plan.add(
        name="B",
        generator="b",
        description="B",
        output_directory="b",
        depends_on=["A"],
    )

    try:
        plan.ordered_steps()
    except ValueError as exc:
        assert "dependency cycle" in str(exc)
    else:
        raise AssertionError(
            "Expected dependency cycle failure"
        )
