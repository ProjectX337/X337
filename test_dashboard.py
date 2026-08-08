from core.dashboard.dashboard_state import DashboardState



dashboard = DashboardState(

    project_name="generated_app",

    project_path=
    "workspace/generated/generated_app"

)



dashboard.scan_project()



print("DASHBOARD")

print(
    dashboard.summary()
)