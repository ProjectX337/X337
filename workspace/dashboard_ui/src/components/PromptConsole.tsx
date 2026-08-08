import { useState } from "react";
import { useProject } from "../context/ProjectContext";
import { generateProject } from "../api/generator";

export default function PromptConsole() {
    const [prompt, setPrompt] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const { setProject } = useProject();

    async function generate() {
        const trimmedPrompt = prompt.trim();

        if (!trimmedPrompt || loading) {
            return;
        }

        setLoading(true);
        setError("");

        try {
            const data = await generateProject(trimmedPrompt);

            console.log(
                "X337 Generated:",
                data
            );

            setProject(data);
        } catch (error) {
            console.error(
                "Generation failed",
                error
            );

            setError(
                error instanceof Error
                    ? error.message
                    : "Generation failed"
            );
        } finally {
            setLoading(false);
        }
    }

    function handleKeyDown(
        event: React.KeyboardEvent<HTMLTextAreaElement>
    ) {
        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {
            event.preventDefault();
            generate();
        }
    }

    return (
        <div
            style={{
                width: "100%",
                display: "flex",
                flexDirection: "column",
                gap: "12px",
            }}
        >
            <textarea
                value={prompt}
                onChange={(event) =>
                    setPrompt(event.target.value)
                }
                onKeyDown={handleKeyDown}
                placeholder="Describe the application you want X337 to build..."
                disabled={loading}
                rows={5}
                style={{
                    width: "100%",
                    boxSizing: "border-box",
                    padding: "14px",
                    borderRadius: "10px",
                    border: "1px solid #d9dce3",
                    resize: "vertical",
                    fontFamily: "inherit",
                    fontSize: "15px",
                    lineHeight: "1.5",
                    outline: "none",
                }}
            />

            <button
                type="button"
                onClick={generate}
                disabled={
                    loading ||
                    !prompt.trim()
                }
                style={{
                    alignSelf: "flex-start",
                    padding: "12px 20px",
                    borderRadius: "10px",
                    border: "none",
                    background: loading
                        ? "#9ca3af"
                        : "#111827",
                    color: "white",
                    fontSize: "14px",
                    fontWeight: 600,
                    cursor:
                        loading ||
                        !prompt.trim()
                            ? "not-allowed"
                            : "pointer",
                }}
            >
                {loading
                    ? "Generating..."
                    : "Generate Project"}
            </button>

            {error && (
                <div
                    style={{
                        padding: "12px",
                        borderRadius: "8px",
                        background: "#fef2f2",
                        border: "1px solid #fecaca",
                        color: "#b91c1c",
                        fontSize: "14px",
                    }}
                >
                    {error}
                </div>
            )}
        </div>
    );
}
