import { useEffect, useState } from "react";


export default function CodeExplorer(){

    const [files,setFiles] = useState<string[]>([]);
    const [selected,setSelected] = useState("");
    const [code,setCode] = useState("");


    useEffect(()=>{

        fetch(
            "http://localhost:9001/api/files"
        )
        .then(res=>res.json())
        .then(data=>{

            setFiles(data);

        });


    },[]);



    async function openFile(
        file:string
    ){

        setSelected(file);


        const response = await fetch(
            `http://localhost:9001/api/file?path=${file}`
        );


        const data = await response.json();


        setCode(
            data.code
        );

    }



    return (

        <div
        style={{
            display:"flex",
            height:"600px"
        }}
        >


            <div
            style={{
                width:"300px",
                borderRight:"1px solid #ccc",
                padding:"20px"
            }}
            >

            <h3>
                Generated Files
            </h3>


            {
                files.map(file=>(

                    <div
                    key={file}
                    onClick={()=>openFile(file)}
                    style={{
                        cursor:"pointer",
                        marginBottom:"8px"
                    }}
                    >

                    {file}

                    </div>

                ))
            }


            </div>



            <div
            style={{
                flex:1,
                padding:"20px",
                overflow:"auto"
            }}
            >

            <h3>
                {selected}
            </h3>


            <pre>
                {code}
            </pre>


            </div>


        </div>

    )

}
