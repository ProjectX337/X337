import {
useState
} from "react";

import FileExplorer from "./FileExplorer";
import CodeViewer from "./CodeViewer";
import PreviewPanel from "./PreviewPanel";



interface Props{

project:any;

}



export default function ProjectWorkspace(
{
project
}:Props
){


const [selectedFile,setSelectedFile]
=
useState("");



return (

<div>


<h2>
Project Workspace
</h2>



<div

style={{

display:"grid",
gridTemplateColumns:"300px 1fr",
gap:"20px"

}}

>


<FileExplorer

onSelect={
setSelectedFile
}

/>



<CodeViewer

file={
selectedFile
}

/>


</div>



<PreviewPanel

project={project}

/>


</div>

)

}
