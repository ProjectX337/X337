export interface DashboardData {

    project: string;
    status: string;
    files: number;
    components: string[];
    pages: string[];
    services: string[];

}


export async function getDashboard(): Promise<DashboardData> {

    const response = await fetch(
        "http://localhost:9000/api/dashboard"
    );


    return response.json();

}
