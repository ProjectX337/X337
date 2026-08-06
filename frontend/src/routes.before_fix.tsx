import Analytics from "./features/analytics/pages/analytics";
import Login from "./features/authentication/pages/login";
import Signup from "./features/authentication/pages/signup";
import Billing from "./features/payments/pages/billing";
import Checkout from "./features/payments/pages/checkout";
import AI from "./features/ai/pages/ai";
import Contacts from "./features/crm/pages/contacts";
import Dashboard from "./features/dashboard/pages/dashboard";
import Landing from "./pages/Landing";
import Settings from "./pages/Settings";
import API from "./pages/API";

export const routes = [
{
    path: "/analytics",
    element: <Analytics />,
},
{
    path: "/login",
    element: <Login />,
},
{
    path: "/signup",
    element: <Signup />,
},
{
    path: "/billing",
    element: <Billing />,
},
{
    path: "/checkout",
    element: <Checkout />,
},
{
    path: "/ai",
    element: <AI />,
},
{
    path: "/contacts",
    element: <Contacts />,
},
{
    path: "/dashboard",
    element: <Dashboard />,
},
{
    path: "/",
    element: <Landing />,
},
{
    path: "/settings",
    element: <Settings />,
},
{
    path: "/api",
    element: <API />,
},
];