import {
    useEffect,
    useState
} from "react";


import {
    getFiles,
    getFile
} from "../api/code";



export default function CodeExplorer(){


    const [files,setFiles] = useState<string[]>([]);

    const [selected,setSelected] = useState("");

    const [code,setCode] = useState("");

    const [loading,setLoading] = useState(false);

    const [error,setError] = useState("");



    useEffect(()=>{


        getFiles()

        .then(data=>{


            console.log(
                "FILES FROM X337:",
                data
            );


            setFiles(data);


        })


        .catch(err=>{


            console.error(err);

            setError(
                "Could not load files"
            );


        });



    },[]);




    async function openFile(path:string){


        console.log(
            "OPENING FILE:",
            path
        );


        setSelected(path);

        setLoading(true);

        setError("");



        try{


            const result = await getFile(path);



            console.log(
                "FILE RESPONSE:",
                result
            );



            setCode(
                result.code || "No code returned"
            );



        }

        catch(err){


            console.error(err);


            setError(
                "Could not load file"
            );


        }


        finally{


            setLoading(false);


        }


    }




return (

<div

style={{

display:"flex",

height:"75vh",

border:"1px solid #ddd",

borderRadius:"12px",

overflow:"hidden",

background:"#fff"

}}

>



{/* FILE TREE */}

<div

style={{

width:"320px",

borderRight:"1px solid #ddd",

padding:"20px",

overflowY:"auto"

}}

>


<h2>

Generated Files

</h2>



{
error &&

<p style={{color:"red"}}>

{error}

</p>

}



{
files.map(file=>(


<button

key={file}

onClick={()=>openFile(file)}

style={{

display:"block",

width:"100%",

padding:"10px",

marginBottom:"8px",

textAlign:"left",

borderRadius:"6px",

border:"1px solid #ddd",

background:

selected===file

?

"#dbeafe"

:

"#f8fafc",

cursor:"pointer"

}}

>


{file}


</button>



))

}



</div>





{/* CODE VIEWER */}


<div

style={{

flex:1,

padding:"20px",

overflow:"auto"

}}

>


<h2>

{

selected ||

"Select a file"

}

</h2>




{

loading &&

<p>

Loading code...

</p>

}




<pre

style={{

background:"#111827",

color:"#f8fafc",

padding:"20px",

borderRadius:"10px",

minHeight:"500px",

overflow:"auto",

fontSize:"14px",

lineHeight:"1.6"

}}

>


{

code ||

"Select a file from the left panel"

}


</pre>



</div>



</div>


)

}
