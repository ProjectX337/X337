import {useEffect,useState} from "react";


interface Props{

file:string;

}



export default function CodeViewer(
{
file
}:Props
){


const [code,setCode]=useState("");



useEffect(()=>{


if(!file)
return;



async function loadCode(){


const response =
await fetch(

`http://localhost:9001/api/file?path=${file}`

);



const data =
await response.json();


setCode(data.code);


}


loadCode();


},[file]);



return (

<div

style={{

background:"#050505",
padding:"20px",
borderRadius:"15px",
height:"500px",
overflow:"auto"

}}

>


<h2>
Code
</h2>


<pre>

{code ||
"Select a file"}

</pre>


</div>


)

}
