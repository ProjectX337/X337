import { useState } from "react";
import { useProject } from "../context/ProjectContext";


export default function ProjectInput(){


const {
    setProject
}=useProject();


const [prompt,setPrompt]=useState("");

const [loading,setLoading]=useState(false);



async function generate(){


setLoading(true);


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


const data = await response.json();


setProject(data);


setLoading(false);


}



return (

<div
style={{
padding:"30px",
color:"white"
}}
>


<h2>
Create Project
</h2>


<input

value={prompt}

onChange={
(e)=>setPrompt(e.target.value)
}

placeholder="Describe what you want X337 to build..."

style={{
width:"400px",
padding:"12px"
}}

/>


<button

onClick={generate}

style={{
marginLeft:"10px",
padding:"12px"
}}

>

{
loading
?
"Generating..."
:
"Generate"
}

</button>


</div>

)

}
