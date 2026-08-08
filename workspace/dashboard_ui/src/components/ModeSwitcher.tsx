import type { DashboardMode } from "../state/dashboardMode";

interface Props {
    mode: DashboardMode;
    setMode: (mode: DashboardMode) => void;
}

export default function ModeSwitcher({ mode, setMode }: Props) {
    return (
        <div
            style={{
                display: "flex",
                gap: "8px",
            }}
        >
            <button
                type="button"
                onClick={() => setMode("overview")}
                aria-pressed={mode === "overview"}
            >
                Overview
            </button>

            <button
                type="button"
                onClick={() => setMode("code")}
                aria-pressed={mode === "code"}
            >
                Code
            </button>

            <button
                type="button"
                onClick={() => setMode("preview")}
                aria-pressed={mode === "preview"}
            >
                Preview
            </button>

            <button
                type="button"
                onClick={() => setMode("agents")}
                aria-pressed={mode === "agents"}
            >
                Agents
            </button>
        </div>
    );
}
