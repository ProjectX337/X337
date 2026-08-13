from core.training.training_intelligence import TrainingIntelligence


REFERENCE = """
import React from "react";

export default function Dashboard() {
    return (
        <div className="dashboard">

            <aside className="sidebar">
                Navigation
            </aside>

            <section className="metrics">

                <article className="card">
                    <span>Revenue</span>
                    <strong>$84,240</strong>
                    <small>+18%</small>
                </article>

            </section>

            <button className="primary">
                Create Project
            </button>

        </div>
    );
}
"""


def test_component_patterns_are_learned():
    profile = TrainingIntelligence().analyze(
        name="Dashboard Reference",
        description="Dark SaaS dashboard",
        code=REFERENCE,
    ).to_dict()

    patterns = profile["component_patterns"]

    assert isinstance(patterns, list)

    print(patterns)
