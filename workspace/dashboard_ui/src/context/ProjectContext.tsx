import {
createContext,
useContext,
useState
} from "react";


const ProjectContext = createContext<any>(null);


export function ProjectProvider({
children
}:{
children:any
}){


const [project,setProject]=useState(null);


return (

<ProjectContext.Provider

value={{
project,
setProject
}}

>

{children}

</ProjectContext.Provider>


)


}


export function useProject(){

return useContext(ProjectContext);

}
