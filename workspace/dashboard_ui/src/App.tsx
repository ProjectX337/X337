import { useState } from "react";
import PromptConsole from "./components/PromptConsole";
import PreviewPanel from "./components/PreviewPanel";

export default function App() {

    const [previewUrl, setPreviewUrl] = useState(
        "http://localhost:9100"
    );

    return (
        <div
            style={{
                minHeight: "100vh",
                padding: "30px",
                background: "#f5f7fb",
                fontFamily: "Inter, sans-serif"
            }}
        >

            <h1>
                X337
            </h1>

            <p>
                AI Project Generation Dashboard
            </p>

            <div
                style={{
                    marginTop: "30px",
                    marginBottom: "30px"
                }}
            >
                <PromptConsole />
            </div>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "1fr 2fr",
                    gap: "20px"
                }}
            >

                <div
                    style={{
                        background: "white",
                        padding: "20px",
                        borderRadius: "12px",
                        border: "1px solid #ddd"
                    }}
                >

                    <h2>
                        Generated Project
                    </h2>

                    <p>
                        ADHD Learning Assistant
                    </p>

                    <p>
                        Preview runtime:
                    </p>

                    <code>
                        {previewUrl}
                    </code>

                </div>

                <PreviewPanel
                    url={previewUrl}
                />

            </div>

        </div>
    );
}
