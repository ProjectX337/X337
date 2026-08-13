export interface PreviewInfo {
    status: string;
    url: string;
    port: number;
}

export interface TrainingExample {
    name: string;
    description: string;
    code: string;
    created_at?: string;
}

export interface PreviewResponse {
    status: string;
    url: string;
    port: number;
}

export interface GenerateResponse {
    project: string;
    status: string;
    directory: string;
    files: string[];
    pages: string[];
    components: string[];
    training_examples: number;
    preview: PreviewResponse;
    message: string;
}

export async function generateProject(
    prompt: string,
): Promise<GenerateResponse> {
    const response = await fetch(
        "http://127.0.0.1:9000/api/generate",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                prompt,
            }),
        },
    );

    if (!response.ok) {
        const errorText = await response.text();

        throw new Error(
            `Generation failed (${response.status}): ${errorText}`,
        );
    }

    return response.json();
}

export async function getTrainingExamples(): Promise<
    TrainingExample[]
> {
    const response = await fetch(
        "http://127.0.0.1:9000/api/training",
    );

    if (!response.ok) {
        const errorText = await response.text();

        throw new Error(
            `Training load failed (${response.status}): ${errorText}`,
        );
    }

    const data = await response.json();

    return data.examples ?? [];
}

export async function addTrainingExample(input: {
    name: string;
    description: string;
    code: string;
}): Promise<TrainingExample[]> {
    const response = await fetch(
        "http://127.0.0.1:9000/api/training",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(input),
        },
    );

    if (!response.ok) {
        const errorText = await response.text();

        throw new Error(
            `Training failed (${response.status}): ${errorText}`,
        );
    }

    const data = await response.json();

    return data.examples ?? [];
}
