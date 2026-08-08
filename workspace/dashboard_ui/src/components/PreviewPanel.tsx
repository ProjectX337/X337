interface PreviewProject {
    previewUrl?: string;
    preview_url?: string;
    url?: string;
}

interface PreviewPanelProps {
    url?: string;
    project?: PreviewProject;
}

export default function PreviewPanel({
    url,
    project,
}: PreviewPanelProps) {
    const previewUrl =
        url ??
        project?.previewUrl ??
        project?.preview_url ??
        project?.url;

    if (!previewUrl) {
        return (
            <div
                style={{
                    height: "600px",
                    border: "1px solid #ddd",
                    borderRadius: "12px",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    color: "#777",
                    background: "#fafafa",
                }}
            >
                <div>
                    <h3>Live Preview</h3>
                    <p>
                        Generate a project to see the application here.
                    </p>
                </div>
            </div>
        );
    }

    return (
        <div
            style={{
                width: "100%",
                height: "600px",
                border: "1px solid #ddd",
                borderRadius: "12px",
                overflow: "hidden",
                background: "white",
            }}
        >
            <iframe
                src={previewUrl}
                title="X337 Generated Application"
                style={{
                    width: "100%",
                    height: "100%",
                    border: "none",
                }}
            />
        </div>
    );
}
