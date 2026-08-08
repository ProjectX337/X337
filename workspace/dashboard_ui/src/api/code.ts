
export async function getFiles(){

    const response = await fetch(
        "http://localhost:9001/api/files"
    );

    return response.json();

}



export async function getFile(path:string){

    const response = await fetch(
        `http://localhost:9001/api/file?path=${encodeURIComponent(path)}`
    );


    return response.json();

}

