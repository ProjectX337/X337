export async function generateProject(prompt: string) {
    const response = await fetch(
        "http://localhost:9000/api/generate",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                prompt,
            }),
        }
    );

    if (!response.ok) {
        const errorText = await response.text();

        throw new Error(
            `Generation failed (${response.status}): ${errorText}`
        );
    }

    return response.json();
}
