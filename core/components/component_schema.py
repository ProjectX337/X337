from dataclasses import dataclass, field
from typing import List, Dict, Any



@dataclass
class ComponentDefinition:
    """
    Blueprint definition for generated React components.
    Designed to support future X337 expansion.
    """


    name: str


    category: str = ""


    description: str = ""



    #
    # React interface
    #
    props: List[str] = field(
        default_factory=list
    )



    #
    # npm/package dependencies
    #
    dependencies: List[str] = field(
        default_factory=list
    )



    #
    # React state variables
    #
    state: List[str] = field(
        default_factory=list
    )



    #
    # React hooks
    #
    hooks: List[str] = field(
        default_factory=list
    )



    #
    # User interactions
    #
    events: List[str] = field(
        default_factory=list
    )



    #
    # Component variations
    #
    variants: List[str] = field(
        default_factory=list
    )



    #
    # Styling system
    #
    styling: Dict[str, Any] = field(
        default_factory=dict
    )



    #
    # Backend/API services
    #
    services: List[str] = field(
        default_factory=list
    )



    #
    # Database requirements
    #
    database: List[str] = field(
        default_factory=list
    )



    #
    # AI capabilities
    #
    ai_capabilities: List[str] = field(
        default_factory=list
    )



    #
    # Accessibility requirements
    #
    accessibility: List[str] = field(
        default_factory=list
    )



    #
    # Responsive behavior
    #
    responsive: Dict[str, Any] = field(
        default_factory=dict
    )



    #
    # Any future fields from JSON
    #
    metadata: Dict[str, Any] = field(
        default_factory=dict
    )