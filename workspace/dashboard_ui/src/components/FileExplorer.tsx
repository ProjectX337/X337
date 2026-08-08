import {useEffect,useState} from "react";


interface Props{

onSelect:(file:string)=>void;

}



export default function FileExplorer(
{
onSelect
}:Props
){


const [files,setFiles]=useState<string[]>([]);
const [error,setError]=useState("");



useEffect(()=>{


async function loadFiles(){


try{


const response =
await fetch(
"http://localhost:9001/api/files"
);


const data =
await response.json();


setFiles(data);


}

catch(err){

console.error(err);

setError(
"Could not load files"
);

}


}


loadFiles();


},[]);



return (

<div

style={{
background:"#111",
padding:"20px",
borderRadius:"15px",
height:"500px",
overflow:"auto"
}}

>


<h2>
Files
</h2>



{
error &&

<p>
{error}
</p>

}



{

files.map(
(file)=>(


<div

key={file}

onClick={()=>onSelect(file)}

style={{

cursor:"pointer",
padding:"8px",
borderBottom:"1px solid #222"

}}

>


{file}


</div>


)

)


}



</div>


)


}
