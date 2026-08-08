import {useState} from "react";
import {useProject} from "../context/ProjectContext";


export default function PromptConsole(){


const [prompt,setPrompt]=useState("");

const [loading,setLoading]=useState(false);


const {setProject}=useProject();



async function generate(){


if(!prompt){

return;

}


setLoading(true);


try{


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


console.log(
"X337 Generated:",
data
);



setProject(data);



}

catch(error){


console.error(
"Generation failed",
error
);


}


setLoading(false);


}



return(

<div>


<h2>
X337 Builder
</h2>


<textarea

value={prompt}

onChange={
(e)=>setPrompt(e.target.value)
}


placeholder="Describe the project you want X337 to build..."

style={{

width:"100%",
height:"120px",
background:"#111",
color:"white",
padding:"15px",
borderRadius:"10px"

}}

/>



<button

onClick={generate}

style={{

marginTop:"15px",
padding:"12px 25px",
borderRadius:"8px",
cursor:"pointer"

}}

>

{
loading
?
"Generating..."
:
"Generate Project"
}


</button>


</div>

)


}
