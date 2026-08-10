import React from "react";
import type { RouteObject } from "react-router-dom";


import Landing from "./pages/Landing";

import Dashboard from "./pages/Dashboard";

import Settings from "./pages/Settings";

import Billing from "./pages/Billing";

import API from "./pages/API";


export const routes: RouteObject[] = [

  {
    path: "/",
    element: <Landing />,
  },

  {
    path: "/dashboard",
    element: <Dashboard />,
  },

  {
    path: "/settings",
    element: <Settings />,
  },

  {
    path: "/billing",
    element: <Billing />,
  },

  {
    path: "/api",
    element: <API />,
  },

];
