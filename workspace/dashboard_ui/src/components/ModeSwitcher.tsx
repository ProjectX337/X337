import type {DashboardMode} from "../state/dashboardMode";


interface Props {

mode:DashboardMode;

setMode:(mode:DashboardMode)=>void;

}


export default function ModeSwitcher({
mode,
setMode
}:Props){


return (

<div>


<button onClick={()=>setMode("overview")}>
Overview
</button>


<button onClick={()=>setMode("code")}>
Code
</button>


<button onClick={()=>setMode("preview")}>
Preview
</button>


<button onClick={()=>setMode("agents")}>
Agents
</button>


<h3>
Current Mode: {mode}
</h3>


</div>

)

}
