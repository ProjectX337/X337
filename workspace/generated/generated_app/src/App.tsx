

import {

BrowserRouter,

Routes,

Route

} from "react-router-dom";


import Dashboard from "./pages/Dashboard";
import Lesson from "./pages/Lesson";
import Profile from "./pages/Profile";
import ReadingCoach from "./pages/ReadingCoach";
import Practice from "./pages/Practice";
import Planner from "./pages/Planner";
import Focus from "./pages/Focus";



export default function App(){


return (

<BrowserRouter>

<Routes>



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



<Route
path="/readingcoach"
element={<ReadingCoach/>}
/>



<Route
path="/practice"
element={<Practice/>}
/>



<Route
path="/planner"
element={<Planner/>}
/>



<Route
path="/focus"
element={<Focus/>}
/>



</Routes>

</BrowserRouter>

)

}

