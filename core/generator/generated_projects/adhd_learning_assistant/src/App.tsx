
import React from "react";

import Dashboard from "./pages/Dashboard";
import Practice from "./pages/Practice";
import Profile from "./pages/Profile";

export default function App() {

    return (
        <div
            style={{
                minHeight: "100vh",
                padding: "40px",
                fontFamily: "Inter, sans-serif",
                background: "#f5f7fb"
            }}
        >

            <h1>
                ADHD Learning Assistant
            </h1>

            <Dashboard />

            <Practice />

            <Profile />

        </div>
    );
}
