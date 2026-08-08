export async function generateProject(prompt:string){

    const response = await fetch(
        "http://localhost:9002/api/generate",
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                prompt
            })
        }
    );


    return response.json();

}
