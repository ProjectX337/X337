

import {

BrowserRouter,

Routes,

Route

} from "react-router-dom";


import Landing from "./pages/Landing";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Lesson from "./pages/Lesson";
import Profile from "./pages/Profile";



export default function App(){


return (

<BrowserRouter>

<Routes>



<Route
path="/"
element={<Landing/>}
/>



<Route
path="/login"
element={<Login/>}
/>



<Route
path="/dashboard"
element={<Dashboard/>}
/>



<Route
path="/lesson"
element={<Lesson/>}
/>



<Route
path="/profile"
element={<Profile/>}
/>



</Routes>

</BrowserRouter>

)

}

