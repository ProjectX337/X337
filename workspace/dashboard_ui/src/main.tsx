import ReactDOM from "react-dom/client";

import App from "./App";

import {
ProjectProvider
} from "./context/ProjectContext";


ReactDOM.createRoot(
document.getElementById("root")!
)
.render(

<ProjectProvider>

<App />

</ProjectProvider>

);
