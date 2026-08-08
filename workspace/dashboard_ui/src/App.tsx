import {useState} from "react";

import ModeSwitcher from "./components/ModeSwitcher";

import type {DashboardMode} from "./state/dashboardMode";


function App(){

const [mode,setMode] = useState<DashboardMode>(
    "overview"
);


return (

<div style={{
    padding:"40px",
    fontFamily:"Arial"
}}>


<h1>
X337 Dashboard
</h1>


<ModeSwitcher
    mode={mode}
    setMode={setMode}
/>



{
mode==="overview" &&
<div>

<h2>
Project Overview
</h2>

<p>
X337 Generated Application Dashboard
</p>

</div>
}



{
mode==="code" &&
<div>

<h2>
Code Explorer
</h2>

<p>
Generated files will appear here.
</p>

</div>
}



{
mode==="preview" &&
<div>

<h2>
Generated App Preview
</h2>

</div>
}



{
mode==="agents" &&
<div>

<h2>
Agent Activity
</h2>

</div>
}



</div>

)

}


export default App;
