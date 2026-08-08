interface PreviewPanelProps {
    url?: string;
    project?: any;
}

export default function PreviewPanel({
    url,
    project
}: PreviewPanelProps) {

    const preview =
        url ??
        project?.previewUrl ??
        "http://localhost:9100";


    return (
        <div
            style={{
                width:"100%",
                height:"600px",
                border:"1px solid #ddd",
                borderRadius:"12px",
                overflow:"hidden",
                background:"white"
            }}
        >

            <iframe
                src={preview}
                title="X337 Generated Application"
                style={{
                    width:"100%",
                    height:"100%",
                    border:"none"
                }}
            />

        </div>
    );
}
